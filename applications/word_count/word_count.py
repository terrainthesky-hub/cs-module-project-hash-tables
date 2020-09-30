
    # Your code here
def word_count(string):
    my_string = string.lower().split()
    my_dict = {}
    for item in my_string:
        my_dict[item] = my_string.count(item)
    return my_dict


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
