import sys
input = sys.stdin.readline
n = int(input())
l = list(map(int,input().split()))

dp = [ 0 for _ in range(n) ]
for i in range(n):
	for j in range(i):
		if l[i] > l[j] and dp[i] < dp[j]:
			# Maximum elements in dp
			dp[i] = dp[j]
	dp[i] += 1
print(max(dp))
