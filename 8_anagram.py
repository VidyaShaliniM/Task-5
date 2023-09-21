#function to check if two strings are anagram or not
s1 = input()
s2 = input()


def anagram(w1, w2):
    if (sorted(w1) == sorted(w2)):
        return True
    else:
        return False


print(anagram(s1, s2))
