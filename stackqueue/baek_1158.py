import sys

def print_ans(num) :
    print("<", end="")
    for n in num :
        print(n, end="")
        if n != num[-1] :
            print(", ", end="")
    print(">")

def Josephus_prob(n, k) :
    josephus = [i for i in range(1, n + 1)]
    answer = []
    idx = k
    for i in range(n) :
        length = len(josephus)
        while idx >= length :
            idx -= len(josephus)
        answer.append(josephus[idx])
        josephus.pop(idx)
        idx += k
    print_ans(answer)

n, k = map(int, sys.stdin.readline().split())
Josephus_prob(n, k - 1)