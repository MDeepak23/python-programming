f = open('deepak.txt','w')
f.write("hello,world")
f = open('deepak.txt','a')
f.write(" cse-c")
f = open('deepak.txt','r')
print(f.read())
f.seek(5)
pos = f.tell()
print(pos)
f.read(5)
pos = f.tell()
print(pos)
f.close()

