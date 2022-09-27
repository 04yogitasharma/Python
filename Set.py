#set is a collection of non repetitive element
#set is immutable
a={1,4,6,1,2,1}

print(type(a))
print(a)

#we cannot add list and dictionary in the set
#but we can add tupple in the set 

a.add(5)
print(a)
print(len(a))
a.remove(1)
print(a)
print(a.pop)  #remove an arbitrary element
print(a.clear)

b={1,2,3}
c={4,5,6}
print(b.union(c))
print(a.intersection(c))

 