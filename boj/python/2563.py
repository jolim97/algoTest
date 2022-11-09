a = [[0] * 100 for _ in range(100)]
n = int(input())
for _ in range(n):
	x,y = map(int,input().split())
	for i in range(x,x+10):
		if i >= 100: break
		for j in range(y,y+10):
			if j >= 100: break
			a[j][i] = 1

area = 0
for a_i in a:
	area += sum(a_i)
print(area)
