if __name__ == "__main__":
    # O(1) constant time
    array = [10, 20, 30, 40, 50, 60]
    print(f"first element: {array[0]}")

    # O(n) linear time
    for index, number in enumerate(array):
        print(f"index: {index} value: {number}")

    # O(logn) Logarithmic time
    for i in range(0, len(array), 3):
        print(f"index: {i} value: {array[i]}")

    # O(n2) quadratic time
    for i in array:
        for j in array:
            print(i, j)

    # O(2n) exponentialE time, aka the worst
    # ex: fibonacci with recursion
