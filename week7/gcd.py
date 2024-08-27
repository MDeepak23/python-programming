def gcd(a,b):
	if(b==0):
		return a
	else:
		return gcd(b,a%b)
a = int(input("enter a:"))
b = int(input("enter b:"))
print(gcd(a,b))
