e,d = map(int, input().split())
if e > d:
    print('Eu odeio a professora!')
elif (d - e) >= 3:
    print('Muito bem! Apresenta antes do Natal!')
elif (e+2 < 24 ):
    print("Parece o trabalho do meu filho!\nTCC Apresentado!")
else:
    print("Parece o trabalho do meu filho!\nFail! Entao eh nataaaaal!")
