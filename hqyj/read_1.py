f = open('1.txt','rb')
content = f.readline(3)
print(content.decode())
for i in content:
    print(i)
f.close()
