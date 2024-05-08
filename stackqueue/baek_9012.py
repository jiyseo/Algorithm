import sys

def bracket(bracstr) :
    answer = []
    for brac in bracstr :
        stack = []
        for b in brac :
            if b == "(" :
                stack.append(b)
            elif b == ")" :
                if len(stack) != 0 :
                    stack.pop(-1)
                else :
                    stack.append("(")
                    break
        if len(stack) == 0 :
            answer.append("YES")
        else : answer.append("NO")
    for a in answer :
        print(a)

n = int(sys.stdin.readline())
bracstr = []
for i in range(n) :
    bracstr.append(sys.stdin.readline())
bracket(bracstr)

