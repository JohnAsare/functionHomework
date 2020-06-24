# John Asare
# Jun 19 2020

""" Write a Python function to check whether a string is pangram or not.
Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog" """

import string


def ispangram(str1, alphabet=string.ascii_lowercase):
    str1 = set(str1.replace(' ', '').lower())
    alpha_set = set(alphabet)
    return str1 == alpha_set


print(ispangram("The quick brown fox jumps over the lazy dog"))


