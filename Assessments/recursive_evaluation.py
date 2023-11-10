def func_a(n):
    if n == 0:
        return 1

    else:
        return n * func_b(n=1)


def func_b(n):
    if n == 0:
        return 1

    else:
        return n * func_a(n=1)


func_a(4)
