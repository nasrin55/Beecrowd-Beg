n = int(input())
m = int(input())
fig = [0] * n
while m:
    m -= 1
    fig[int(input()) - 1] = 1
count = fig.count(0)
print(count)