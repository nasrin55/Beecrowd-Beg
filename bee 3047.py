m = int(input())
a = int(input())
b = int(input())
c = m - (a + b)
children = [a, b, c]
print(max(children))