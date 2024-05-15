import sys
sys.setrecursionlimit(10 ** 6) 

T = int(input())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y) :
    global Map
    if x < 0 or y < 0 or x >= N or y >= M :
        return
    if Map[x][y] == 1 :
        Map[x][y] = 0
        for i in range(4) :
            xx = x + dx[i]
            yy = y + dy[i]
            dfs(xx, yy)

for t in range(T) :
    N, M, K = map(int, input().split())
    Map = [[0 for _ in range(M)] for _ in range(N)]
    count = 0
    for k in range(K) :
        x, y = map(int, input().split())
        Map[x][y] = 1
    for i in range(N) :
        for j in range(M) :
            if Map[i][j] == 1 :
                dfs(i, j)
                count += 1
    print(count)