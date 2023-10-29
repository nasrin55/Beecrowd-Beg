while True:
    try:
        n = int(input())
        test = []
        for i in range(n):
            test.append(float(input()))

        print(min(test))
    except EOFError:
        break