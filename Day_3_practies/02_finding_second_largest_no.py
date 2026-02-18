def Second(l):
    # for i in range(0 , 3):
    #     if l[i] > l[i + 1]:
    #      if l[ i + 1] > l[i]:
    #         return l[i + 1]
    #      else:
    #         return l[i]
    return l
    for i in range(0 , 3):
        if l[i] < l[i + 1]:
            temp = l[i]
            l[i] = l[i + 1]
            l[i + 1] = temp
    return l

    

    
            



print(Second([10,20,23,26]))