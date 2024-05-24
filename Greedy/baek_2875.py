n, m, k = map(int, input().split())

k -= n % 2
n = n // 2

if n >= m :
    team = m
    k -= (n - m) * 2
else :
    team = n
    k -= m - n

while k > 0 :
    k -= 3
    team -= 1

print(team)