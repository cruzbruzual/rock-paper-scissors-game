
---

## **3. Python Code: `rps_game.py`**  
This code implements a game in which **the player enters his choice** and **the computer chooses randomly**.

```python
import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("🎮 Welcome to Rock, Paper, Scissors!")
    choices = ["rock", "paper", "scissors"]
    
    while True:
        user_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()
        if user_choice == "quit":
            print("Thanks for playing!")
            break
        
        if user_choice not in choices:
            print("Invalid choice! Please enter rock, paper, or scissors.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        print(determine_winner(user_choice, computer_choice))

if __name__ == "__main__":
    play_game()
