l = []
n = int(input("enter n:"))
for i in range(n):
	ele = int(input("enter element:"))
	l.append(ele)
print(l)
#using inbuilt method
l.reverse()
print(l)
#using slicing
print(l[::-1])
