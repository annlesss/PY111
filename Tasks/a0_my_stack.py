"""
My little Stack
"""
from typing import Any


class Stack:
    def __init__(self):
        self.data = []  # todo для стека можно использовать python list
        self.ind = 0

    def push(self, elem: Any) -> None:
        """
        Operation that add element to stack

        :param elem: element to be pushed
        :return: Nothing
        """
        self.data.append(elem)
        self.ind += 1

        print(elem)
        return None

    def pop(self) -> Any:
        """
        Pop element from the top of the stack. If not elements - should return None.

        :return: popped element
        """
        try:
            self.data.pop(self.ind)
            dat = self.data[self.ind]
            self.ind -= 1
            return dat
        except:
            return None



    def peek(self, ind: int = 0) -> Any:
        """
        Allow you to see at the element in the stack without popping it.

        :param ind: index of element (count from the top, 0 - top, 1 - first from top, etc.)
        :return: peeked element or None if no element in this place
        """
        print(self.data[ind])
        print(ind)

        return None

    def clear(self) -> None:
        """
        Clear my stack

        :return: None
        """
        self.data.clear()

        return None

if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)

    print(s.data)
    s.pop()
    print(s.data.pop())



