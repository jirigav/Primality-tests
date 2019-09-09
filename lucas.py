from random import randint
from sympy.ntheory import factorint  # sympy required "pip install sympy"


def is_probably_prime(number, number_of_loops=1):

    if number < 3 or not number % 2:
        return number == 2

    for _ in range(number_of_loops):

        a = randint(2, number - 1)

        if pow(a, number - 1, number) != 1:
            return False

        p_factors = factorint(number - 1)

        for q in p_factors:
            if pow(a, (number - 1)//q, number) == 1:
                break

        else:
            return True

    return False



