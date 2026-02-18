def iseven(n):
    s = 0
    c = 0
    for i in n:
       
        if i % 2 == 0:
           s += i
           c += 1
        
    print(f"No of even {c}")

    return s 


l = []
for i in range(1,10):
    l.append(int(input("Enter an element: ")))


# iseven(l)
print(iseven(l))
