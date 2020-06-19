# John Asare
# Jun 19 2020


""" Write a function that checks whether a number is in a given range (inclusive of high and low) """


def ran_check(num, low, high):
    for i in range(low, high + 1):
        if i == num:
            return f'{num} is in the range between {low} and {high}'


print(ran_check(5, 2, 7))
print(ran_check(3, 1, 10))
