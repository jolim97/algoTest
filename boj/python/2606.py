import sys
input = sys.stdin.readline
ncomputers = int(input())
npairs = int(input())
graph = [ [0]*(ncomputers+1) for _ in range(ncomputers+1) ]
for _ in range(npairs):
    a,b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

def dfs(start,visited=[]):
    visited.append(start)
    for i in range(ncomputers+1):
        if (graph[start][i] == 1) and (i not in visited):
            dfs(i,visited)
    return len(visited)

ninfected = dfs(1)
print(ninfected-1)
