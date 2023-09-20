word = input()
# function to take a string and return a string with only unique characters


def unique_char(a):
    uni_char = set(word)
    for i in uni_char:
        return len(uni_char)


print(unique_char(word))
