with open('input') as f:
    result = sorted(sum(map(int, elf.split('\n'))) for elf in f.read().rstrip().split('\n\n'))
    print(result[-1])
    print(sum(result[-3:]))

