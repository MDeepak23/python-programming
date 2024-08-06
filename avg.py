l = []
n = int(input("enter n:"))
for i in range(n):
	ele = int(input("enter element:"))
	l.append(ele)
print(l)
SUM = sum(l)
avg = sum(l)/len(l)
print(SUM,avg)
