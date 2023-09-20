# Guvi Geeks Network Private Limited is the given input string

word = "Guvi Geeks Network Private Limited"
total_count = 0
vowels_list = []
letters_list = []
# for splitting the string into a list of characters
for char in word:
    if char != ' ':
        letters_list.append(char)

# for finding the count of all the vowels in the given string
for char in letters_list:
    if (char == 'a') or (char == 'e') or (char == 'i') or (char == 'o') or (char == 'u'):
        total_count = total_count + 1
        vowels_list.append(char)

# function to find the count of individual vowels in the given string

        def vowel_count(ch):
            v_count = 0
            for i in vowels_list:
                if ch == i:
                    v_count = v_count + 1
            return v_count

print('Number of vowels in the given string are :', total_count)
print('Count of letter A is',vowel_count('a'))
print('Count of letter E is', vowel_count('e'))
print('Count of letter I is', vowel_count('i'))
print('Count of letter O is', vowel_count('o'))
print('Count of letter U is', vowel_count('u'))
