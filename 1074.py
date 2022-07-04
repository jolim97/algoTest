import sys
n, r, c = map(int,sys.stdin.readline().split())
front = 0
while True:
    pos = -1
    if r < 2**(n-1) and c < 2**(n-1):
        pos = 0
    elif r < 2**(n-1) and c >= 2**(n-1):
        pos = 1
        c = c - 2**(n-1)
    elif r >= 2**(n-1) and c < 2**(n-1):
        pos = 2
        r = r - 2**(n-1)
    else:
        pos = 3
        r = r - 2**(n-1)
        c = c - 2**(n-1)
    front += pos * 2**(2*(n-1))
    n = n - 1
    if n <= 1: break
print(front + 2*r + c)
