###rock paper scissors####
import random

user=int(input("enter your chioce 0 for rack,1 for paper,2 for scissers :"))
if user>2 or user<0:
        print("your enetered invalid number,you lose!")
else:
        computer=random.randint(0,2)
        print(f"computer enters:{computer}")
        if user==computer:
          print("tie break! play again")              
        elif computer > user:
          print("you lose")
        elif user > computer:
          print("you won")
        elif user == computer:
           print("tie break! play again")
        elif user==0 and computer==2:
          print("you won")
        elif user==2 and computer==0:
         print("you lose")
#


        
  
        
    



    
        
    