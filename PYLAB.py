                             #set1
"""
f = int(input())
c = (f-32)*5/9
print(c)"""

"""
a = int(input())
b = int(input())
a = a^b
b = a^b
a = a^b
print(a,b)"""

"""
d = {1:'apple',2:'bannana',3:'mango'}
key = int(input())
if key in d.keys():
    print("found")
else:
    print("not found")"""

                             
                            #set2

"""
a = ['a','e','i','o','u','A','E','I','O','U']
b = input()
if b in a:
    print("vowel")
else:
    print("consonant")"""

"""
s = input().split(' ')
L = [int(i) for i in s]
print(L)
print(L.index(max(L)))
print(L.index(min(L)))"""
            
"""
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
n = int(input())
print(fact(n))"""

                                #set3
"""
s = input().split(' ')
L = [int(i) for i in s]
print(L)
print(sum(L))
print(sum(L)/len(L))"""

"""
def fib(n):
    if n<=1:
        return n
    else:
        return (fib(n-1)+fib(n-2))
n = int(input())
for i in range(n):
    print(fib(i),end=" ") """

                               #set 4
'''
year = int(input())
if (year%4==0 and year%100!=0) or (year%400==0):
    print("leap year")
else:
    print("not a leap year") '''

""""
list1 = ["M","NA","I","ABHI"]
list2 = ["Y","ME","S","RAM"]
list=[]
for i in range(len(list1)):
    list.append(list1[i]+list2[i])
print(list) """

'''
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(a,b%a)
print(gcd(6,12)) '''

                              #SET 6
"""
s = input().split(' ')
L = [int(i) for i in s]
print(L)
L[0],L[-1] = L[-1],L[0]
print(L) """

"""
s = input().split(" ")
for i in s:
    if(len(i)%2==0):
        print(i) """

"""
s = input().split(' ')
L = [int(i) for i in s]
print(L)
even =  []
odd = []
for i in L:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print(odd)
print(even) """

"""
s = input()
rev = ""
for i in s:
    rev = i+rev
print(rev) """

"""
class A:
    def parent(self):
        print("parent class")
class B(A):
    def child1(self):
        print("child class1")
class C(B):
    def child2(self):
        print("child class 2")
obj = C()
obj.parent()
obj.child1()
obj.child2() """

                             #set 8

"""
d = {1:'apple',2:'banana'}
d.update({3:'orange'})
print(d) """

"""
class A:
    def __init__(self,m,n):
        self.n1 = m
        self.n2 = n
        print(self.n1+self.n2)
obj = A(2,3) """

                          #set 9

"""
s = input().split(' ')
L = [int(i) for i in s]
print(L)
ele = max(L)
L.remove(ele)
print(max(L)) """

                                  #set 10
s = input()
if(s == s[::-1]):
    print("palindrome")
else:
    print("not a palindrome")


