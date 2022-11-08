import sys
input = sys.stdin.readline
n = 9
a = []
for _ in range(n):
	a.append(list(map(int,input().split())))
m = 0
m_i = 0
m_j = 0
for ni,a_i in enumerate(a):
	for nj,j in enumerate(a_i):
		if j > m:
			m = j
			m_i = ni
			m_j = nj

print(m)
print(m_i+1,m_j+1)
