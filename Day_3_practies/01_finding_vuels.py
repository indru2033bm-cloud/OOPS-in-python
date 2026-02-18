def voles():
    str = input("Enter a streng: ")
    c = 0
    for i in str:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
            print(i)
            c += 1
    print(c)

voles()