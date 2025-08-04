import random

def get_user_choice():
    while True:
        user_input = input("Choose Rock, Paper, or Scissors: ").lower()
        if user_input in ['rock', 'paper', 'scissors']:
            return user_input
        else:
            print("Invalid input! Please type rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "user"
    else:
        return "computer"

def display_result(user, computer, winner):
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win! 🎉")
    else:
        print("Computer wins! 💻")

def play_game():
    user_score = 0
    computer_score = 0

    print("=== Welcome to Rock-Paper-Scissors Game ===")
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, winner)

        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        print(f"\nScore => You: {user_score} | Computer: {computer_score}")

        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Final Score => You:", user_score, "| Computer:", computer_score)
            break

# Run the game
play_game()