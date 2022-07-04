import sys
from math import inf
n,m,b = map(int, sys.stdin.readline().split())
blocks = []
for _ in range(n):
    tmp = map(int,sys.stdin.readline().split())
    blocks += tmp

time = inf
height = 0
for i in range(257):
    n_plus = 0
    n_minus = 0
    for j in blocks:
        if j > i:
            n_plus += j-i
        else:
            n_minus += i-j
    if n_plus + b < n_minus:
        continue

    tmptime = n_plus * 2 + n_minus
    if tmptime <= time:
        time = tmptime
        height = i
    else:
        break

print(time,height)
