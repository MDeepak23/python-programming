n = int(input("n:"))
sum = 0
num=n
order = len(str(n))

while(n>0):
	rem = n%10
	sum +=rem**order
	n = n//10
if sum == num:
	print("armstrong number")
else:
	print("not a armstrong number")
	
