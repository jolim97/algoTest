import sys
input = sys.stdin.readline

# DP
l = [0] * 11
l[1] = 1 # 1
l[2] = 2 # 1+1, 2
l[3] = 4 # 1+1+1, 2+1, 1+2, 3

for i in range(4,11):
    l[i] = sum(l[i-3:i])

for _ in range(int(input())):
    print(l[int(input())])
