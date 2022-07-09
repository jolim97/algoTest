import sys
input = sys.stdin.readline
n = int(input())
meetings = [ [0,0] for _ in range(n) ]
for i in range(n):
    a,b = map(int,input().split())
    meetings[i] = [a,b]
meetings.sort(key = lambda x: (x[1], x[0]))
count = previous_end = 0
for start,end in meetings:
    if start >= previous_end:
        count += 1
        previous_end = end
print(count)
