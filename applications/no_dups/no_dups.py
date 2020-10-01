def no_dups(s):
    # Your code here
    #pull out individual words
    words = s.split()
    seen = {}
    result = []
    for word in words:
        if word not in seen:
            result.append(word)
            seen[word] = True
    return " ".join(result)



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))