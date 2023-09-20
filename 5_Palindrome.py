input_word = input()
# function to check if the input string is a palindrome


def is_palindrome(a):
    rev = ''.join(reversed(a))
    if a == rev:
        return True
    return False


print(is_palindrome(input_word))