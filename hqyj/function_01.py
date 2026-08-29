def sum(n):
    res = 0
    i = 1
    while i < (n+1):
        res += i
        i+=1
    return res


n=int(input('shuru:'))
res= sum(n)
print(res)