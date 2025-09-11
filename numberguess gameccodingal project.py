# Number Guessing Game

import random

def game():

    print("Welcome to the Number Guessing Game")

    secret_num = random.randint(1, 100)

    play = input("Would you like to play this game. (Enter yes/no)")

    attempts = 0

    while play.lower() == "yes":

        try:

            guess_num = int(input("Guess a number between 1 and 100: "))

            attempts = attempts + 1

            if guess_num >= 1 or guess_num <= 100:

                if guess_num < secret_num:

                    print("Too low! Try again.")

                elif guess_num > secret_num:

                    print("Too high! Try again.")

                else:

                            print("Congratulations! You guessed the number {secret_number} in {attempts} attempts.")




                            break

        except:

            print("Invalid input. Please enter a valid number.")

    else:

        print("Have a nice day")

game()  

         



































































