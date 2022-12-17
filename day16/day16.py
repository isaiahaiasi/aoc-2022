import sys
import re
import heapq
from collections import deque
from pprint import pprint
import functools


class Node:
    def __init__(self, key: str, flow: int, neighbors: list[str]):
        self.key = key
        self.flow = flow
        self.adj = neighbors


class Graph:
    def __init__(self, nodes: dict[str, Node]):
        self.graph = nodes
        # pre-sort might be more efficient?...
        self.distances = {n: self.distances_from(n) for n in
                          self.graph.keys() if self.graph[n].flow > 0}
        self.flows = {k: v.flow for k,
                      v in self.graph.items() if self.graph[k].flow > 0}

    def distances_from(self, start: str):
        distances = {start: 0}
        q = deque([start])
        while q:
            r = q.popleft()
            for n in self.graph[r].adj:
                if n not in distances:
                    q.append(n)
                    distances[n] = distances[r] + 1
        del distances[start]
        return {k: v for k, v in distances.items() if self.graph[k].flow > 0}

    def best_single_runner(self):
        # initialize priority queue
        # heuristic must be negative bc heapq ONLY provides min-heap
        pq = []
        for n in self.flows.keys():
            dist = self.distances_from('AA')[n]
            t = 30 - dist - 1
            pq.append((-self.flows[n] * t, n, t))
        heapq.heapify(pq)

        opened = set()
        best = 0

        while pq:
            heur, rkey, t = heapq.heappop(pq)
            opened.add(rkey)
            for nkey, ndist in self.distances[rkey].items():
                if nkey in opened or t < ndist + 1:
                    continue
                nt = t - ndist - 1
                nheur = heur - self.flows[nkey] * nt
                best = max(best, -nheur)
                heapq.heappush(pq, (nheur, nkey, nt))
        return best

    @functools.lru_cache(maxsize=None)
    def best_naive(self, n, time, opened=()):
        if time <= 0:
            return 0
        best = 0
        valve_val = (time - 1) * n.flow
        next_open = tuple(sorted(opened + (n.key,)))
        for a_key in n.adj:
            a_node = self.graph[a_key]
            if n.key not in opened and valve_val:
                best = max(best, valve_val +
                           self.best_naive(a_node, time - 2, next_open))
            best = max(best, self.best_naive(a_node, time - 1, opened))
        return best


def get_max_pressure(graph: Graph):
    return graph.best_naive(graph.graph["AA"], 30)  # 2110 TOO HIGH


def load_graph_from_input(path):
    with open(path, "r") as fp:
        adjacency_graph = {}
        for line in fp:
            n, *adj = re.findall('[A-Z]{2}', line)
            flow = int(re.findall('\d+', line)[0])
            adjacency_graph[n] = Node(n, flow, adj)
        return Graph(adjacency_graph)


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else './day16/test-input.txt'
    graph = load_graph_from_input(path)

    pprint(graph.best_single_runner())


if __name__ == "__main__":
    main()
