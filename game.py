import random


def gameWin(comp,you):
    if comp == 's':
       if you == 'w':
           return False
       if you == 'g':
           return True
       
       
    if comp == 'w':
       if you == 'g':
           return False
       if you == 's':
           return True
       
       
       if comp == 'g':
         if you == 's':
           return False
       if you == 'w':
           return True
       
       
comp=print("the comp turn: snake(s) gun(g) or water(w)")
randNo=random.randint(1,3)
print(randNo)


if randNo == "1" :
   comp == 's'
elif randNo == "2":
   comp == 'g' 
elif randNo == "3" :
   comp == 'w'

you=input("your turn : snake(s) gun (g) or water(w) ")
a=gameWin( comp , you)


print(f"comp chose{comp}")
print(f"you chose {you}")


if a == None:
   print("game is tie") 
elif a:
   print("game win!") 
else :
   print("game lose!")
    