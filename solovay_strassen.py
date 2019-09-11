from random import randint
from utils.jacobi import jacobi


def is_probably_prime(n, k=1):
    """
    Solovay–Strassen primality test

    :param n: Number to be tested
    :param k: number of iterations, more iterations equals higher accuracy and time complexity
    :return: True if number is probably prime, False otherwise
    """

    if n < 3 or not n % 2:
        return n == 2

    for _ in range(k):
        a = randint(2, n - 1)
        x = jacobi(a, n)
        if not x or pow(a, (n - 1)//2, n) != x % n:
            return False

    return True
