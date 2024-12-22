import random

class NumberGuessing:
    def __init__(self, user, min=50, max=100, tries=5):
        self.number = random.randint(min, max)
        self.tries = tries
        self.min_number = min
        self.max_number = max
        self.user = user

    def play(self):
        print(f"You have {self.tries} tries to guess the number between {self.min_number} and {self.max_number}")
        guess = None

        while guess != self.number and self.tries > 0:
            try:
                guess = int(input("Enter your guess: "))
                if guess < self.min_number or guess > self.max_number:
                    print(f"Please enter a number between {self.min_number} and {self.max_number}")
                    continue
            except ValueError:
                print("Invalid input! Please enter a valid integer")
                continue

            if guess < self.number:
                print("Guess higher!")
            elif guess > self.number:
                print("Guess lower!")
            else:
                print("You won!")
                self.user.score += 2
                break

            self.tries -= 1
            if self.tries == 0:
                print(f"You lost! The number was {self.number}")
            else:
                print(f"You have {self.tries} tries left")
