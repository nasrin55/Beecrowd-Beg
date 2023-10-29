t = int(input())
for i in range(t):
    n,k = input().split()
    n = int(n)
    k = int(k)
    total = int(int(n%k) + int(n/k))
    print(total)