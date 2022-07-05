n = int(input())
nfives = 0
nzeros = 0
for i in range(1,n+1):
    if i % 5 == 0:
        while True:
            i = i/5
            nfives += 1
            if i%5 != 0:
                break
    if i % 10 == 0:
        while True:
            i = i/10
            nzeros += 1
            if i%10 != 0:
                break
print(nfives+nzeros)

