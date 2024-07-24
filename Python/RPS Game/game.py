import os
import random
while True:
    print("Welcome to Rock, Paper, Scissors game\n")
    print("Press 'e' to exit\n")

    rcomp = random.randint(1,3)

    comp = print("Comp's Turn")
    you = input("Your's Turn : Press 'r' for Rock, 'p' Paper or 's' Scissors\n")
    
    if you=='e':
        break

    if rcomp == 1:
        comp = "r"
    elif rcomp == 2:
        comp = "p"
    else:
        comp = "s"

    def game(comp, you):
        if comp == you:
            return None
        elif comp == 'r':
            if you == 'p':
                return False
            elif you == 's':
                return True
        
        elif comp == 'p':
            if you == 'r':
                return True
            elif you == 's':
                return False
        
        elif comp == 's':
            if you == 'r':
                return False
            elif you == 'p':
                return True

    a = game(comp, you)
    print(f"You chose {you}")
    print(f"computer chose {comp} ")
    if a == None:
        print("It's a tie")
    elif a == True:
        print("You Win")
    elif a == False:
        print("You Lose")



