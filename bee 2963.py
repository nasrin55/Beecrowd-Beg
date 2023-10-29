n = int(input())
c = int(input())
p = True

for i in range(n-1):
    x = int(input())
    if c < x:p = False
if p:
    print('S')
else:
    print('N')