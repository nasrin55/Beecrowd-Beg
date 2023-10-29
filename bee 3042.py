while True:
    m = int(input())
    if m == 0:
        break


    pos = 2
    count = 0

    for i in range(m):
        line = input()
        lines = line.split()

        if lines == ['0', '1', '1']:
            count += abs(pos-1)
            pos = 1
        elif lines == ['1', '0', '1']:
            count += abs(pos - 2)
            pos = 2
        elif lines == ['1', '1', '0']:
            count += abs(pos - 3)
            pos = 3

    print(count)