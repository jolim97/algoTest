l = input()
operators = []
for i in str(l):
    if i == "+":
        operators.append(1)
    elif i == "-":
        operators.append(-1)
l = l.replace("+"," ").replace("-"," ")
numbers = list(map(int,l.split()))
result = numbers[0]
isMinus = False
for i in range(len(operators)):
    if operators[i] == -1:
        isMinus = True
    if isMinus:
        result -= numbers[i+1]
    else:
        result += numbers[i+1]
print(result)
