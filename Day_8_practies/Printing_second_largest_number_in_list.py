def printsec(l):
    n = len(l)
    curren = 0
    index = 1
    for i in range(0 , n):
        
        if l[i] < l[index]:
            curren += l[index]
        index += 1
    return curren


    

print(printsec([ 2 , 3 , 4 , 1 , 5]))