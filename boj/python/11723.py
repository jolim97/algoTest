import sys
input = sys.stdin.readline
m = int(input())
s = set()
for _ in range(m):
    l = input().split()
    if l[0] == "all":
        s = set([ i+1 for i in range(0,20) ])
        continue
    if l[0] == "empty":
        s = set()
        continue
    if l[0] == "check":
        if int(l[1]) in s:
            print(1)
        else:
            print(0)
        continue
    if l[0] == "add":
        if int(l[1]) not in s:
            s.add(int(l[1]))
    elif l[0] == "remove":
        if int(l[1]) in s:
            s.remove(int(l[1]))
    elif l[0] == "toggle":
        if int(l[1]) in s:
            s.remove(int(l[1]))
        else:
            s.add(int(l[1]))
