import sys

def CUTLAN(n, lan) :
    start = 1
    end = max(lan)

    while start <= end :
        mid = (start + end) // 2
        sum = 0
        print("sum = ", sum)
        print("start = ", start)
        print("mid = ", mid)
        print("end = ", end)
        for l in lan :
            sum += l // mid
        if sum >= n : start = mid + 1
        else : end = mid - 1
    return end

if __name__ == '__main__' :
    k, n = map(int, sys.stdin.readline().split())
    lan = []
    for i in range(k) :
        lan.append(int(sys.stdin.readline()))
    print(CUTLAN(n, lan))