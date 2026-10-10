
import random

game = ["rock", "paper", "scissors"]

player_score = 0
computer_score = 0

while player_score < 3 and computer_score < 3:

    player = input("\nEnter your choice (rock/paper/scissors): ")
    choice = player.strip().lower()

    if choice not in game:
        print("Invalid input! Please choose rock, paper, or scissors.")
        continue

    comp = random.choice(game)

    print(f"Computer chose: {comp}")

    if comp == choice:
        print("Match draw!")

    elif (comp == "rock" and choice == "scissors") or \
         (comp == "paper" and choice == "rock") or \
         (comp == "scissors" and choice == "paper"):
        print("Computer won!")
        computer_score += 1

    else:
        print("Player won!")
        player_score += 1

    print(f"Player: {player_score} | Computer: {computer_score}")


print("\n===== GAME OVER =====")

if player_score == 3:
    print("Player won the game! 🏆")
else:
    print("Computer won the game!")

print(f"Final Score → Player: {player_score} | Computer: {computer_score}")
