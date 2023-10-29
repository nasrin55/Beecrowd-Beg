def Fibonot(k):
    prevPrev = 1
    prev = 2
    curr = 3

    while k > 0:
        prevPrev = prev
        prev = curr
        curr = prevPrev + prev

        k = k - (curr - prev - 1)
    k = k + (curr - prev - 1)

    return prev + k

k = int(input())
print(Fibonot(k))