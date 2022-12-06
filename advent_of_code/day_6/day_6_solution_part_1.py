with open('/Users/aabitokh/Desktop/repo/Assir-Bitokhov/advent_of_code/day_6/input.txt', 'r') as f:
    input_file = f.read()

ans = []
line_check = []
n = 14 #4 for part 1
for num, el in enumerate(input_file):
    if num < n: 
        print(num, el)
        line_check.append(el)
    else: 
        line_check.pop(0)
        line_check.append(el)
        print('new linecheck', line_check)
        if len(line_check) == len(set(line_check)):
            ans.append(num)

print(ans)
