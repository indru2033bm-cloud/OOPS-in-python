def count_words(sent):
    count = 0
    for  i in range(len(sent)):
        if sent[i] != " " and (i == 0 or sent[i - 1] == " ") :
            count += 1
    return count

        
    #     if sent.startswith(" ") == " " or sent.endswith(" ") == " ":
    #         if i == " ":
    #             count += 1
    #         count - 2
    
    # return count


print(count_words(" I love python "))
