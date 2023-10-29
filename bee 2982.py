n = int(input())
tv = 0 #govt grant
tg = 0 #uni expense
for i in range(n):
    t,c = input().split()
    c = int(c)
    if t == 'G':
        tg += c
       # print(tg)
    else:
        tv += c
       # print(tv)
if tg <= tv:
    print('A greve vai parar.')
else:
    print('NAO VAI TER CORTE, VAI TER LUTA!')