from random import randint


def is_probably_prime(n, k=1):
    """
    Miller–Rabin primality test

    :param n: Number to be tested
    :param k: number of iterations, more iterations equals higher accuracy and time complexity
    :return: True if number is probably prime, otherwise False
    """
    if n < 4:
        return n == 2 or n == 3

    d = n - 1
    s = 0
    while not d % 2:
        s += 1
        d //= 2
    for i in range(k):
        a = randint(2, n - 2)
        x = pow(a, d, n)

        if x == 1 or x == (n - 1):
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == (n - 1):
                break
        else:
            return False

    return True
