import ctypes


class DynamicArray():
    def __init__(self, capacity):
        self._length = 0
        self._capacity = capacity
        self._array = self._create_array(capacity)

    def __len__(self):
        return self._length

    def __getitem__(self, index):
        # return item in array[n]
        if index < 0 and index >= self._length:
            raise IndexError('Index out of bounds!')
        else:
            return self._array[index]

    def __str__(self) -> str:
        string = '['
        for i in range(self._length):
            if i == self._length - 1:
                string += f'{self._array[i]}'
            else:
                string += f'{self._array[i]}, '
        string += ']'
        return string

    def append(self, item):
        # insert item at the end of the array
        if self._capacity == self._length:
            self._resize()

        self._array[self._length] = item
        self._length += 1

    def _resize(self):
        # resize the array
        self._capacity *= 2
        new_array = self._create_array(self._capacity)

        for i in range(self._length):
            new_array[i] = self._array[i]

        self._array = new_array
        self._capacity = self._capacity

    def _create_array(self, capacity):
        return (capacity * ctypes.py_object)()


if __name__ == "__main__":
    array = DynamicArray(10)

    for i in range(11):
        array.append(i + 2)

    print(f'length: {len(array)}')
    print(f'capacity: {array._capacity}')
    print(array)
