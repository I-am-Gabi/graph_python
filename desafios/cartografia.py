# !/usr/bin/env python

nodes = int(raw_input())
adjacencyList = []

for i in range(0, nodes):
    adjacencyList.append([])

while nodes > 1:
    e = raw_input().split()
    u = int(e[0]) - 1
    v = int(e[1]) - 1
    adjacencyList[u].append(v)
    adjacencyList[v].append(u)
    nodes -= 1


def bfs(u, max_value):
    status = []
    distance = []

    for node in range(0, len(adjacencyList)):
        status.append(1)
        distance.append(-1)

    status[u] = 0
    distance[u] = 0
    queue = [u]
    return aux_bfs(queue, status, distance, max_value)


def aux_bfs(queue, status, distance, max_value):
    while queue:
        u = queue.pop()
        for v in adjacencyList[u]:
            if status[v] is 1:
                status[v] = 0
                distance[v] = distance[u] + 1
                if distance[v] > max_value:
                    max_value = distance[v]
                queue.append(v)
        status[u] = 2
    return max_value


m = bfs(0, 0)
m = bfs(m, m)
print m
