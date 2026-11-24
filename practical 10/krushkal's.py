
def kruskal(edges, n):
    parent = list(range(n))
    total = 0

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    edges.sort(key=lambda x: x[2])

    print("Minimum Spanning Tree:")

    for u, v, w in edges:
        pu = find(u)
        pv = find(v)

        if pu != pv:
            print(u, "-", v, ":", w)
            total += w
            parent[pu] = pv

    print("Minimum cost =", total)


n = int(input("Enter number of vertices: "))
m = int(input("Enter number of edges: "))

edges = []

for i in range(m):
    u, v, w = map(int, input("Enter edge (u v weight): ").split())
    edges.append((u, v, w))

kruskal(edges, n)
