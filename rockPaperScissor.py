import random as rand




# THE DO YOU WISH CONTINUE FUNCTION

def cont():
    print("\n Do you wish to continue? (YES / NO)")
    inp = input("> ")
    
    if inp == "YES":
        print("\n Continuing...")
    elif inp == "NO":
        print("\n Do you wish to quit the game? (YES / NO)")
        inp = input("> ")
        if inp == "YES":
            print("\n Quitting...")
            exit(0)
        elif inp != "YES" or inp != "NO":
            print("\n Wrong choice")
            exit(0)

    else:
        print("\n Wrong input")

# DEFINE A FUNCTION TO START THE GAME
def gameStart():
    print("\n Rules of winning the game are as follows:",
          "\n Rock Vs Paper - > Paper Wins",
         "\n Rock Vs Scissors - > Rock Wins",
         "\n Paper Vs Scissors - > Scissors Win")

    game = True
    while game == True:

        # USER TURN
        # PROMPT THE USER TO INSERT HIS CHOICE & COMPUTER
        choices = ["Rock", "Paper", "Scissors"]

        print("\n Your turn")
        print("\n Enter your choice")
        userInput = input("> ")

        compChoice = rand.choice(choices)

        print("\n Computer's choice is:", compChoice)
        print("\n", userInput, "Vs", compChoice)

        if (userInput == "Rock" and compChoice == "Paper") or (compChoice == "Rock" and userInput == "Paper"):
            result = "Paper"
        elif (userInput == "Rock" and compChoice == "Scissors") or (compChoice == "Scissors" and userInput == "Rock"):
            result = "Rock"
        elif (userInput == "Scissors" and compChoice == "Paper") or (compChoice == "Scissors" and userInput== "Paper"):
            result = "Scissors"

        # DETERMINING THE WINNER

        if userInput == result:
            print("\n YOU WIN!!")
            cont()
        elif compChoice == result:
            print("\n The Computer Wins!!")
            cont()
        else:
            print("It's a tie")
            cont()


while True:
    print("\n <== WELCOME TO PLAYING ROCK PAPER SCISSORS ==>")
    print("\n Enter your name:")
    userName = input("> ")

    print("\n Good Luck", userName)
    print("\n Let the game begin...")

    gameStart()

