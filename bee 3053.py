n = int(input())
start = input()
A = False
B = False
C = False

if start == 'A':
    A = True
elif start == "B":
    B = True
elif start == "C":
    C = True


for i in range(n):
    move = int(input())

    if move == 1:
        if A == True:
            A = False
            B = True
        elif B == True:
            A = True
            B = False
    if move == 2:
        if B == True:
            B = False
            C = True
        elif C == True:
            B = True
            C = False
    if move == 3:
        if A == True:
           A = False
           C = True
        elif C == True:
            A = True
            C = False
if A == True:
    print("A")
elif B == True:
    print("B")
elif C == True:
    print("C")