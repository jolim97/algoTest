import sys
from collections import deque

def bfs(graph,start):
    num = [0] * (n+1)
    visited = [start]
    queue = deque()
    queue.append(start)
    while queue:
        v = queue.popleft()
        for w in range(n+1):
            if (graph[v][w] == 1) and (w not in visited):
                num[w] = num[v] + 1
                visited.append(w)
                queue.append(w)
    return sum(num)

input = sys.stdin.readline
n,m = map(int,input().split())
graph = [ [0]*(n+1) for _ in range(n+1) ]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1
result = []
for i in range(1,n+1):
    result.append(bfs(graph, i))
print(result.index(min(result))+1)
