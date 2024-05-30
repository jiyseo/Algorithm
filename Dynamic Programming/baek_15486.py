import sys
n = int(input())

due = []
money = []
for _ in range(n) :
    d, m = map(int, sys.stdin.readline().split())
    due.append(d)
    money.append(m)

dp = [0 for _ in range(n)]

for i in range(n) :
    dp[i] = max(dp[i], dp[i - 1])
    cur = due[i] + i - 1
    # print("=================")
    if cur < n :
        # print("due[i] = ", due[i], "money[i] = ", money[i])
        # print("cur = ", cur, "dp[cur] = ", dp[cur])
        dp[cur] = max(dp[cur], dp[i - 1] + money[i])
    # print(dp)
print(dp[n - 1])

