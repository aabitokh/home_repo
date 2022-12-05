with open('/Users/aabitokh/Desktop/repo/Assir-Bitokhov/advent_of_code/day_5/input.txt', 'r') as f:
    input_file = f.read()

import re
import pprint


keys = input_file.split('\n\n')[0].split('\n')[-1]
values = input_file.split('\n\n')[0].split('\n')[:-1]


sector_dict = {} 
for num, el in enumerate(keys):
    if el != ' ':
        sector_dict[num] = int(el)

value_dict = {}
for key in sector_dict.keys():
    value_dict[key] = []

for value in values:
    for num , el in enumerate(value):
        if el not in ['[', ' ', ']'] and num in sector_dict.keys():
            value_dict[num].append(el)

work_place = {} 
for sector_key in sector_dict.keys(): 
    work_place[sector_dict[sector_key]] = [] 
    work_place[sector_dict[sector_key]].append(value_dict[sector_key][::-1])

moves = input_file.split('\n\n')[1].split('\n')
moves_list = []
for move in moves: 
    move_list_oder = []
    move_oder_str = re.findall(r'\d+', move)
    for move_number in move_oder_str:
        move_list_oder.append(int(move_number))
    moves_list.append(move_list_oder)

work_place_test = work_place.copy()

count = 0
for move in moves_list:
    count = count + 1
    print(move)
    x = move[0]
    y = move[1]
    z = move[2]
    for i in range(x):
        print(i, 'step')
        move_element = work_place_test[y][0][-1]
        print('column', y, work_place_test[y][0], '>delete>', move_element)
        print(work_place_test[y][0].pop(-1))
        print(z, work_place_test[z][0], 'add', move_element)
        work_place_test[z][0].append(move_element)
        print(z, work_place_test[z][0], 'added')

ans = ''

for key in work_place_test.keys():
    try:
        ans = ans + work_place_test[key][0][-1]
    except:
        pass

print(ans)
