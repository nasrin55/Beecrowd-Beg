n = int(input())
d = [int(x) for x in input().split()]
d.sort()
m = max(d) + 1

while True:
    for x in range(n):
        if m % d[x] == 0 and d[x] != 1:
            m += 1
            break
    if x == n - 1:
        break
print(m)
