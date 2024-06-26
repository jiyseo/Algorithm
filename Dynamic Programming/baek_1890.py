n = int(input())
game = []
for _ in range(n) :
    g = list(map(int, input().split()))
    game.append(g)
dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = 1

for i in range(n) :
    for j in range(n) :
        if dp[i][j] >= 1 :
            jump = game[i][j]
            if jump == 0 :
                break
            if i + jump < n :
                dp[i + jump][j] += dp[i][j]
            if j + jump < n :
                dp[i][j + jump] += dp[i][j]

print(dp[n-1][n-1])
