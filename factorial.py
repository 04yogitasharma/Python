def fact(n):
    if n==1 or n==0:
        return 1
    return n*fact(n-1)    

i=5
res=fact(i)
print(res)