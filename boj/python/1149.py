import sys
input = sys.stdin.readline
n = int(input())
prices = [ list(map(int,input().split())) for _ in range(n) ]
# DP
for i in range(n-1):
    prices[i+1][0] = min(prices[i][1],prices[i][2]) + prices[i+1][0]
    prices[i+1][1] = min(prices[i][0],prices[i][2]) + prices[i+1][1]
    prices[i+1][2] = min(prices[i][0],prices[i][1]) + prices[i+1][2]
print(min(prices[n-1]))
