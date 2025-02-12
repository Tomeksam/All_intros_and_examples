# you have 3 lives, you roll a dice, if you get a 6 you win
# if you dont get a 6, you lose 1 life
from random import randint

lives = 3
while True: # as long as i have lives
    roll = input("Would you like to roll? ") # adding an extra spin on this class assignment, originally it would just run all three rolls at once
    if roll == "yes":
        # roll the dice
        dice = randint(1,6)
        if dice == 6:
            print("You rolled a 6! You win congrats bro!")
            again = input("Play again?")
            if again == "yes":
                lives = 3
            else: print("ok bro ;(")
            break # stops the code
        lives = lives - 1
        print("You rolled a", dice, "you have", lives, "left")
    else:
        print("bro lets play :D")
    if lives == 0:
        print("You lose!")
        again = input("Play again?")
        if again == "yes":
                lives = 3
        else: print("ok bro ;(")
        break
