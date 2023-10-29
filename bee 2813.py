c = e = qc = qe = 0
n = int(input())
for i in range(n):
    sd,sn = input().split()
    if sd == 'chuva':
        if c > 0:
            c -= 1
            e += 1
        else:
            qc += 1
            e += 1
    if sn == 'chuva':
        if e > 0:
            e -= 1
            c += 1
        else:
            qe += 1
            c += 1
print(qc, qe)