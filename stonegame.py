import random

def rock_paper_scissors(player_score=0, computer_score=0):
    """
    Rock Paper Scissors game using recursion.
    """
    
    choices = ['rock', 'paper', 'scissors']
    
    print(f"\nScore - You: {player_score}, Computer: {computer_score}")
    player_input = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()
    
    if player_input == 'quit':
        print(f"\nFinal Score - You: {player_score}, Computer: {computer_score}")
        return
    
    if player_input not in choices:
        print("Invalid input! Please enter rock, paper, or scissors.")
        return rock_paper_scissors(player_score, computer_score)
    
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    
    if player_input == computer_choice:
        print("It's a tie!")
    elif (player_input == 'rock' and computer_choice == 'scissors') or \
         (player_input == 'paper' and computer_choice == 'rock') or \
         (player_input == 'scissors' and computer_choice == 'paper'):
        print("You win this round!")
        player_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1
    
    return rock_paper_scissors(player_score, computer_score)

if __name__ == "__main__":
    rock_paper_scissors()