# Rock, Paper, Scissors
# Build a rock-paper-scissors game where the user plays against the computer.
# The computer should make random choices, and the game should declare the winner
# based on the standard rules (rock beats scissors, scissors beats paper, paper beats rock).

import random


class RockPaperScissorGame:

    def __init__(self, computer_choice="", your_choice=""):
        self.computer_choice = computer_choice
        self.your_choice = your_choice

    def computer_turn(self):
        self.computer_choice = random.choice(['r', 'p', 's'])
        return self.computer_choice

    def your_turn(self):
        self.your_choice = input("Enter your choice: ")
        return self.your_choice

    def declare_winner(self):
        if self.computer_choice == 'r':
            if self.your_choice == 'r':
                return "You both selected rock!"
            elif self.your_choice == 'p':
                return "You win!"
            elif self.your_choice == 's':
                return "Computer wins!"
            else:
                return "You entered an invalid choice!"
        elif self.computer_choice == 'p':
            if self.your_choice == 'r':
                return "Computer wins!"
            elif self.your_choice == 'p':
                return "You both selected paper!"
            elif self.your_choice == 's':
                return "You win!"
            else:
                return "You entered an invalid choice!"
        elif self.computer_choice == 's':
            if self.your_choice == 'r':
                return "You win!"
            elif self.your_choice == 'p':
                return "Computer wins!"
            elif self.your_choice == 's':
                return "You both selected scissors!"
            else:
                return "You entered an invalid choice!"


def main():
    rpsgame = RockPaperScissorGame()
    print("This is a rock-paper-scissors game")
    print("Select 'r' for rock, 'p' for paper, and 's' for scissors")
    rpsgame.your_turn()
    print(f"Computer's choice: {rpsgame.computer_turn()}")
    print(rpsgame.declare_winner())


if __name__ == "__main__":
    main()