#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      raopr
#
# Created:     04-05-2024
# Copyright:   (c) raopr 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# Guess the Number

import random

target = random.randint(1, 100)

while True:
    userChoice = input("Guess the target or Quit(Q): ")
    if userChoice == "Q":
        break

    userChoice = int(userChoice)  # Remove the extra colon here
    if userChoice == target:
        print("Success: Correct Guess!!")
        break
    elif userChoice < target:
        print("Your number was too small. Take a bigger guess...")
    else:
        print("Your number was too big. Take a smaller guess..")
sxxc
print("-------GAME OVER--------")
