fib = [1, 1]
for i in range(2, 41):
    fib.append(fib[i-1] + fib[i-2])
fib.sort(reverse=True)
n = int(input())
result = ''
for i in fib[41-n:]:
    result += str(i) + ' '

result = result[:-1]
print(result)