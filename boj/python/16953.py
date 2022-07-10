a,b = map(int,input().split())
cnt = 1
while True:
    if a == b:
        break
    elif (b % 10) in [2,4,6,8,0]:
        b /= 2
        cnt += 1
    elif ((b % 10) == 1) and b > 10:
        b //= 10
        cnt += 1
    else:
        cnt = -1
        break
print(cnt)
