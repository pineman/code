import sys

history = ['']
buf = ''

for line in sys.stdin.readlines()[1:]:
    op = line.strip().split()
    if op[0] == '1':
        history.append((op[0], op[1]))
        buf += op[1]
    elif op[0] == '2':
        history.append((op[0], buf[-int(op[1]):]))
        buf = buf[:-int(op[1])]
    elif op[0] == '3':
        print(buf[int(op[1])-1])
    elif op[0] == '4':
        undo = history.pop()
        if undo[0] == '1':
            buf = buf[:-len(undo[1])]
        elif undo[0] == '2':
            buf += undo[1]
        else:
            print('unreachable')
            sys.exit()
    else:
        print('unsupported operation:', op)
        sys.exit()
