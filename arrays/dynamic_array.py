import ctypes


class DynamicArray():
    def __init__(self, capacity):
        self.length = 0
        self.capacity = capacity
        self.array = self._create_array(capacity)

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        # return item in array[n]
        if index < 0 and index >= self.length:
            raise IndexError('Index out of bounds!')
        else:
            return self.array[index]

    def __str__(self) -> str:
        string = '['
        for i in range(self.length):
            if i == self.length - 1:
                string += f'{self.array[i]}'
            else:
                string += f'{self.array[i]}, '
        string += ']'
        return string

    def append(self, item):
        # insert item at the end of the array
        if self.capacity == self.length:
            self.array = self._resize()

        self.array[self.length] = item
        self.length += 1

    def _resize(self):
        # resize the array
        self.capacity *= 2
        new_array = self._create_array(self.capacity)

        for i in range(self.length):
            new_array[i] = self.array[i]

        self.array = new_array

    def _create_array(self, capacity):
        return (capacity * ctypes.py_object)()


if __name__ == "__main__":
    array = DynamicArray(10)

    array.append(2)
    array.append(3)
    array.append(4)
    array.append(5)

    print(len(array))
    print(array.capacity)
    print(array)
