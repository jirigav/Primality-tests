
def jacobi(n, k):
    """
    Jacobi symbol

    :param n: number n > 0
    :param k: number k > 0, k % 2 == 1
    :return: Jacobi symbol -1, 0 or 1
    """
    assert (k % 2 == 1 and 0 < k)

    n = n % k
    t = 1

    while n != 0:

        while n % 2 == 0:
            n /= 2
            r = k % 8
            if r == 3 or r == 5:
                t = -t

        n, k = k, n
        if n % 4 == k % 4 == 3:
            t = -t
        n = n % k

    if k == 1:
        return t
    else:
        return 0
