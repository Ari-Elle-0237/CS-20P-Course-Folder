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

class SomeClass:
    SOME_CONSTANT = 2
    some_class_var = 0
    def __init__(self):
        self._somevar = None

    @property
    def somevar(self):
        return self._somevar

    @somevar.setter
    def somevar(self, value):
        self._somevar = value

    def some_method(self, some_arg):
        self.somevar = some_arg * self.SOME_CONSTANT

    @staticmethod
    def some_static(self):
        return 2

    @classmethod
    def some_class_method(cls, some_arg):
        cls.some_class_var = some_arg * cls.SOME_CONSTANT

def main():
    pass

if __name__ == "__main__":
    main()