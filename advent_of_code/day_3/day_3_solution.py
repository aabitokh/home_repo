import string

def make_alphabet():

    points = {}
    alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)

    for num, el in enumerate(alphabet):
        points[el] = num+1
    
    return points

def backpack_intersection(backpack):

    length = len(backpack)
    middle_index = length//2
    first_half = backpack[:middle_index]
    second_half = backpack[middle_index:]

    set.intersection(set(first_half), set(second_half))

    intTuple = tuple(set(first_half) & set(second_half))

    return list(intTuple)[0]


if __name__ == "__main__":

    with open('/Users/aabitokh/Desktop/repo/Assir-Bitokhov/advent_of_code/day_3/input.txt', 'r') as f:
        input_file = f.read()

    backpacks = input_file.split('\n')
    int_list = []
    points_dict = make_alphabet()
    points = []

    for backpack in backpacks:
        int_list.append(backpack_intersection(backpack))
    
    for int_el in int_list: 
        points.append(points_dict[int_el])

    print(sum(points))


