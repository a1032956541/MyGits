print("hello world!")
price = input("请输入产品单价：")  # 返回字符串
print(type(price))
price = float(price)
print(type(price))
num = int(input("请输入数量："))
pay = float(input("输入支付的金额："))
change = pay - price * num
print("找回金额：" +str(change))