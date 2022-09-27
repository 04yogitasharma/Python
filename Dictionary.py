#It is a collection of key value pairs
#Dictionary is mutable
#we cannot add duplicate keys
myDic={
    "fast":"Quickely",
    "yogita":"student"
}

print(myDic['fast'])
print(myDic['yogita'])
myDic['yogita']='college student'
print(myDic['yogita'])

print(myDic.keys())
print(type(myDic))
print(myDic.values())
print(myDic.items())  #print both key values pair
print(myDic.get('yogita'))

