# John Asare
# Jun 19 2020

""" Write a Python function that checks whether a passed in string is palindrome or not.
Note: A palindrome is word, phrase, or sequence that reads the same backward as forward,
e.g., madam or nurses run."""


def palindrome(s):
    rvsd = ''
    for letter in reversed(s):
        rvsd += letter
    return rvsd == s


print(palindrome('helleh'))
print(palindrome('John'))

