# USER GUESSING A NUMBER ACCORDING TO THE RANGE OF HIS CHOICE
# 1 NUMBER GUESSING

import random

# lowestNumber = int(input("Enter the lowest bound "))
# highestNumber = int(input("Enter the highest bound "))

# randomNumber = random.randrange(lowestNumber,highestNumber)
# print(randomNumber)

userName = input("Enter Your Name: ")
print(userName + ", on the scale of 1 - 100, guess the secret random number.")

randomNumber = random.randrange(1, 100)

userGuess = input("Enter your Guess: ")
userGuess = int(userGuess)

turns = 10

while turns > 0:
    failed = 0

    while userGuess != randomNumber:

        while (userGuess > 100) or (userGuess < 1):
            print("\n Please enter a valid input.!!")
            exit(0)

        if userGuess < randomNumber:
            print("Opps.! Your guess is too low")
            failed += 1
            # turns -= 1
            print("You have", turns, "chances left")
            break

        elif userGuess > randomNumber:
            print("Opps.! Your guess it too high") 
            failed += 1
            # turns -= 1
            print("You have", turns, "chances left")
            break
        

    if failed == 0:
        print("You Won!!")
        print("The number is:", randomNumber)
        break

    userGuess = input("Enter another guess ")
    userGuess = int(userGuess)

    turns -= 1
    if turns == 0:
        print("You Loose!! You ran out of chances!!")
        print("The number is: ", randomNumber)
        break

    
    






