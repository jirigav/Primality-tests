from random import randint
from sympy.ntheory import factorint  # sympy required "pip install sympy"


def is_probably_prime(n, k=1):
    """
    Lucas primality test

    :param n: Number to be tested
    :param k: number of iterations, more iterations equals higher accuracy and time complexity
    :return: True if number is probably prime, otherwise False
    """

    if n < 3 or not n % 2:
        return number == 2

    for _ in range(k):

        a = randint(2, n - 1)

        if pow(a, n - 1, n) != 1:
            return False

        p_factors = factorint(n - 1)

        for q in p_factors:
            if pow(a, (n - 1)//q, n) == 1:
                break

        else:
            return True

    return False



