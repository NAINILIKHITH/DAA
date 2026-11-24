
def bfs(graph, src):
    visited = []
    q = [src]

    while q:
        node = q.pop(0)

        if node not in visited:
            print(node, end=" ")
            visited.append(node)

            for i in graph[node]:
                if i not in visited:
                    q.append(i)


n = int(input("Enter number of vertices: "))
graph = {}

for i in range(n):
    graph[i] = list(map(int, input().split()))

src = int(input("Enter source: "))

print("BFS:")
bfs(graph, src)
