a,d = input().split()
x = abs(ord(a[0]) - ord(d[0]))
y = abs(ord(a[1]) - ord(d[1]))
if (x == 1 and y == 2)  or (x == 2 and y == 1):
    print('VALIDO')
else:
    print('INVALIDO')
