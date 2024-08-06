l = []
n = int(input("enter n:"))
for i in range(n):
	ele = int(input("enter element:"))
	l.append(ele)
print(l)
k = int(input("enter k:"))
l.remove(k)
print(l)
