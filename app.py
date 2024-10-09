import random
choices = ["Rock", "Paper", "Scissors"]
computer = random.choice(choices)
player = False
cpu_score = 0
player_score = 0
while True:
    player = input("Rock, Paper or  Scissors? enter 'end' to finish the game.").capitalize()

    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            cpu_score+=1
            computer = random.choice(choices)

        else:
            print("You win!", player, "smashes", computer)
            player_score+=1
            computer = random.choice(choices)

    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
            cpu_score+=1
            computer = random.choice(choices)

        else:
            print("You win!", player, "covers", computer)
            player_score+=1
            computer = random.choice(choices)

    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
            cpu_score+=1
            computer = random.choice(choices)

        else:
            print("You win!", player, "cut", computer)
            player_score+=1
            computer = random.choice(choices)

    elif player=='End':
        print("Final Scores:")
        print(f"CPU:{cpu_score}")
        print(f"Player:{player_score}")
        break

