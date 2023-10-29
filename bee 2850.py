while True:
    try:
        a = input()
        if a == 'direita':
            print('frances')
        elif a == 'esquerda':
            print('ingles')
        elif a == 'nenhuma':
            print('portugues')
        elif a == 'as duas':
            print('caiu')


    except EOFError:
        break