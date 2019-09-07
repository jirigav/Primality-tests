from random import randint
from sympy.ntheory import factorint  # sympy required "pip install sympy"


def is_probably_prime(number, loops):

    if number < 3 or not number % 2:
        return number == 2

    for _ in range(loops):
        b = True

        a = randint(2, number - 1)

        if pow(a, number - 1, number) != 1:
            return False

        p_factors = factorint(number - 1)

        for q in p_factors:
            if pow(a, (number - 1)//q, number) == 1:
                b = False
                break

        if b:  # get rid off b would be nice
            return True

    return False



