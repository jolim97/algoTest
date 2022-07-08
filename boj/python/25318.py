import sys
input = sys.stdin.readline

def days_of_months(endmonth,startmonth):
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    days_of_months = sum(days[startmonth-1:endmonth-1])
    return days_of_months

def calculate_timeperiod(year,month,day,hour,minute,second):
    # from 2019.01.01
    ydiff = year - 2019
    daydiff = day - 1
    hours_to_day = hour / 24. + minute / float(24*60) + second / float(24*60*60)
    ndays = days_of_months(month,1) + daydiff + hours_to_day
    if year == 2020:
        if month >= 3:
            return ydiff + (ndays + 1)/366.
        else:
            return ydiff + ndays/366.
    return ydiff + ndays/365.

n = int(input())
if n == 0:
    print(0)
else:
    timediffs = []
    scores = []
    for _ in range(n):
        a,b,score = input().rstrip().split()
        year,month,day = map(int,a.split("/"))
        hour,minute,second = map(int,b.split(":"))
        tp = calculate_timeperiod(year,month,day,hour,minute,second)
        timediffs.append(tp)
        scores.append(int(score))
    p = []
    for i in range(n):
        s = 0.5**((timediffs[-1]-timediffs[i]))
        pn = 0.9**(n-i-1)
        p.append(max(pn,s))
    p_dot_l = [ float(scores[i])*p[i] for i in range(n) ]
    x = sum(p_dot_l)/sum(p)
    print(round(x))
