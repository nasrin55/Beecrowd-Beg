from math import ceil
v,n = map(int, input().split())
t = v*n
m = []
for i in range(10, 100, 10):
    m.append(ceil(i*t/100))
print('{} {} {} {} {} {} {} {} {}'.format(*m))