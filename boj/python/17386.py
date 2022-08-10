import sys
input = sys.stdin.readline
x1, y1, x2, y2 = map(int,input().split())
x3, y3, x4, y4 = map(int,input().split())

p1 = [x1,y1]
p2 = [x2,y2]
p3 = [x3,y3]
p4 = [x4,y4]

def ccw(p1, p2, p3):
	return (p3[0]-p1[0])*(p2[1]-p1[1]) - (p2[0]-p1[0])*(p3[1]-p1[1])

ccw1 = ccw(p1, p2, p3)
ccw2 = ccw(p1, p2, p4)
ccw3 = ccw(p3, p4, p1)
ccw4 = ccw(p3, p4, p2)

if ccw1 * ccw2 < 0 and ccw3 * ccw4 < 0:
	print(1)
else:
	print(0)
#
#
#
#if x1 == x2:
#	if (x3-x1)*(x4-x1) < 0:
#		if min(y1,y2) <= min(y3,y4) and max(y3,y4) <= max(y1,y2):
#			print(1)
#	else:
#		print(0)
#elif y1 == y2:
#	if (y3-y1)*(y4-y1) < 0:
#		if min(x1,x2) <= min(x3,x4) and max(x3,x4) <= max(x1,x2):
#			print(1)
#	else:
#		print(0)
#else:
#	slope1 = (y2-y1)/(x2-x1)
#	d1 = (x2*y1 - x1*y2)/(x2-x1)
#	slope2 = (y4-y3)/(x4-x3)
#	d2 = (x4*y3 - x3*y4)/(x4-x3)
#
#	if slope1 == slope2:
#		print(0)
#	else:
#		xcross = (d2 - d1)/(slope1 - slope2)
#		ycross = xcross * slope1 + d1
#		xvalidmin = max(min(x1,x2), min(x3,x4))
#		xvalidmax = min(max(x1,x2), max(x3,x4))
#		yvalidmin = max(min(y1,y2), min(y3,y4))
#		yvalidmax = min(max(y1,y2), max(y3,y4))
#		if (xvalidmin <= xcross <= xvalidmax) and (yvalidmin <= ycross <= yvalidmax):
#			print(1)
#		else:
#			print(0)
