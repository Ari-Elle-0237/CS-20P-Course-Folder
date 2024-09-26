"""
Assignment #4:
______.py
by Ariel Zepezauer (arielzepezauer@gmail.com
Pengo: 'azepezau'
Test Cases in unittest_______.py
Repository at: https://github.com/Ari-Elle-0237/CS-20P-Course-Folder.git
Due: _______
Exit Code _:________
"""

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