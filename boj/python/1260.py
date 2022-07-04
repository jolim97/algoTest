import sys
from collections import deque
input = sys.stdin.readline
n,m,v = map(int,input().split())
graph = [ [0]*(n+1) for _ in range(n+1) ]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1

# 깊이우선탐색 (재귀함수 이용)
def dfs(start, visited=[]):
    visited.append(start)
    print(start, end=' ')
    for w in range(len(graph[start])):
        if (graph[start][w] == 1) and (w not in visited):
            dfs(w,visited)

# 너비우선탐색 (queue 이용)
def bfs(start):
    visited = [start]
    queue = deque()
    queue.append(start)
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for w in range(len(graph[start])):
            if (graph[v][w] == 1) and (w not in visited):
                visited.append(w)
                queue.append(w)
dfs(v)
print()
bfs(v)
