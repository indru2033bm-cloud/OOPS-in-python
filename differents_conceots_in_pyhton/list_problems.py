# a = [1,2,3]
# a = a + [4]
# print(a)
l = []
for i in range(1,10):
    l.append(int(input("Enter the element: ")))
# print(l)
result = []
for i in l:
    if i not in result:
        result.append(i)
print(l)
print(result)