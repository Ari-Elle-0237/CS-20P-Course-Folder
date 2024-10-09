"""
Assignment #4: Integer Sets
integer_set.py
by Ariel Zepezauer (arielzepezauer@gmail.com
Pengo: 'azepezau'
Test Cases in unittest_integer_set.py and program4.py
Repository at: https://github.com/Ari-Elle-0237/CS-20P-Course-Folder.git
Due: Oct 17th 2024
Exit Code 0: Passes all tests
"""


class integer_set:
    """
    Class for storing sets of integers equal to or between 0 and the constant SETUPPERLIMIT (1000 by default)
    (PEP8 violations in this Class are required by assignment spec)
    """
    SETUPPERLIMIT = 1000

    def __init__(self, initialElements=[]):  # List[int]
        self.elements = initialElements

    @property
    def elements(self):
        return self._elements

    @elements.setter
    def elements(self,value):
        self._elements = [False for _ in range(self.SETUPPERLIMIT + 1)]
        for element in value:
            self.insertElement(element)

    def get_elements(self):
        ret = []
        for i, v in enumerate(self.elements):
            if v:
                ret.append(i)
        return ret

    def getUpperLimit(self) -> int:
        return self.SETUPPERLIMIT

    def insertElement(self, e: int):
        if not self.check_range(e):
            return
        self.elements[e] = True

    def deleteElement(self, e: int):
        if not self.check_range(e):
            return
        self.elements[e] = False

    def hasElement(self, e: int) -> bool:
        if not self.check_range(e):
            return False
        return self.elements[e]

    def equals(self, other) -> bool:
        return self.elements == other.elements

    def check_range(self, value):
        if not isinstance(value, int):
            raise TypeError("Tried to put a non-integer into an integer set!")
        return 0 <= value <= self.SETUPPERLIMIT

    def __str__(self):
        elements = self.get_elements()
        ret = "{"
        for element in self.get_elements():
            if element != elements[-1]:
                ret += str(element) + ", "
            else:
                ret += str(element) + "}"
        return ret

    def intersectionOf(self, other1, other2):
        self._elements = [other1.elements[i] & other2.elements[i] for i in range(self.SETUPPERLIMIT + 1)]
        return self.elements

    def unionOf(self, other1, other2):
        self._elements = [other1.elements[i] | other2.elements[i] for i in range(self.SETUPPERLIMIT + 1)]
        return self.elements

class PositiveIntegerSetBytes(integer_set):
    """
    Class for storing sets of integers greater than or equal to 0
    """

    def __init__(self, initial_elements=None):
        super().__init__()
        self.bin = 0b0
        self.elements = initial_elements

    # <editor-fold: Properties>
    @property
    def elements(self):
        return self.get_one_bit_indices(self.bin)

    @elements.setter
    def elements(self,value):
        self.bin = 0b0
        if value is None:
            return
        for element in value:
            self.insert(element)

    @property
    def bin(self):
        return self._bin

    @bin.setter
    def bin(self, value):
        self._bin = value
    # </editor-fold: Properties>

    # <editor-fold: Methods>
    def insert(self, value: int):
        # Set the bit at the index provided by value
        if self.check_range(value):
            self.bin |= 0b1 << value

    def delete_element(self, value: int):
        # Clear the bit at the index provided by value
        if self.check_range(value):
            self.bin &= ~(0b1 << value)

    def has_element(self, value: int) -> bool:
        # Read the bit at the index provided by value
        # Rearranged from https://stackoverflow.com/questions/2576712/using-python-how-can-i-read-the-bits-in-a-byte
        if not self.check_range(value):
            return False
        return (self.bin & (0b1 << value)) != 0

    def equals(self, other) -> bool:
        if isinstance(other, PositiveIntegerSetBytes):
            return self.bin == other.bin
        return super().equals(other)

    def intersectionOf(self, other1, other2):
        self.bin = other1.bin & other2.bin
        return self.elements

    def unionOf(self, other1, other2):
        self.bin = other1.bin | other2.bin
        return self.elements
    # </editor-fold>

    # <editor-fold: Utilities>
    @staticmethod
    def get_one_bit_indices(value):
        # source: https://stackoverflow.com/questions/49592295/getting-the-position-of-1-bits-in-a-python-long-object
        one_bit_indexes = []
        index = 0
        while value:  # returns true if sum is non-zero
            if value & 1:  # returns true if right-most bit is 1
                one_bit_indexes.append(index)
            value >>= 1  # discard the right-most bit
            index += 1
        return one_bit_indexes

    def check_range(self,value):
        return value >= 0
    # </editor-fold>

    # <editor-fold: Backwards compatibility redirects>
    def get_elements(self):
        return self.elements

    def insertElement(self, e: int):
        self.insert(e)

    def deleteElement(self, e: int):
        self.delete_element(e)

    def hasElement(self, e: int) -> bool:
        return self.has_element(e)

    def getUpperLimit(self):
        self.get_upper_limit()
    # </editor-fold>

    # <editor-fold: Disabled Parent Methods>
    def get_upper_limit(self):
        raise AttributeError
    # </editor-fold>

class IntegerSetBytes(PositiveIntegerSetBytes):
    def __init__(self, initial_elements=None):
        self.min, self.max = None, None
        super().__init__(initial_elements)

    def update_min_max_lazy(self, value):
        if value > self.max or self.max is None:
            self.max = value
        if value < self.min or self.min is None:
            self.min = value

    def update_range(self, value):
        try:
            self.update_min_max_lazy(value)
        except AttributeError:
            for num in value:
                self.update_min_max_lazy(num)

    def translate_to_index(self, value):
        self.update_range(value)
        return (value - self.min)

    # <editor-fold: Properties>
    # @property
    # def range(self):
    #     return self.min, self.max
    #
    # @range.setter
    # def range(self, value):
    #     self.min, self.max = value

    @property
    def elements(self):
        return self.get_one_bit_indices(self.bin >> self.min)

    @elements.setter
    def elements(self,value):
        self.min, self.max = 0, 0
        # super().elements = value
        self.bin = 0b0
        if value is None:
            return
        for element in value:
            self.insert(element)
    # </editor-fold: Properties>

    def check_range(self,value):
        return True

    def insert(self, value):
        super().insert(self.translate_to_index(value))

def main():
    test_is = IntegerSetBytes([99,98])
    print(test_is.elements)
    print(f"{test_is.bin:b}")

if __name__ == "__main__":
    main()