word = input()
char_freq = {}
# function to find the most frequent character


def most_freq_char(a):
    for i in word:
        if i in char_freq:
          char_freq[i] = char_freq[i] + 1
    else:
        char_freq[i] = 1
        result = max(char_freq, key= char_freq.get)
        return result
print('most frequent character is: ',most_freq_char(word))