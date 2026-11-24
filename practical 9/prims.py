
def prims(graph, n):
    visited = [False] * n
    visited[0] = True
    total = 0

    print("Minimum Spanning Tree:")

    for i in range(n - 1):
        min_cost = float('inf')
        x = -1
        y = -1

        for j in range(n):
            if visited[j]:
                for k in range(n):
                    if not visited[k] and graph[j][k] != 0:
                        if graph[j][k] < min_cost:
                            min_cost = graph[j][k]
                            x = j
                            y = k

        if y == -1:
            print("MST not possible")
            return

        print(x, "-", y, ":", min_cost)
        total += min_cost
        visited[y] = True

    print("Minimum cost =", total)


n = int(input("Enter number of vertices: "))
print("Enter adjacency matrix:")

graph = []
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

prims(graph, n)
