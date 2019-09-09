from math import sqrt


def is_prime(n):
    """
    Trial division

    :param n: Number to be tested
    :return: True if number is prime, otherwise False
    """

    if n < 6:
        return n in {2, 3, 5}

    if not n % 2 or not n % 3:
        return False

    end = int(sqrt(n)) + 1
    for i in range(5, end, 6):
        if not n % i or not n % (i + 2):
            return False
    return True

