for i in range(int(input())):
    input()
    e = [int(x) for x in input().split()]
    v = [x for x in e if x % 2 != 0]
    case = True
    while len(v) > 0:
        if case:
            print(max(v), end='')
            v.remove(max(v))
            case = False
            if len(v) > 0:
                print(end=' ')
        else:
            print(min(v), end='')
            v.remove(min(v))
            case = True
            if len(v) > 0:
                print(end=' ')
    print()