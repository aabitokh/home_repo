if __name__ == "__main__": 
    with open('', 'r') as f:
        contents = f.read()
    values = contents.split('\n\n')
    fat_elf = 0
    for i in range(len(values)):
        elf_i_fat = sum(list(map(int, values[i].split('\n'))))
        if elf_i_fat > fat_elf:
            fat_elf = elf_i_fat
    print(fat_elf)
