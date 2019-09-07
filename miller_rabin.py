from random import randint


def is_probably_prime(number, loops):
    if number < 4:
        return number == 2 or number == 3

    d = number - 1
    s = 0
    while not d % 2:
        s += 1
        d //= 2
    for i in range(loops):
        a = randint(2, number - 2)
        x = pow(a, d, number)

        if x == 1 or x == (number - 1):
            continue
        for _ in range(s - 1):
            x = pow(x, 2, number)
            if x == (number - 1):
                break
        else:
            return False

    return True
