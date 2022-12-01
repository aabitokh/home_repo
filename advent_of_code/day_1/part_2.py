if __name__ == "__main__": 
    with open('', 'r') as f:
        contents = f.read()
    values = contents.split('\n\n')
    elf_list = []
    for i in range(len(values)):
        elf_list.append(sum(list(map(int, values[i].split('\n')))))
    elf_list = sorted(elf_list)
    print(sum(elf_list[-3:]))
