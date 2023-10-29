test = 1
while True:
    m = int(input())

    if m == 0:
        break

    calculator = input()
    operators = []

    for i in range(len(calculator)):
        if not calculator[i].isnumeric():
            operators.append(calculator[i])


    calculator = calculator.replace('-','+').split('+')
    for i in range(len(calculator)):
        calculator[i] = int(calculator[i])

    count = calculator[0]

    for i in range(len(operators)):
        if operators[i] == '+':
            count += calculator[i+1]
        else:
            count -= calculator[i+1]


    print("Teste {}".format(test))
    print(count)
    print()
    test += 1