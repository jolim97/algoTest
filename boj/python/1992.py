import sys
input = sys.stdin.readline
N = int(input())
qt = []
for _ in range(N):
	qt.append(list(input().rstrip()))


def search(x,y,n):
	icolor = qt[x][y]
	#out = icolor
	check = 0
	for i in range(x, x+n):
		for j in range(y, y+n):
			if icolor != qt[i][j]:
				print("(",end='')
				search(x, y, n//2)
				search(x, y + n//2, n//2)
				search(x + n//2, y, n//2)
				search(x + n//2, y + n//2, n//2)
				print(")",end='')
				return
	print(icolor,end='')
	return

search(0,0,N)
