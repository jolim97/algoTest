import sys
input = sys.stdin.readline
n = int(input())
numbers = list(map(int,input().split()))
numbers = set(numbers)
m = int(input())
result = []
for i in list(map(int,input().split())):
    if i in numbers:
        result.append(1)
    else:
        result.append(0)
print(*result)

