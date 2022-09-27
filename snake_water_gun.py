import random

def game(comp,you):
    if(comp==you):
        return None

    elif comp=='s':
        if you=='w':
             return False
        elif(you=='g'):
            return True

    elif comp=='w':
        if you=='s':
             return True
        elif(you=='g'):
            return False 

    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True                  


print(("Comp turn : Snake(s) Water(w) Gun(g)?"))
randNo=random.randint(1,3)
# print(randNo)
if randNo==1:
    comp='s'
elif randNo==2:
    comp='w'
elif randNo==3:
    comp='g' 

you=input("Your Turn: Snake(s) Water(w) Gun(g) ? ")     
a=game(comp,you)

print("Computer choose :",comp)
print("you choose :",you)
if a==None:
    print("The game is tie!")
elif a:
    print("You Win!")    
else:
    print("You Lose!")