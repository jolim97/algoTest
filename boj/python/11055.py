import sys
t = int(sys.stdin.readline().strip())
for _ in range(t):
    k = int(sys.stdin.readline().strip())
    pages = list(map(int,sys.stdin.readline().split()))
    print(pages)
    costs = 0
    while True:
        newpage = []
        for i in range(k-1):
            if i == 0: continue
            if pages[i] + pages[i-1] > pages[i] + pages[i+1]:

            if pages[i] < pages[i+1]:
                if pages[i] + pages[i+1] < pages[i+2]:
                    newpage.append(pages[i] + pages[i+1])

                continue

        newpages = []
        if len(pages) == 1:
            break
        for i in range(0,int(len(pages)/2)):
            newpages.append(pages[i*2] + pages[i*2+1])
            print(newpages)
        costs += sum(newpages)
        print(costs)
        if len(pages) % 2 == 1:
            newpages.append(pages[-1])
            print(newpages)
        pages = newpages
    print(costs)
