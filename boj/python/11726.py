n = int(input())
# DP
l = [0,1,2]
if n < 3:
    print(l[n])
else:
    for i in range(3,n+1):
        l.append(l[i-2] + l[i-1])
    print(l[n]%10007)
