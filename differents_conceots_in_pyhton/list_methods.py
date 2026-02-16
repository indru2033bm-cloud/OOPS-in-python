a = [1,2,3]
# b = a
# b.append(4)
# print(a) # [1, 2, 3, 4]
# print(b) # [1, 2, 3, 4]

b = a.copy() # or b = list(a) or b = a[:] #This mack the copy of the list a to b **but** it is not sayes that both are same 
# print(b)
# print(a)
b.append(4) #This will not change the list a because b is a copy of a, not a reference to the same list.
print(b)
print(a)
