def iseven(n):
    sum = 0
    for i in n:
        if i % 2 == 0:
           sum += i

    return sum




l = []
for i in range(1,10):
    l.append(int(input("Enter an element: ")))


# iseven(l)
print(iseven(l))


    