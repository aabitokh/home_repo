with open('/Users/aabitokh/Desktop/repo/Assir-Bitokhov/advent_of_code/day_4/input.txt', 'r') as f:
    input_file = f.read()

pairs = input_file.split('\n')


target = 0 

for i in range(len(pairs)):
    start_first = int(pairs[i].split(',')[0].split('-')[0])
    end_first = int(pairs[i].split(',')[0].split('-')[1])

    start_second = int(pairs[i].split(',')[1].split('-')[0])
    end_second = int(pairs[i].split(',')[1].split('-')[1])

    if start_first <= start_second and end_first >= end_second:
        target = target + 1 

    elif start_second <= start_first and end_second >= end_first:
        target = target + 1 
    else: 
        continue

print(target)