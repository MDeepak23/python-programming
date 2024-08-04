n = int(input("enter n:"))
a,b = 0,1
while(n>0):
 print(a,end=" ")
	c = a+b
	a = b
	b = c
	n-=1


