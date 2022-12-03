with open('/Users/aabitokh/Desktop/repo/Assir-Bitokhov/advent_of_code/day_3/input.txt', 'r') as f:
    input_file = f.read()


def make_alphabet():

    points = {}
    alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)

    for num, el in enumerate(alphabet):
        points[el] = num+1
    
    return points

backpacks = input_file.split('\n')
int_list = []
points_dict = make_alphabet()
points = []

chunk_size = 3
groups = [backpacks[i:i+chunk_size] for i in range(0, len(backpacks), chunk_size)]

for group in groups:
    intTuple = tuple(set(group[0]) & set(group[1]) & set(group[2])) 
    int_list.append(list(intTuple)[0])

for int_el in int_list: 
    points.append(points_dict[int_el])

print(sum(points))
