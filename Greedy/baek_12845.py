n = int(input())
card = list(map(int, input().split()))

print(max(card) * (len(card) - 2) + sum(card))