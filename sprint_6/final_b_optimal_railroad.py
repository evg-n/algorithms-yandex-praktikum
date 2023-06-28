"""
-- ПРИНЦИП РАБОТЫ --
    Важно заметить, что задачу можно переформулировать в классический поиск
    циклов в ориентированном графе. Один из двух типов дорог можно обозначить
    за обратное направление. Таким образом, при существовании цикла в таком
    графе железная дорога будет неоптимальной, так как будет хотя бы один город
    в который можно будет добраться по дорогам обоих типов.

    Само решение с поиском цикла в ориентированном графе - тривиально
    с использованием DFS с массивом цветов из курса. Заметим, даже
    учитывая что в задаче описан связный граф, мы все равно должны проверить
    все его вершины из-за ориентированности.

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
    Наличие цикла в графе означает, что данная конфигурация железной дороги
    - неоптимальна, тк любой цикл для нашей задачи означает что в город можно
    добраться как прямым маршрутом, так и по "обратным ребрам" (другой тип
    дорожного полотна).

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
    O(N + E) ~ O(N * N),
    в худшем случае требуется обойти каждую вершину и каждое ребро. При этом 
    стоит заметить, что граф достаточно плотный. Число ребер - N*(N-1)/2,
    поэтому сложность можно также обозначить через O(N * N).

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
    O(N * N) - хранение плотного ориентированного графа в виде списков
    смежности.
"""


def has_cycles(graph):
    colors = ["white"] * len(graph)

    # standart dfs with colors
    def iterative_dfs(start_node):
        stack = [start_node]

        while stack:
            current_node = stack.pop()
            if colors[current_node] == "white":
                colors[current_node] = "gray"
                stack.append(current_node)

                for i in graph[current_node]:
                    if colors[i] == "gray":
                        return True
                    elif colors[i] == "white":
                        stack.append(i)

            elif colors[current_node] == "gray":
                colors[current_node] = "black"
        return False

    # we need to check all graph vertices
    for i, _ in enumerate(graph):
        if colors[i] == "white":
            if iterative_dfs(i):
                return True
    return False


def build_graph(n):
    graph = [[] for _ in range(n)]

    for i in range(n - 1):
        # connections for i-th vertex
        roads_info = input()
        for j, road in enumerate(roads_info, start=1):
            if road == "R":
                graph[i].append(i + j)
            else:
                graph[i + j].append(i)

    return graph


def main():
    n = int(input())
    graph = build_graph(n)
    print("NO" if has_cycles(graph) else "YES")


if __name__ == "__main__":
    main()
