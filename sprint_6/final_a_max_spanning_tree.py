"""
-- ПРИНЦИП РАБОТЫ --
    Задача в явном виде сводится к классическому поиску максимального остовного
    дерева. Воспользуемся алгоритмом Прима из теории практикума.

    - обход вершин можно начать с любого места графа. В случае обнаруженмя
    несвязности, мы закончим работу и выведем сообщение с ошибкой.
    - в ходе работы алгоритма мы на каждом шаге извлекаем из приоритетной
    очереди ребро с максимальным весом, помечаем его просмотренным (удаляем из 
    множества not_seen) и суммируем веса таких ребер, получая искомое
    значение.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
    O(N * logN + M * logN) = O((N + M) * logM), где:

    O(N * logN) - необходимость обойти каждую вершину, извлекая ее из множества
    на каждом проходе.
    O(M * logN) - просмотр каждого исходящего из рассматриваемой вершины ребра 
    и запись его в кучу (в самой куче содержится не более чем N ребер, так как
    мы добавляем ребра только для "новых", ранее не встречавшихся вершин.

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
    O(N * N) - хранение списков смежности плотного графа.
"""
import heapq


class MaxHeap:
    def __init__(self):
        self.data = []

    def push(self, triplet):
        from_idx, to_idx, weight = triplet
        heapq.heappush(self.data, (-weight, from_idx, to_idx))

    def pop(self):
        weight, from_idx, to_idx = heapq.heappop(self.data)
        return (from_idx, to_idx, -weight)

    def __len__(self):
        return len(self.data)


ERROR_MSG = "Oops! I did it again"


class GraphIsNotConnectedException(Exception):
    pass


def get_max_spanning_tree_weight(graph):
    mst_weight = 0
    not_seen = set(range(1, len(graph)))
    edges_heap = MaxHeap()

    def get_max_edge():
        return edges_heap.pop()

    def add_vertex(vertex_idx):
        not_seen.remove(vertex_idx)
        for i, weight in graph[vertex_idx]:
            if i in not_seen:
                # add triplet ("from, to, weight") to max-heap
                edges_heap.push((vertex_idx, i, weight))

    add_vertex(1)  # we could start from any vertex

    while not_seen and edges_heap:
        _, to_idx, weight = get_max_edge()

        if to_idx in not_seen:
            mst_weight += weight
            add_vertex(to_idx)

    if not_seen:
        raise GraphIsNotConnectedException()
    return mst_weight


def build_graph(n, m):
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))

    return graph


def main():
    n, m = map(int, input().split())

    graph = build_graph(n, m)
    try:
        print(get_max_spanning_tree_weight(graph))
    except GraphIsNotConnectedException as _:
        print(ERROR_MSG)


if __name__ == "__main__":
    main()
