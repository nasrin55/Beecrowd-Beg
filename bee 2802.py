from math import pow
n = int(input())
c = (n/24) * (pow(n,3) - 6*pow(n,2) + 23*n - 18) + 1
print('%.0f'%c)