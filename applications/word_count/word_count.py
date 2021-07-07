
import re

    # Your code here
def word_count(string):
    my_string = str.maketrans('', '', '":;,.-+=/\\|[]{}()*^&')
    string = string.translate(my_string).lower()
    words = string.split()  
    my_dict = {}
    for item in words:
        if item not in my_dict:
            my_dict[item] = 1
        else:
            my_dict[item] += 1
        # my_dict[item] = words.count(item)
    return my_dict


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
