l = []
n = int(input("enter n:"))
for i in range(n):
	ele = int(input("enter element:"))
	l.append(ele)
print(l)
l[0],l[-1] = l[-1],l[0]
print(l)
