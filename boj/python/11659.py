import sys
input = sys.stdin.readline
n,m = map(int,input().split())
numbers = list(map(int,input().split()))
sumlists = [0] * (n+1)
for i in range(1,n+1):
    sumlists[i] = sumlists[i-1] + numbers[i-1]

for _ in range(m):
    i,j = map(int,input().split())
    if i == j:
        print(numbers[i-1])
    else:
        print(sumlists[j]-sumlists[i-1])
