def simple_recursion(n):
    if n < 1:
        print(f"{n} is less than 1")
    else:
        simple_recursion(n - 1)
        print(n)


def power_of_two(n):
    if n == 0:
        return 1
    return (2 * power_of_two(n - 1))


def fib(n):
    assert n >= 0, "only positive numbers"
    if n in [0, 1]:
        return n
    return fib(n - 1) + fib(n - 2)


def factorial(n):
    assert n >= 0, "only positive numbers"
    if n in [0, 1]:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    n = 5
    print(fib(8))
