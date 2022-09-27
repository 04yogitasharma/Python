# When we want to print the set of statements in our program
#while loop
i=0
while i<10:
    print("Yes")
    i=i+1
print("Done")    


#printing first 50 natural number
i=0
for i in range(51) :
    print(i)
    
print("done")

#use of break statement
for i in range(51):
    print(i)
    if(i==20):   #it use to break the loop
        break
print("done")    

#use of continue statement

for i in range(20):
    if(i==10):
        continue #it is used to just skip that 1 statement and the continue from next
    print(i)
print("done")    

#we use pass statement to do nothing it is used as null statement
