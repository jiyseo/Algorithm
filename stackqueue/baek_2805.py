import sys

def cuttree(need, tree) :
    start = 1
    end = max(tree)
    while start <= end :
        mid = (start + end) // 2
        s = 0
        for i in tree :
            if i > mid :
                s += i - mid
        if s >= need : start = mid + 1
        elif s < need : end = mid - 1
        print("sum = ", s)
        print("mid = ", mid)
        print("start = ", start)
        print("end = ", end)
        print("----------------------")
    print(end)

n, need = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

cuttree(need, tree)