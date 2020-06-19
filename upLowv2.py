# John Asare
# Jun 19 2020


""" Another way for solving upLow question"""


def up_low(statement):
    for letter in statement:
        upps = statement.count(letter.isupper())
        lows = statement.count(letter.islower())
        print(f'No. of Upper characters are : {upps}')
        print(f'No. of Lower characters are : {lows}')
        #Failed

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)