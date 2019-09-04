from random import randint


def is_probably_prime(n, loops):

    if n < 4:
        return n == 2 or n == 3

    for _ in range(loops):

        a = randint(2, n - 2)
        if pow(a, n - 1, n) != 1:
            return False

    return True
