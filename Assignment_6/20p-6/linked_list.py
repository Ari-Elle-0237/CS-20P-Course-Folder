"""
Assignment #4: Integer Sets
linked_list.py
by Ariel Zepezauer (arielzepezauer@gmail.com
Pengo: 'azepezau'
Test Cases in unittest_linked_list.py
Repository at: https://github.com/Ari-Elle-0237/CS-20P-Course-Folder.git
Due: Dec 5th 2024
Exit Code _:
"""

class linked_list: # PEP8 violation req'd by assignment spec
    class Node:
        def __init__(self, data=None, link=None):
            self.link = link
            self.data = data

        @property
        def data(self):
            return self._data

        @data.setter
        def data(self, new):
            if not isinstance(new, str):
                raise TypeError("Tried to insert non-string into a node")
            if len(new) > 1:
                raise TypeError("Tried to place more than one character into a node")
            self._data = new

        def __str__(self):
            return f"(Node: {self.data} | -> {self.link})"

    def __init__(self, initial:""):
        self.length = 0
        self.first = None
        for i in reversed(initial):
            self.insert(i)

    def insert(self, item: str):
        if not isinstance(item, str):
            raise TypeError("Tried to insert non-string into linked_list")
        if len(item) == 0:
            return
        for i in reversed(item):
            node = self.Node(i)
            node.link = self.first
            self.first = node
            self.length += 1

    def splice(self, find, replace):
        pass

    def __getitem__(self, item: int):
        current = self.first
        if item > self.length:
            raise IndexError("Index out of range")
        for _ in range(item):
            if not current.link:
                raise StopIteration
            current = current.link
        return current

    def __len__(self):
        return self.length

    def __str__(self):
        return f"({self.length})" + "".join([f"{i.data}" for i in self])

def main():
    test = linked_list("")
    # print(test)
    print(test)


if __name__ == "__main__":
    main()
