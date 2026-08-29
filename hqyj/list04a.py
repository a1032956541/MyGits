a=list(range(10,50,10))
print(a)
b = a[:]
b[0]=11
print(a)

l1=list(range(1,31))
print(l1)

l2=[x for x in l1 if (x%3==0 or x%5==0)]
print(l2)

l3=[x for x in [x for x in l1 if x%2 != 0] if (x%3==0 or x%5==0)]
print(l3)

l4=[x for x in [x for x in [x for x in l1 if x%9 != 0] if x%2 != 0] if (x%3==0 or x%5==0)]
print(l4)