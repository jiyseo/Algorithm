import sys

def dfs(graph, node, visited) :
    visited[node] = 1 
    print(node, end=' ')
    for i in range(1, n + 1) :
        if (graph[node][i] == 1 and visited[i] == 0) :
            dfs(graph, i, visited)

def bfs(graph, node, visited) :
    queue = [node]
    visited[node] = 1
    while queue:
        node = queue.pop(0)
        print(node, end = ' ')
        for i in range(1, n + 1) :
            if (visited[i] == 0 and graph[node][i] == 1) :
                queue.append(i)
                visited[i] = 1

n, m, node = map(int, sys.stdin.readline().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1

visited = [0] * (n + 1)
dfs(graph, node, visited)
print()
visited = [0] * (n + 1)
bfs(graph, node, visited)
