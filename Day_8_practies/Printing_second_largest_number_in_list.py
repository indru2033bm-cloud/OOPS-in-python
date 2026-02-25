def printsec(l):
    n = len(l)
    curren = 0
    for i in range(0 , n):
        
        if l[i] < l[i + 1]:
            curren += l[i + 1]
    return curren


    

print(printsec([ 2 , 3 , 4 , 1 , 5]))