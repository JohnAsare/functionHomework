# John Asare
# Jun 19 2020


""" Write a Python function that accepts a string and calculates the number of upper case letters and
lower case letters.
Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
Expected Output :
No. of Upper case characters : 4
No. of Lower case Characters : 33 """


def up_low(s):
    uppers = ''
    lowers = ''
    for letter in s:
        if letter.isupper():
            uppers += letter
        elif letter.islower():
            lowers += letter
    print(f'No. of Upper case characters : {len(uppers)}')
    print(f'No. of Lower case characters : {len(lowers)}')


s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)
