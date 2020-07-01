def simple(n):
    i = 2
    k = 0
    while i ** 2 <= n and k != 1:
        if n % i == 0:
            k = 1
        i += 1
    return k != 1


def divisor(n):
    list_divisor = []
    i = 1
    while i <= n:
        if n % i == 0:
            list_divisor.append(i)
        i += 1
    return list_divisor


def simple_divisor(n):
    list_simple_div = [1]
    x = 1
    while x <= n:
        list_divisor = [i for i in range(1, x + 1) if x % i == 0 and n % x == 0]
        if len(list_divisor) == 2:
            list_simple_div.append(x)
        x += 1
    return list_simple_div


def max_simple_div(n):
    list_simple_div = [1]
    x = 1
    while x < n:
        list_divisor = [i for i in range(1, x + 1) if x % i == 0 and n % x == 0]
        if len(list_divisor) == 2:
            list_simple_div.append(x)
        x += 1
    return max(list_simple_div)


def canonical_decomposition(n):
    list_factors = []
    x = 1
    while n != 1:
        list_divisor = [i for i in range(1, x + 1) if x % i == 0 and n % x == 0]
        if len(list_divisor) == 2:
            list_factors.append(x)
            n = n / x
            x = 0
        x += 1
    return list_factors


def max_div(n):
    x = 1
    while x < n:
        if n % x == 0:
            maximum = x
        x += 1
    return maximum