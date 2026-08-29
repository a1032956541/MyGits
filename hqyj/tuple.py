year =int(input('请输入年份：'))
month =int(input('请输入月分：'))
day =int(input('请输入日：'))

days=(31,28,31,30,31,30,31,31,30,31,30,31)
a = sum(days[:month-1])
if month > 2:
    if(year % 4 == 0 and year % 100 != 0) or year%400 ==0:
        a += 1
a += day
print(f'{year}年{month}月{day}日是该年中的第{a}天')