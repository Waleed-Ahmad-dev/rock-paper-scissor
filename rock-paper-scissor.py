import random

while True:
    choices = ["rock", "paper", "scissors"]
    player = None
    computer = random.choice(choices)
    while player not in choices:
        player = input("rock, paper or scissors?: ").lower()

    if player == computer: 
        print(player)
        print(computer)
        print("It's a tie!")

    elif player == "rock":
        if computer == "paper":
            print(player)
            print(computer)
            print("You lose!")
        elif computer == "scissors":
            print(player)
            print(computer)
            print("You win!")

    elif player == "sscissors":
        if computer == "paper":
            print(player)
            print(computer)
            print("You win!")
        elif computer == "rock":
            print(player)
            print(computer)
            print("You lose!")

    elif player == "paper":
        if computer == "rock":
            print(player)
            print(computer)
            print("You win!")
        elif computer == "scissors":
            print(player)
            print(computer)
            print("You lose!")

    play_again = input("Play Again? (y/n): ").lower()

    if play_again == "y":
        continue

    elif play_again == "n":

        print("Bye!")
        break

