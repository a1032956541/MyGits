str="友谊就是栖身于两个身体中的同一灵魂"
print(str[::-1])

str1 = list(str[::-1])
print(str1)
str1.reverse()
str1 = ''.join(str1)
print(str1)

s = "Hello\nWorld"
print(len(s))



con=[]
while True:
    c = input("输入任意单词：")
    if c == 'quit':
        break
    con.append(c)
s1='_'.join(con)
print(f'用户输入：{s1}')
