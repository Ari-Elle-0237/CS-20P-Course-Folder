"""
Assignment #4: Integer Sets
linked_list.py
by Ariel Zepezauer (arielzepezauer@gmail.com)
Pengo: 'azepezau'
Test Cases in unittest_linked_list.py
Repository at: https://github.com/Ari-Elle-0237/CS-20P-Course-Folder.git
Due: Dec 5th 2024
Exit Code _:
"""
import re

class linked_list: # PEP8 violation req'd by assignment spec
    class Node:
        """
        Nodes are simple objects with two attributes, a 1 character string that they store (data),
        and a link to the next node in the chain. Most of the code here is input sanitization
        """
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

    def __init__(self, initial:str=""):
        self.length = 0
        self.first = None
        for i in reversed(initial): # Reverse to preserve order correctly
            self.insert(i)

    def insert(self, item: str):
        """"Inserts item(s) at the beginning of the list using insert_at_index()"""
        self.insert_at_index(0, item)

    def append(self, item):
        """"Inserts item(s) at the end of the list using insert_at_index()"""
        self.insert_at_index(self.length, item)

    def insert_at_index(self, index: int, item: str):
        """"
        Inserts item(s) at a particular index
        Acts as infrastructure for splice(), insert(), and append(), and additionally handles input sanitization
        :param index: integer between 0 and self.length (inclusive)
        :param item: string input to be converted into linked list nodes
        :return: None
        """
        # Sanitize Inputs
        if not isinstance(item, str):
            raise TypeError("Tried to insert non-string into linked_list")
        if len(item) == 0:
            return

        # Assemble the item(s) to be inserted into a chain
        chain_to_insert = []
        for i in item:
            node = self.Node(i)
            if chain_to_insert:
                chain_to_insert[-1].link = node
            chain_to_insert.append(node)

        # Get the previous and next items in the list (if they exist) and save them
        if index - 1 >= 0:
            prev = self[index - 1]
        if index < len(self):
            nxt = self[index]
        elif index == self.length:
            nxt = None
        else:
            raise IndexError("Index out of range")

        # Then update the links (if possible)
        try:
            prev.link = chain_to_insert[0]
        except UnboundLocalError:
            # If we're at the beginning of the list, prev won't exist, so instead we update self.first
            self.first = chain_to_insert[0]
        # Try/Except is not necessary for nxt since we can just assign None to it.
        chain_to_insert[-1].link = nxt

        # Lastly, update length
        self.length += len(chain_to_insert)


    def remove_at_index(self, index, count):
        """
        Deletes nodes from the list by breaking their links
        :param index: index to begin from (inclusive)
        :param count: number of nodes to be deleted
        :return: None
        """
        if index == 0:
            self.first = self[index + count]
        elif index + count < self.length:
            self[index - 1].link = self[index + count]
        elif index + count == self.length:
            self[index - 1].link = None
        else:
            raise IndexError("Index out of range")
        self.length -= count

    def splice(self, find, replace):
        # Sanitize Inputs
        if len(find) == 0:
            return
        match = re.search(find, str(self)[3:])
        self.remove_at_index(match.start(0), len(find))
        self.insert_at_index(match.start(0), replace)



    def __getitem__(self, item: int):
        # idk if this is the right way to make this iterable but it seems to work
        current = self.first
        if item > self.length or item < 0: # TODO: Add support for negative indexing
            raise IndexError("Index out of range")
        for _ in range(item):
            if current.link is None:
                raise StopIteration
            current = current.link
        return current

    def __len__(self):
        return self.length

    def __str__(self):
        if len(self) == 0:
            return "(0)"
        return f"({self.length})" + "".join([f"{i.data}" for i in self])

def main():
    # test = linked_list("")
    # print(test)
    test = linked_list("2345")
    test.insert("1")
    test.append("6")
    # print(test[-1].data)
    test.insert_at_index(6, "ABC")
    # print(test[2].data)
    print(test)
    # test.remove_at_index(6, 3)
    # print(test)
    test.splice("ABC", "XYZ")
    print(test)

if __name__ == "__main__":
    main()
