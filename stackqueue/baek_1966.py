import sys

def printer(imp, k) :
    result = 1
    while imp :
        # print("imp = ", imp)
        # print(k)
        if imp[0] < max(imp) :
            imp.append(imp.pop(0))
        else :
            if k == 0 : break
            imp.pop(0)
            result += 1
        if k > 0 :  k = k - 1
        else : k = len(imp) - 1
    print(result)


if __name__ == '__main__' :
    testcase = int(sys.stdin.readline())
    for i in range(testcase) :
        imp = []
        n, k = map(int, sys.stdin.readline().split())
        imp = list(map(int,sys.stdin.readline().split()))
        printer(imp, k)