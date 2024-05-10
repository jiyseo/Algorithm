import sys

def solution(n, times):
    start = 1
    end = n * min(times)

    while start <= end : 
        mid = (start + end) // 2
        s = 0
        for t in times :
            s += mid//t
        if s >= n : end = mid - 1
        else : start = mid + 1
        # print("sum = ", s)
        # print("mid = ", mid)
        # print("start = ", start)
        # print("end = ", end)
        # print("----------------------")
    print(start)
    return start

# solution(10, [10, 15, 20, 25, 30])