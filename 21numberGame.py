# FUNCTION FOR RETURNING THE NEAREST MULTIPLE TO 4

def nearestMultiple(num):
    if num >= 4:
        near = num + (4 - (num % 4))
    else:
        near = 4
    return near

# FUNCTION TO CALL ONCE ONE PLAYER LOOSES

def lose():
    print("\n\n YOU HAVE LOOSE THE GAME")
    print("Better luck next time!!")
    exit(0)

# FUNCTION TO CHECKIF THE NUMBERS ARE CONSECUTIVE

def check(numbers):
    i = 1
    while i < len(numbers):
        if (numbers[i] - numbers[i - 1]) != 1:
            return False
        i += 1
    return True

# FUNCTION TO START THE GAME

def start():
    printOuts = []
    lastNumber = 0

    #LOOP RUN THE ENTIRE GAME
    while True:
        print("Enter 'F' to take the first chance")
        print("Enter 'S' to take the second chance")
        chance = input("> ")

        #PLAYER TAKES THE FIRST CHANCE
        if chance == "F":
            while True:
                if lastNumber == 20:
                    lose()
                else:
                    print("\n Your Turn")
                    print("\n How many numbers do you want to enter?")
                    userInput = input("> ")
                    userInput = int(userInput)

                    if userInput > 0 and userInput <= 3:
                        comp = 4 - userInput
                    else:
                        print("Wrong input. You're disqualified")
                        lose()
                
                    # DECLARE VARIABLE TO HELP ITERATING AND STORING ALL USER INPUTS
                    i, j = 1, 1

                    print("Now enter the values")
                    while i <= userInput:
                        a = input("> ")
                        a = int(a)
                        printOuts.append(a)
                        i += 1
                
                    #ASSIGN THE LAST PRINT OUT TO THE LAST VARIABLE

                    lastNumber = printOuts[-1]
                    if check(printOuts) == True:
                        if lastNumber == 21:
                            lose()
                        else:
                            # COMPUTER TURN
                            while j <= comp:
                                printOuts.append(lastNumber + j)
                                j += 1

                            print("The order of numbers after the computer turn is:")
                            print(printOuts)
                            lastNumber = printOuts[-1]

                    else:
                        print("You inputs are not consecutive numbers.!")
                        lose()

        # ELSE IF THE USER CHOSE THE SECOND CHANCE
        elif chance == "S":
            comp = 1
            lastNumber = 0
            while lastNumber < 20:
                j = 1
                while j <= comp:
                    printOuts.append(lastNumber + j)
                    j += 1

                print("\n The order of numbers after computer's turn is:")
                print(printOuts)
                if printOuts[-1] == 20:
                    lose()

                # PLAYER'STURN
                else:
                    print("\n Your Turn")
                    print("\n How many numbers do you want to enter?")

                    userInput = input("> ")
                    userInput = int(userInput)

                    i = 1

                    print("Enter your numbers")
                    while i <= userInput:
                        printOuts.append(int(input("> ")))
                        i += 1

                    lastNumber = printOuts[-1]

                    if check(printOuts) == True:
                        near = nearestMultiple(lastNumber)
                        comp = near - lastNumber
                        if comp == 4:
                            comp = 3
                        else:
                            comp = comp 
                    else:
                        print("\n The numbers you have entered are not consecutive")
                        lose()

            print("\n CONGRATULATIONS !!!")
            print("YOU WIN !!")
            exit(0)

        else:
            print("\n Wrong choice")


game = True

while game == True:
    print("Do you wish to play 21 NUMBER GAME? (YES / NO)")

    choice = input("> ")
    
    if choice == "YES":
        userName = input("\n Enter your name: ")
        print("Good luck,", userName)
        print("Computer is your opponet")
        start()

    elif choice == "NO":
        print("\n Dou you wish to quit the game? (YES / NO)")
        choice = input("> ")
        if choice == "YES":
            print("Quitting...")
            exit(0)
        elif choice == "NO":
            print("Continuing...")
        else:
            print("Wrong choice")

            



                