from task1 import get_elfs_items
if __name__ == '__main__':
    elfs = get_elfs_items()
    elfs.sort()
    print(sum(elfs[-3:]))
