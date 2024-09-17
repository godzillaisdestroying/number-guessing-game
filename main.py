import random

class NumberGuessingGame:
    def __init__(self, min_num=1, max_num=100):
        self.min_num = min_num
        self.max_num = max_num
        self.target_number = random.randint(self.min_num, self.max_num)
    
    def guess(self, user_guess):
        if user_guess < self.target_number:
            return "Too low!"
        elif user_guess > self.target_number:
            return "Too high!"
        else:
            return "Correct! You've guessed the number!"

    def start_game(self):
        print(f"Welcome to the Number Guessing Game! Try to guess the number between {self.min_num} and {self.max_num}.")
        attempts = 0
        while True:
            try:
                user_input = int(input("Enter your guess: "))
                attempts += 1
                result = self.guess(user_input)
                print(result)
                if result == "Correct! You've guessed the number!":
                    print(f"Congratulations! You guessed the number in {attempts} attempts.")
                    break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

# Example usage
if __name__ == "__main__":
    game = NumberGuessingGame(1, 100)  # Create a game where the target number is between 1 and 100
    game.start_game()  # Start the game
