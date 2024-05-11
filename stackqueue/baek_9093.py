import sys

def reversestr(str) :
    word = str.split()

    for w in word :
        print(w[::-1], end = " ")
    print()

if __name__ == '__main__' :
    n = int(input())
    for i in range(n) :
        str = sys.stdin.readline()
        reversestr(str)