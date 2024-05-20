n = int(input())
p = list(map(int, input().split()))

p.sort()
result = []
s = 0
for i in p :
    s += i
    result.append(s)

print(sum(result))