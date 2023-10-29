f = m = 0
for _ in range(int(input())):
    c = input()
    if(c[-1] == 'F'):
        f += 1
    else:
        m += 1
print(m,'carrinhos')
print(f,'bonecas')