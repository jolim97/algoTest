import sys
input = sys.stdin.readline
n = int(input())
papers = [ ]
for _ in range(n):
    papers.append(list(map(int,input().split())))
results = []
def cut_papers(x,y,n):
    global results
    color = papers[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != papers[i][j]:
                cut_papers(x, y, n//2)
                cut_papers(x, y+n//2, n//2)
                cut_papers(x+n//2, y, n//2)
                cut_papers(x+n//2, y+n//2, n//2)
                return
    results.append(color)

cut_papers(0,0,n)
print(results.count(0))
print(results.count(1))
