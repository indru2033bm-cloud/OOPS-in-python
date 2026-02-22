def largest(sent):
    le = 0
    for i in range(len(sent)):
        if sent[i] != " " and (i == 0 or sent[i - 1] == " "):
        
            le += 1
    return le

print(largest("I love python"))