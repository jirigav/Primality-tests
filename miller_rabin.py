from random import randint


def prime_test(n, loops):
    if n < 3:
        return n == 2

    d = n - 1
    s = 0
    while not d % 2:
        s += 1
        d //= 2
    for i in range(loops):
        a = randint(2, n- 1)
        x = pow(a, d, n)

        if x == 1 or x == (n - 1):
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == 1:
                return False
            if x == (n - 1):
                break
        else:
            return False

    return True
