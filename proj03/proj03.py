import random
# Name:Carter Moore
# Date:6-20-17


# """
# proj 03: Guessing Game
#
# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high,
# or exactly right. Keep the game going until the user types exit.
# Keep track of how many guesses the user has taken, and when the game ends, print this out.
#
# """
randomnumber=random.randint(1,9)
input=raw_input('Guess a number from 1 to 9 (No Limit). ')
number=1
if int(input)==randomnumber:
    print 'Congratulations! You guessed correctly on try number',number
while int(input)!=randomnumber:
    if int(input)<randomnumber:
        input=int(raw_input("That's a bit too low, try again "))
        number = number + 1
    else:
        input=int(raw_input("That's a bit too high, try again "))
        number = number + 1
if input==randomnumber:
    print 'Congratulations! You guessed correctly on try number',number


randomnumber=random.randint(1,9)
input=int(raw_input('Guess a number from 1 to 9 (5 Guess Limit). '))
number=0
# if int(input)==randomnumber:
#     print 'Congratulations! You guessed correctly on try number',number
while int(input)!=randomnumber:
    if number == 4:
        print raw_input("Sorry, you've run out of guesses, type exit to quit ")
    if input<randomnumber:
        input=raw_input("That's a bit too low, try again ")
        number = number + 1
    else:
        input=raw_input("That's a bit too high, try again ")
        number = number + 1
if input==randomnumber:
    print 'Congratulations! You guessed correctly on try number',number

#Exit doesn't really work yet, sorry about that.
#Unfinished