def largest(sent):
    le = 0
    largest_len = "" 
    current_len = ""
    for i in range(len(sent)):
        if sent[i] != " ":
            current_len += sent[i]
        else:
            if len(current_len) > len(largest_len):
                largest_len = current_len
            current_len = ""
    if len(current_len) > len(largest_len):
        largest_len = current_len
                
    return largest_len

print(largest("I love python"))