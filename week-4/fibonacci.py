n = int(input("enter n:"))
a,b = 0,1
while(n>0):
        print(a,b)
	c = a+b
	a = b
	b = c
	print(a,end=" ")
	n-=1


