try:
    f = open('1.txt','r+')#读方式打开要求文件存在，否则异常
except Exception as e:
    f = open('1.txt', 'w')
    print(e.args)

