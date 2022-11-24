def multiply(m, n):
    """
    >>> multiply(5,3)
    15
    >>> multiply(6,3)
    18
    >>> multiply(5,4)
    20
    """
    if n == 0:
        return 0
    else:
        return m + multiply(m, n - 1)


print(multiply(5, 4))


def is_prime(n):
    """
    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False
    """

    def prime_helper(b=2):
        if n <= 2:
            return False
        elif n == b:
            return True
        elif n % b == 0:
            return False

        else:
            return prime_helper(b + 1)

    if prime_helper(b=2):
        return True
    else:
        return False


def make_func_repeater(f, x):
    def repeat(f, x):
        if x == 1:
            return f(x)
        else:
            return f(repeat(f, x - 1))

    return repeat


def count_stair_ways(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return count_stair_ways(n - 1) + count_stair_ways(n - 2)


def count_k(n, k):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return count_k(n - 1, k) + count_k(n - 1, k - 1)
