def get_elfs_items():
    with open('./data.txt', 'r') as input:
        data = input.readlines()
        elf = []
        elfs = []
        for line in data:
            if (line == '\n'):
                elfs.append(sum(elf))
                elf = []
                continue
            elf.append(int(line.replace('\n', '')))
    return elfs

if __name__ == '__main__':
  print(max(get_elfs_items()))
