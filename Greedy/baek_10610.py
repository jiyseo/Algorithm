num = list(map(int, input()))

if sum(num) % 3 != 0 or 0 not in num :
    print(-1)

else : 
    num.sort(reverse=True)
    mul = 0
    for i in num :
        mul += int(i)
        mul *= 10
    print(mul//10)
