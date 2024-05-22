n, k = map(int, input().split())
coin = []
for _ in range(n) :
    coin.append(int(input()))

coin.sort(reverse=True)

count = 0
for i in coin :
    if i > k :
        continue
    else :
        count += k // i
        k = k % i
print(count)