if __name__ == "__main__": 
    with open('', 'r') as f:
        contents = f.read()
    values = contents.split('\n\n')
    fat_elv = 0
    for i in range(len(values)):
        elv_i_fat = sum(list(map(int, values[i].split('\n'))))
        if elv_i_fat > fat_elv:
            fat_elv = elv_i_fat
    print(fat_elv)
