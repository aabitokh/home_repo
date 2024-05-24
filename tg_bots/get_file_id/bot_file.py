from aiogram import Bot, Dispatcher, F
from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, InputMediaAudio,
                           InputMediaDocument, InputMediaPhoto,
                           InputMediaVideo, Message)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import CommandStart
from aiogram.exceptions import TelegramBadRequest
from dotenv import load_dotenv
import os 
# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather

load_dotenv()
BOT_TOKEN = os.getenv("TOKEN")

bot = Bot(BOT_TOKEN)
dp = Dispatcher()


LEXICON: dict[str, str] = {
    'audio': '🎶 Аудио',
    'text': '📃 Текст',
    'photo': '🖼 Фото',
    'video': '🎬 Видео',
    'document': '📑 Документ',
    'voice': '📢 Голосовое сообщение',
    'text_1': 'Это обыкновенное текстовое сообщение, его можно легко отредактировать другим текстовым сообщением, но нельзя отредактировать сообщением с медиа.',
    'text_2': 'Это тоже обыкновенное текстовое сообщение, которое можно заменить на другое текстовое сообщение через редактирование.',
    'photo_id1': 'AgACAgIAAxkBAAIB0mZQoRYn_DN3TSyjGXKGG5pVjXNXAAIM2zEb_yuJSr31k2KAFVWwAQADAgADcwADNQQ',
    'photo_id2': 'AgACAgIAAxkBAAIB02ZQoRzd7-wdfWHHzDEMUbXhxPGXAAIO2zEb_yuJSkZb26q0HY0KAQADAgADcwADNQQ',
    'voice_id1': 'AwACAgIAAxkBAAIB1GZQoSTTvmCZGGpIy2rDSK2zCTiJAALXRwAC_yuJSv7agt7_uQ04NQQ',
    'voice_id2': 'AwACAgIAAxkBAAIB1WZQoShKTOXWYD5HQzlzZQXm4YZBAALYRwAC_yuJSkTIVq4oFjpVNQQ',
    'audio_id1': 'CQACAgIAAxkBAAIVRWPKsPl83xynqlF9YvF5MRyF9GxeAAL1JAACkhBZSmyFCDY61yX8LQQ',
    'audio_id2': 'CQACAgIAAxkBAAIVR2PKsXppkdhAnOlqwpOHDJivtfvJAAL4JAACkhBZSoMVyPSB59h5LQQ',
    'document_id1': 'BQACAgIAAxkBAAIB2GZQoUoQE6ZVBdII6YZ7XhB22TKcAAIDQgAC-9ZpSo6DSjpGjffMNQQ',
    'document_id2': 'BQACAgIAAxkBAAIB2WZQoU4cLAxAdR3zUGNegx0tMgaXAAIDQgAC-9ZpSo6DSjpGjffMNQQ',
    'video_id1': 'BAACAgIAAxkBAAIB1mZQoTJQV3KRypMXVbMV9VXJnOHwAALZRwAC_yuJSrUBdNEjs7U9NQQ',
    'video_id2': 'BAACAgIAAxkBAAIB12ZQoTodBXuYNvb6Quqyxpjk0rHPAALaRwAC_yuJSlRRu4TA6hsdNQQ',
}


# Функция для генерации клавиатур с инлайн-кнопками
def get_markup(width: int, *args, **kwargs) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder = InlineKeyboardBuilder()
    # Инициализируем список для кнопок
    buttons: list[InlineKeyboardButton] = []
    # Заполняем список кнопками из аргументов args и kwargs
    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(
                text=LEXICON[button] if button in LEXICON else button,
                callback_data=button
            ))
    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(
                text=text,
                callback_data=button
            ))
    # Распаковываем список с кнопками в билдер методом row c параметром width
    kb_builder.row(*buttons, width=width)
    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()


# Этот хэндлер будет срабатывать на команду "/start"
# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(CommandStart())
async def process_start_command(message: Message):
    markup = get_markup(2, 'text')
    await message.answer(
        text=LEXICON['text_1'],
        reply_markup=markup
    )


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
@dp.callback_query(F.data.in_(
    ['text', 'audio', 'video', 'document', 'photo', 'voice']
))
async def process_button_press(callback: CallbackQuery):
    markup = get_markup(2, 'text')
    if callback.message.text == LEXICON['text_1']:
        text = LEXICON['text_2']
    else:
        text = LEXICON['text_1']
    await callback.message.edit_text(
        text=text,
        reply_markup=markup
    )



# Этот хэндлер будет срабатывать на все остальные сообщения
@dp.message()
async def send_echo(message: Message):
    await message.answer(text='Не понимаю')


if __name__ == '__main__':
    dp.run_polling(bot)