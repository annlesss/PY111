from typing import Hashable, List
import networkx as nx
from Tasks.a0_my_stack import Stack
from queue import LifoQueue as Stack

def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an depth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node of search
    :return: list of nodes in the visited order
    """
    print(g, start_node)

    s = Stack()
    node = start_node
    path = []
    # пробегаемся по глубине
    while s.data:
        if node not in path:
            path.append(node)
            for neig in g.neighbors(node):
                if neig not in path and neig not in s.data:
                    s.push(neig)
        node = s.pop()
        # if node is None:
        #     return path

if __name__ == "__main__":
    s = Stack()
    print(1)

