import random

userName = input("Enter Your Name: ")
print("Good Luck,", userName)

someWords = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = random.choice(someWords)

guesses = ""
turns = 12


while turns > 0:
    failed = 0 
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed += 1
        
    if failed == 0:
        print("Congratulations", userName, "You Won")
        print("The word is:", word)
        break
    
    print()
    userGuess = input("Enter your guess: ")
    guesses += userGuess

    if not userGuess in word:
        print("Incorrect Character, please try again!")
        turns -= 1
        print("You have", turns, "turns left")

    if turns == 0:
        print("You loose")
        break