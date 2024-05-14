
N = int(input())
Map = []
for i in range(N) :
    Map.append(list(map(int, input())))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(x, y) :
    global count
    if x < 0 or y < 0 or x >= N or y >= N :
        return
    # print("=============MAP=============")
    # for i in Map :
    #     print(i)
    # print("=============================")
    if Map[x][y] == 1:
        Map[x][y] = 0
        count += 1
        for i in range(4) :
            xx = x + dx[i]
            yy = y + dy[i]
            dfs(xx, yy)

result = []
count = 0
for i in range(N) :
    for j in range(N) :
        if Map[i][j] == 1 :
            dfs(i, j)
            result.append(count)
            # print("count = ", count)
            count = 0
result.sort()
print(len(result))
for i in result :
    print(i)