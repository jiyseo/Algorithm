import sys

n = int(input())
meet = []
for _ in range(n) :
    meet.append(list(map(int, sys.stdin.readline().split())))

meet.sort(key = lambda x : (x[1], x[0]))
end = 0
count = 0

for m in meet :
    if m[0] >= end :
        end = m[1]
        count += 1

print(count)
