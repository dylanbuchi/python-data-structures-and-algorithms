# find runtimes of the functions below:


def foo(array):
    #total runtime is linear:O(N)
    total = 0  # O(1)
    product = 1  # O(1)

    for i in array:  # O(N)
        total += i  # O(1)
    for i in array:  # O(N)
        product *= i  # O(1)

    print(f"Sum: {total}, Product: {product} \nand the run time is linear O(n)"
          )  # O(1)


def print_pairs(array):
    #total runtime is quadratic : O(N2)
    for i in array:  # O(N2)
        for j in array:  # O(N)
            print(f"{i}, {j}")  # O(1)
    print("Run time is quadratic O(n2)")


def print_unordered_pairs(array):
    #total runtime is quadratic: O(N2)
    for i in range(0, len(array)):  # O(N2)
        for j in range(i + 1, len(array)):  # O(N)
            print(f"{array[i]}, {array[j]}")  # O(1)
    print("Run time is quadratic O(n2)")


if __name__ == "__main__":

    array = [1, 2, 3, 4, 5]
    foo(array)
    print_pairs(array)
    print_unordered_pairs(array)
