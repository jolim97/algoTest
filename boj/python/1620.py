import sys
input = sys.stdin.readline
n,m = map(int,input().split())
book = []
for _ in range(n):
    pokemon = input().strip()
    book.append(pokemon)
for _ in range(m):
    question = input().strip()
    if question.isnumeric():
        print(book[int(question)-1])
    else:
        print(book.index(question)+1)
