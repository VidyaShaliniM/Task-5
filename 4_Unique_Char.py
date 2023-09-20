word = input()
new_word =word.lower()
# function to take a string and return a string with only unique characters


def unique_char(a):
    uni_char = set(new_word)
    for i in uni_char:
        return len(uni_char)


print(unique_char(word))
