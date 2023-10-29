n,g = map(int, input().split())
list1 = []
for i in range(n):
    v = input().split()
    list1.append(v)

n1 = int(input())
list2 = input().split()

result = 0

for i in range(n):
    for j in range(n1):
        if list1[i][0] == list2[j]:
            result += int(list1[i][-1])

print(result)
if result >= g:
    print('You shall pass!')
else:
    print('My precioooous')