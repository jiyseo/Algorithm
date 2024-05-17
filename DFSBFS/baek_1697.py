n, k = map(int, input().split())
time = [0] * (100000 +1)

def bfs():
    queue = []
    queue.append(n)
    while queue:
        x = queue.pop(0)
        if x == k:
            print(time[x])
            break
        for dx in [x - 1, x + 1, x * 2] :
            if 0 <= dx <= 100000 and time[dx] == 0:
                time[dx] = time[x] + 1
                queue.append(dx)

bfs()
