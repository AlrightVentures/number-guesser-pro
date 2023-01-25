# Wednesday night fun - numberGuesserPro

# Import libraries, modules
import random 

# Define a function to control the random guessing game
def guess(): 

    while True: 
        # Ask user to pick a random number
        userNumberPick = int(input("Please pick a number between 2 and 100.\n"))

        if 2 <= userNumberPick <= 100:
            break
        else: 
            print("Please provide a valid number.\n")

    # Generate a random number between 1 and x which is provided by the user
    randomNumber = random.randint(1,userNumberPick)

    # Initialise guess variable
    guessedNumber = 0

    # Keep track of the number of tries
    tryCount = 1

    # Ask user to provide a number they think is the correct guess
    guessedNumber = int(input(f"Try to guess the correct number between 1 and {userNumberPick}\n"))

    # Run a while loop until the guessed number matches the randomly generated number
    while guessedNumber != randomNumber:

        # Provide 'higher' or 'lower' clues to the user to help them reach the correct number
        if guessedNumber < randomNumber:
            guessedNumber = int(input("Try a higher number!\n"))
        elif guessedNumber > randomNumber: 
            guessedNumber = int(input("Try a lower number!\n"))
        
         # Increase tryCounter by 1
        tryCount += 1
    
    # Print a message to provide final 'success' message to the user including the number of tries
    print("Well done! You've guessed correctly!")
    print("It took you 1 time." if tryCount == 1 else f"It took you {tryCount} times.\n")

# Call guess function to play the game
guess()

# Made with love.
# Check out Harry Mack on YouTube. 
# Have a great day.