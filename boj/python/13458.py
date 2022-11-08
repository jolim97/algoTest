n = int(input())
a = list(map(int,input().split()))
b,c = map(int,input().split())

nsub = 0
for a_i in a:
    if a_i <= b:
        continue
    nsub += (a_i - b)//c + 1
    if (a_i - b)%c == 0: nsub -= 1
    
ans = n + nsub
print(ans)
