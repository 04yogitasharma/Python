a=[1,2,3,4,5]  #list is mutable
print(a)
a[0]=7  #we can change the values in list 
print(a)
print(a[0])
  
c=[34,'yogi',True,8.4]   #we can store different values in list

print(c)
  
#we can do slicing in list too

d=[1,5,3,9,10]
d.sort()
print(d)
d.reverse()
print(d)
d.append(45)
print(d)
d.insert(0,4)
print(d)
d.pop()
print(d)
d.remove(3)
print(d)