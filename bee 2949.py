n = int(input())
entry = []
x = 0
h = 0
e = 0
a = 0
m = 0
for i in range(n):
    entry = input().split()
    if entry[-1] == 'X':
        x = x + 1
    elif entry[-1] == 'H':
        h = h + 1
    elif entry[-1] == 'E':
        e = e + 1
    elif entry[-1] == 'A':
        a = a + 1
    elif entry[-1] == 'M':
        m = m + 1
print(x, 'Hobbit(s)')
print(h, 'Humano(s)')
print(e, 'Elfo(s)')
print(a, 'Anao(oes)')
print(m, 'Mago(s)')