def Remove_duplicent(l):
    result = []
    for i in l:
        if i not in result:
            result.append(i)
    return result
    

print((Remove_duplicent([1,2,2,3,4,5,2,5,3,6,7,5])))