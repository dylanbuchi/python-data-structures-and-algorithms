#Question 1:
# How to find the sum of digits of a positive integer number using recursion
def sum_digits(n):
    assert n >= 0, "only positive numbers"
    if n == 0:
        return n
    return n % 10 + sum_digits(n // 10)


#Question 2:
# How to calculate power of a number using recursion
def power(base, exp):
    assert exp >= 0, "only positive numbers"
    if exp == 0:
        return 1
    return base * power(base, exp - 1)


if __name__ == "__main__":
    print(power(24, 1))
