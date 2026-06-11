import random

options = ["Rock", "Paper", "Scissor"]

while True:
    player1 = input("Player 1: enter your choice (Rock, Paper, Scissor): ").strip().capitalize()
    if player1 not in options:
        print("Invalid choice. Please enter Rock, Paper, or Scissor.")
        continue

    player2 = random.choice(options)
    print(f"Player 1 chose: {player1}")
    print(f"Player 2 chose: {player2}")

    if player1 == player2:
        print("It's a tie!")
    elif player1 == "Rock" and player2 == "Scissor":
        print("Player 1 wins!")
    elif player1 == "Paper" and player2 == "Rock":
        print("Player 1 wins!")
    elif player1 == "Scissor" and player2 == "Paper":
        print("Player 1 wins!")
    else:
        print("Player 2 wins!!! Better luck next time.")

    again = input("Play again? (y/n): ").strip().lower()
    if again != "y":
        print("Thanks for playing!")
        break