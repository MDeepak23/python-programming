f = open('deepu.txt','wb')
f.write(b'\x00\x01\x03')
f = open('deepu.txt','rb')
print(f.read())
f.close()