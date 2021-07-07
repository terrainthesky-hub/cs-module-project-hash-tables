# Your code here
f = open("robin.txt", "r")
f = f.read()

def histogrammer(s):
    #Need a count of every word
    #need to print out word, with counted amount of hashes
    #ordered by which has most count
    
    #clean text, split it, ignore special characters
    #get counts of each character
    #sort character by their counts
    #for each word print its hash count in hashes
    #hash marks should be left justified two spaces after the longest word
    no_punct = str.maketrans('', '', '":;,.-+=/\\|[]{}()*^&')
    s = s.translate(no_punct).lower()
    text = s.split()
    my_dict = {}

    for item in text:
        if item not in my_dict:
            my_dict[item] = -1
        else:
            my_dict[item] -= 1
    s_dict = sorted(my_dict.items(), key=lambda kv:(kv[1], kv[0]))
    for x, y in s_dict:
        print(f"{x}  {'#'*-y}")

histogrammer(f)