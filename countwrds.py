def howMany(sentence):
    count = 0
    flag = 1
    for i in range(len(sentence)):
        if ((ord(sentence[i]) >= 65 and ord(sentence[i]) <= 90) or (ord(sentence[i]) >= 97 and ord(sentence[i]) <= 122) or sentence[i] == "-" or sentence[i] == "," or sentence[i] == "." or sentence[i] == "!" or sentence[i] == "?"):
            pass
        elif (ord(sentence[i]) == 32):
            if flag == 0:
                flag = 1
                continue
            else:
                count = count + 1
                flag = 1  
        else:
            flag = 0
    count = count + 1
    
    return count
sentence = "he is a good programmer, ?"
print(howMany(sentence))