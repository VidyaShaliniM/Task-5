word = input()
letter_list = []
vowels = ['a', 'e', 'i', 'o', 'u']
# split the input string into a list of letters
for char in word:
    letter_list.append(char)

# function to remove vowels in the given string


def remove_vowels(v):
    new_list = []
    for i in letter_list:
        if i not in vowels:
            new_list.append(i)
    return new_list


print(''.join(remove_vowels(word)))

