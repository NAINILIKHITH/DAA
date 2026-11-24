
def dfs(graph, src, visited):
    print(src, end=" ")
    visited.append(src)

    for i in graph[src]:
        if i not in visited:
            dfs(graph, i, visited)


n = int(input("Enter number of vertices: "))
graph = {}

for i in range(n):
    graph[i] = list(map(int, input().split()))

src = int(input("Enter source: "))

print("DFS:")
dfs(graph, src, [])
