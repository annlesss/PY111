"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any


class PriorityQueue:
    def __init__(self):
        self.data = {}  # todo для очереди можно использовать python dict
        for i in range(11):
            self.data[i] = []

    def enqueue(self, elem: Any, priority: int = 0) -> None:
        """
        Operation that add element to the end of the queue

        :param elem: element to be added
        :return: Nothing
        """
        self.data[priority].append(elem)

        return None

    def dequeue(self) -> Any:
        """
        Return element from the beginning of the queue. Should return None if not elements.

        :return: dequeued element
        """
        self.data.pop(0)
        return None

    def peek(self, ind: int = 0, priority: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param ind: index of element (count from the beginning)
        :return: peeked element
        """
        return None

    def clear(self) -> None:
        """
        Clear my queue

        :return: None
        """
        self.data.clear()
        return None

if __name__ == "__main__":
    q = PriorityQueue()

    priority = 0
