import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n,m = map(int,input().split())
graph = [ [0] * (n+1) for _ in range(n+1) ]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1

# DFS
def dfs(start,visited=[]):
    visited.append(start)
    for i in range(1,n+1):
        if (graph[start][i] == 1) and (i not in visited):
            dfs(i,visited)
    return visited

start = 1
nconnected = 0
visited = []
for i in range(1,n+1):
    if i not in visited:
        nconnected += 1
        start = i
        visited = dfs(start,visited)
print(nconnected)
