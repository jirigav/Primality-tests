from random import randint


def is_probably_prime(n, k=1):
    """
    Fermat primality test

    :param n: Number to be tested
    :param k: number of iterations, more iterations equals higher accuracy and time complexity
    :return: True if number is probably prime, otherwise False
    """

    if n < 4:
        return n == 2 or n == 3

    for _ in range(k):

        a = randint(2, n - 2)
        if pow(a, n - 1, n) != 1:
            return False

    return True
