#/usr/bin/env/python
'''
实现斐波那契额函数

'''

import sys

def fib1(n):#输出一个斐波那切数列，最大值小于n
    a, b = 0, 1
    while b < n:
        print(b,end=' ')
        a , b = b , a+b
    print()

def fib2(n):
    result=[]
    a,b=0,1
    while b < n:
        result.append(b)
        a, b = b , a+b
    return result


if __name__ == "__main__":
    fib1(100)
    l1=fib2(1000)
    print(l1)