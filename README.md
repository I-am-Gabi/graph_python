# graph_python

# !/usr/bin/env python

nodes = int(raw_input())
adjacencyList = []
vis = [0] * nodes
fila = [0] * nodes
dist = [0] * nodes
deg = [0] * nodes

for i in range(0, nodes):
    adjacencyList.append([])

while nodes > 1:
    e = raw_input().split()
    u = int(e[0]) - 1
    v = int(e[1]) - 1
    adjacencyList[u].append(v)
    deg[u] += 1
    adjacencyList[v].append(u)
    deg[v] += 1
    nodes -= 1


def bfs(s, adjacencyList):
    l = 0
    r = 0
    vis[s] = 1
    fila[r] = s
    r += 1
    dist[s] = 0
    maior = s
    while (l < r):
        v = fila[l]
        l += 1
        for i in range(0, deg[v]):
            nxt = adjacencyList[v][i]
            if not vis[nxt]:
                vis[nxt] = 1
                fila[r] = nxt
                r += 1
                dist[nxt] = dist[v] + 1
                if (dist[nxt] > dist[maior]): maior = nxt

    return maior


m = bfs(0, adjacencyList)
m = bfs(m, adjacencyList)
print m
