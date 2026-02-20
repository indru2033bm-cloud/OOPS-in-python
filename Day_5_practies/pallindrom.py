def Revers(s):
    n = len(s)
    r = ""
    for i in range(n-1 , -1 ,-1):
        r += s[i]
    return r == s

    
  
s = "madam"
print(f"{Revers(s)}")

