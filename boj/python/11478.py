s = input()
l = len(s)
strset = set()
for i in range(1,l+1):
	for j in range(l-i+1):
		strset.add(s[j:j+i])
print(len(strset))
