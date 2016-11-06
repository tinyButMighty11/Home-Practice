# home practice 1.py
#
# first python file downloaded at home
# trying guess the number game where
# computer chooses a number and the player
# tries to guess the number
#
#   102116 Emma Firminger
# need to add in what happens when they enter invald number
#need to add 

import random

num = random.randint(1,50)

print(" \t \t \n Welcome to GUESS THE NUMBER game!" +
      " What's your name?") #greeting

answer = input() # users name
name = answer

print(" \t \t \n Hello,",answer,"! I will choose a number between one and fifty, and you will have" +
      " five tries to guess it!") #explanation of the game

print(" \t \n What is your first guess?")

#print("Number = ",num) #debugging purposes

count = 5 #number of guesses

while count > 0:
    
    guess = input()
    number_guess = int(guess) #converting answer into integer so it can be compared
    
    count = count - 1 #takes away one turn every guess
    
    if number_guess > num: # guess is too high
        print(" \t \n Lower! You have ",count," guesses left!")

    elif number_guess < num: #guess is too low
        print("\t \n Higher! You have ",count," guesses left!")

    elif number_guess == num: #user guesses correct number
        print("\t \n Congratulations!! You guessed the number!" +
              "The number was",num,"! \nYou guessed it in ",5-count," tries!" +
              " See you next time,",name,"!")
        break
    else: #if answer is invalid?? not working right now...
        count = count + 1
        print("That is not a valid answer! Try again with a number between 1 and 50! You still" +
              " have ",count," tries left!")

while count == 0 and number_guess != num: #dont have any more turns and didnt guess it
    print("Sorry,",name,"! You didn't guess the number in the number of tries I gave you! The number was ",num,"!")
    break

print("\n\tWould you like to play again?") #ask user if play again

answer = input()
play_again = answer

if play_again == "Yes":
    while True:

        guess = input()
        number_guess = int(guess) #converting answer into integer so it can be compared
        
        count = count - 1 #takes away one turn every guess
        
        if number_guess > num: # guess is too high
            print(" \t \n Lower! You have ",count," guesses left!")

        elif number_guess < num: #guess is too low
            print("\t \n Higher! You have ",count," guesses left!")

        elif number_guess == num: #user guesses correct number
            print("\t \n Congratulations!! You guessed the number!" +
                  "The number was",num,"! \nYou guessed it in ",5-count," tries!" +
                  " See you next time,",name,"!")
            break
        else: #if answer is invalid?? not working right now...
            count = count + 1
            print("That is not a valid answer! Try again with a number between 1 and 50! You still" +
                  " have ",count," tries left!")

    while count == 0 and number_guess != num: #dont have any more turns and didnt guess it
        print("Sorry,",name,"! You didn't guess the number in the number of tries I gave you! The number was ",num,"!")
        break
else:
    print("Bye, ",name,"! Thanks for playing!")

      
