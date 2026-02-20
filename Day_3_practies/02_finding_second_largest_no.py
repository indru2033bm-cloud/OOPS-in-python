# def Second(l):
#     # for i in range(0 , 3):
#     #     if l[i] > l[i + 1]:
#     #      if l[ i + 1] > l[i]:
#     #         return l[i + 1]
#     #      else:
#     #         return l[i]
#     # return l

l = [20,45,23,65,34]
n = 0
for i in l:
    n += 1
for i in range(1 , n + 1):
    if l[i] < l[i + 1]:
        temp = l[i]
        l[i] = l[i + 1]
        l[i + 1] = temp

print(l)







    

    
            



