def square(number):

    if number <= 0 or number > 64:
        raise ValueError("square must be between 1 and 64")

    answer = None

    if number == 1:
        answer = 1
    else:
        answer = 2 ** (number - 1)

    return answer


def total():

    return 2 ** 64 - 1
