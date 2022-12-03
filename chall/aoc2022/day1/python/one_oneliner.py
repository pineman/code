with open('../input/1/input') as f:
    result = sorted(sum(map(int, elf.split('\n'))) for elf in f.read().rstrip().split('\n\n'))
    print(result[-1])
    print(result[-3:])
    print(sum(result[-3:]))

