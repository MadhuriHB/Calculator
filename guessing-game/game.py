import random
secret_number = random.randint(1,100)
#random integer selection 

def validate_guess(user_input): 
    """Validates if the guessed number is within range"""
    if (user_input<1) or (user_input>100):
        print "Sorry you cant break the rules, please enter a valid number."
        return False        
    else:
        return True 

while True: 
    # Using this loop to continue the game

    print "Hello Player, Good Day!"
    print "Whats your name?"
    player_name=raw_input()
    print "Hello %s" % (player_name)
    print "Please guess a number between 1 and 100."
    print "I will tell you if your number is too high or too low."


    guess = None

    while guess != secret_number:
        # continue till guessed number is equal to secret number


        try:
            guess=int(raw_input(">>>")) #Validates if the input is an integer. 
        except:
            print "Oops! That was not a valid number, please try again."   #If not prints statement and goes to top of loop.
            continue                                        

        if validate_guess(guess): # Calling the function, if true it continues if false error message displayed and the game continues with new guesses
            if guess > secret_number:
                print "Your number is too high, please try again."
      
            else:
                print "Your number is too low, please try again."
            
        print "Whats your next guess?"


    print "You've got it! Congratulations! Would you like to play again?" # Congratulates user and asks if they wanna play again
    print "Enter 'Y' for yes or 'N' for no."

    answer = raw_input() #takes the input of user and continues or exits the game
    if answer == 'Y':
        continue
        
    else:
        print "Thank you for playing the game!"
        break

