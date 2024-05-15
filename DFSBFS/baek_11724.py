import sys
sys.setrecursionlimit(10 ** 6)

N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M) :
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(i) :
    global visited
    visited[i] = True
    for node in graph[i] :
        if not visited[node] :
            dfs(node)

count = 0
for i in range(1, N + 1) :
    if not visited[i] :
        dfs(i)
        count += 1

print(count)