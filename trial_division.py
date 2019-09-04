from math import sqrt


def is_prime(number):

    if number < 6:
        return number in {2, 3, 5}

    if not number % 2 or not number % 3:
        return False

    end = int(sqrt(number)) + 1
    for i in range(5, end, 6):
        if not number % i or not number % (i + 2):
            return False
    return True

