s1 = input().split()

# function to return the number of words in the input string


def no_of_words(w1):
    word_count = 0
    for char in s1:
        if char != ' ':
            word_count = word_count + 1
    return word_count


print(no_of_words(s1))


