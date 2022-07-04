import sys
input = sys.stdin.readline
n,m = map(int,input().split())

ns = {}
for _ in range(n):
    name = input().rstrip()
    ns[name] = 0

nm = []
for _ in range(m):
    name = input().rstrip()
    if name not in ns.keys():
        continue
    else:
        nm.append(name)
print(len(nm))
nm.sort()
for i in range(len(nm)):
    print(nm[i])
