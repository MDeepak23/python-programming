def fibo(n):
	if n<=1:
		return n
	else:
		return (fibo(n-1)+fibo(n-2))
num = int(input())
for i in range(num):
	print(fibo(i),end=" ")

