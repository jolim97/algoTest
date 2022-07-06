import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    wears = {}
    for _ in range(n):
        clothes,kinds = map(str,input().split())
        if not kinds in wears.keys():
            wears[kinds] = []
        wears[kinds].append(clothes)
    ans = 1
    for i in wears.values():
        ans *= len(i) + 1
    print(ans-1)
