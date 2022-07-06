t = int(input())
# DP
l = [0] * 101
l[1] = l[2] = l[3] = 1
l[4] = l[5] = 2
for i in range(6,101):
    l[i] = l[i-5] + l[i-1]
for _ in range(t):
    print(l[int(input())])
