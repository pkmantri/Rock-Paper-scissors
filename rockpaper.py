import random

def get_computer_choice():
    """Randomly selects Rock, Paper, or Scissors for the computer."""
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    """Determines the winner based on user and computer choices."""
    if user_choice == computer_choice:
        return "It's a tie!"
    
    winning_combinations = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }
    
    if winning_combinations[user_choice] == computer_choice:
        return "You win!"
    else:
        return "Computer wins!"

def main():
    """Main function to run the Rock, Paper, Scissors game."""
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        user_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()
        
        if user_choice == "quit":
            print("Thanks for playing! Goodbye!")
            break
        
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        print("-" * 30)  # Separator for readability

if __name__ == "__main__":
    main()
