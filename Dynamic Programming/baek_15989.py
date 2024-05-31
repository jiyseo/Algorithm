n = int(input())
dp = [1 for i in range(10001)]
num = [int(input()) for _ in range(n)]

for i in range(2, 10001):
    dp[i] += dp[i - 2]
for i in range(3, 10001):
    dp[i] += dp[i - 3]
for i in num:
    print(dp[i])