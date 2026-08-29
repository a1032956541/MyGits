while True:
    c =input("shuru:")
    if c== 'quit':
        break
    for a in c:
        print(f'{a}unicode:',ord(a))

while True:
    c =int(input("zi:"))
    if c == 0:
        break
    print(f'{c}char:',chr(c))