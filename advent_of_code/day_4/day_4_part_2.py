with open('/Users/aabitokh/Desktop/repo/Assir-Bitokhov/advent_of_code/day_4/input.txt', 'r') as f:
    input_file = f.read()

pairs = input_file.split('\n')

target = 0 

for i in range(len(pairs)):

    start_first = int(pairs[i].split(',')[0].split('-')[0])
    end_first = int(pairs[i].split(',')[0].split('-')[1])

    start_second = int(pairs[i].split(',')[1].split('-')[0])
    end_second = int(pairs[i].split(',')[1].split('-')[1])

    range_first = [i for i in range(start_first, end_first+1)]
    range_second = [i for i in range(start_second, end_second+1)]

    ints = set.intersection(set(range_first), set(range_second))

    if len(ints) > 0:
        target = target + 1 
    else:
        continue

print(target)