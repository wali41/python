
def football_game():
    score = 0
    chances = 5
    print("Welcome to the Football Game!")
    print("You have 5 chances to score goals.\n")
    for chance in range(1, chances + 1):
        print(f"Chance {chance}:")
        action = input("Choose your action (shoot/pass/dribble): ").strip().lower()
        if action == "shoot":
         if random.random() < 0.5:
                print("Goal! You scored.")
                score += 1
            else:
                print("Missed! The goalkeeper saved it.")
        elif action == "pass":
            if random.random() < 0.7:
                print("Good pass! You get another chance to shoot.")
                if random.random() < 0.5:
                    print("Goal after pass!")
                    score += 1
                else:
                    print("Missed after pass.")
            else:
                print("Bad pass! You lost the ball.")
        elif action == "dribble":
                if random.random() < 0.6:
                print("Nice dribble! You get closer to the goal.")
                if random.random() < 0.5:
                    print("Goal after dribble!")
                    score += 1
                else:
                    print("Missed after dribble.")
            else:
                print("Lost the ball while dribbling.")
        else:
            print("Invalid action. You lost your chance.")

        print(f"Current score: {score}\n")

    print(f"Game over! Your final score is {score} out of {chances}.")

if __name__ == "__main__":
    football_game()