from typing import Hashable, List
import networkx as nx
from Tasks.a1_my_queue import Queue


def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an breadth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node for search
    :return: list of nodes in the visited order
    """
    print(g, start_node)
    q = Queue()
    node = start_node
    path = []
    # пробегаемся по ширине
    while True:
        if node not in path:
            path.append(node)
            for neig in g.neighbors(node):
                if neig not in path and neig not in q.data:
                    g.enqueue(neig)
        node = q.dequeue()
        if node is None:
            return path



