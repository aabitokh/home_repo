import copy

from aiogram import Bot, Dispatcher
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import CommandStart
from aiogram.filters.callback_data import CallbackData
from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, Message)
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(filename)s:%(lineno)d #%(levelname)-8s '
            '[%(asctime)s] - %(name)s - %(message)s')

logger = logging.getLogger(__name__)
# Выводим в консоль информацию о начале запуска бота
logger.info('Starting bot')

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
#BOT_TOKEN = 'BOT TOKEN HERE'



BOT_TOKEN = '6468789742:AAFJ8_UTq11OpazNTpovmQcv1FLXnbL-G4Q'

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Инициализируем константу размера игрового поля
FIELD_SIZE = 8

# Создаем словарь соответствий
LEXICON = {
    '/start': 'Вот твое поле. Можешь делать ход',
    0: ' ',
    1: '🌊',
    2: '💥',
    'miss': 'Мимо!',
    'hit': 'Попал!',
    'used': 'Вы уже стреляли сюда!',
    'next_move': 'Делайте ваш следующий ход'
}

# Хардкодим расположение кораблей на игровом поле
ships: list[list[int]] = [
    [1, 0, 1, 1, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0]
]
logger.debug('field is prepared')
for row in ships:
    logger.debug(row)

# Инициализируем "базу данных" пользователей
users: dict[int, dict[str, list]] = {}


# Создаем свой класс фабрики коллбэков, указывая префикс
# и структуру callback_data
class FieldCallbackFactory(CallbackData, prefix="user_field"):
    x: int
    y: int


# Функция, которая пересоздает новое поле для каждого игрока
def reset_field(user_id: int) -> None:
    logger.debug(f'reset field for {user_id}')

    users[user_id]['ships'] = copy.deepcopy(ships)
    users[user_id]['field'] = [
        [0 for _ in range(FIELD_SIZE)]
        for _ in range(FIELD_SIZE)
    ]
    logger.debug(f'not it looks like')
    for row in users[user_id]['field']:
        logger.debug(row)


# Функция, генерирующая клавиатуру в зависимости от данных из
# матрицы ходов пользователя
def get_field_keyboard(user_id: int) -> InlineKeyboardMarkup:
    array_buttons: list[list[InlineKeyboardButton]] = []
    logger.debug('get field keyboard')
    #logger.debug(array_buttons)

    for i in range(FIELD_SIZE):
        array_buttons.append([])
        for j in range(FIELD_SIZE):
            array_buttons[i].append(InlineKeyboardButton(
                text=LEXICON[users[user_id]['field'][i][j]],
                callback_data=FieldCallbackFactory(x=i, y=j).pack()
            ))
            #logger.debug(array_buttons)
 
    return InlineKeyboardMarkup(inline_keyboard=array_buttons)


# Этот хэндлер будет срабатывать на команду /start, записывать
# пользователя в "базу данных", обнулять игровое поле и отправлять
# пользователю сообщение с клавиатурой
@dp.message(CommandStart())
async def process_start_command(message: Message):
    if message.from_user.id not in users:
        users[message.from_user.id] = {}
    reset_field(message.from_user.id)
    await message.answer(
        text=LEXICON['/start'],
        reply_markup=get_field_keyboard(message.from_user.id)
    )


# Этот хэндлер будет срабатывать на нажатие любой инлайн-кнопки на поле,
# запускать логику проверки результата нажатия и формирования ответа
@dp.callback_query(FieldCallbackFactory.filter())
async def process_category_press(callback: CallbackQuery,
                                 callback_data: FieldCallbackFactory):
    field = users[callback.from_user.id]['field']
    ships = users[callback.from_user.id]['ships']
    if field[callback_data.x][callback_data.y] == 0 and \
    ships[callback_data.x][callback_data.y] == 0:
        answer = LEXICON['miss']
        field[callback_data.x][callback_data.y] = 1
    elif field[callback_data.x][callback_data.y] == 0 and \
    ships[callback_data.x][callback_data.y] == 1:
        answer = LEXICON['hit']
        field[callback_data.x][callback_data.y] = 2
    else:
        answer = LEXICON['used']

    try:
        await callback.message.edit_text(
            text=LEXICON['next_move'],
            reply_markup=get_field_keyboard(callback.from_user.id)
        )
    except TelegramBadRequest:
        pass

    await callback.answer(answer)

dp.run_polling(bot)


