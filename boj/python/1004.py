import sys
input = sys.stdin.readline
import math

t = int(input())
for _ in range(t):
    x1,y1,x2,y2 = map(int,input().split())
    nplanets = int(input())
    planets = [ list(map(int,input().split())) for _ in range(nplanets) ]
    ninner = 0
    for p in planets:
        r1 = math.sqrt((x1 - p[0]) ** 2 + (y1 - p[1]) ** 2)
        r2 = math.sqrt((x2 - p[0]) ** 2 + (y2 - p[1]) ** 2)
        if (r1 - p[2]) * (r2 - p[2]) < 0:
            ninner += 1
    print(ninner)
