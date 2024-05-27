import sys

n = int(input())
block = list(map(str, input()))
dp = [sys.maxsize] * n
dp[0] = 0

for i in range(n) :
    for j in range(i + 1, n) :
        if dp[i] == -1 :
            continue

        if block[i] == 'B' and block[j] == 'O' :
            dp[j] = min(dp[i] + (j - i) ** 2, dp[j])
        elif block[i] == 'O' and block[j] == 'J' :
            dp[j] = min(dp[i] + (j - i) ** 2, dp[j])
        elif block[i] == 'J' and block[j] == 'B' :
            dp[j] = min(dp[i] + (j - i) ** 2, dp[j])

if dp[n - 1] == sys.maxsize :
    print(-1)
else :
    print(dp[n - 1])