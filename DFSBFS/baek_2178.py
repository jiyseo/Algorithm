N, M = map(int, input().split())
Map = []
for _ in range(N) :
    Map.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y) :
    queue = []
    queue.append((x, y))

    while queue :
        x, y = queue.pop(0)
        for i in range(4) :
            xx = x + dx[i]
            yy = y + dy[i]

            if 0 <= xx < N and 0 <= yy < M and Map[xx][yy] == 1 :
                queue.append((xx, yy))
                Map[xx][yy] = Map[x][y] + 1

    return Map[N - 1][M - 1]

print(bfs(0, 0))