import json
from Game import NumberGuessing
from QuizGame2 import QuizGame
from user import User

class Main:
    def __init__(self):
        self.users = self.add_users()
        self.current = None

    def add_users(self):
        try:
            with open("users.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_users(self):
        with open("users.json", "w") as file:
            json.dump(self.users, file)

    def sign_up(self):
        username = input("Enter your username: ")
        if username in self.users:
            print("Username already exists. Try logging in")
            return False
        password = input("Enter your password: ")
        self.users[username] = {"password": password, "score": 0}
        self.save_users()
        print("You registered successfully! Please log in")
        return False

    def login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username in self.users and self.users[username]["password"] == password:
            self.current = User(username, password)
            self.current.score = self.users[username]["score"]
            print(f"Welcome back, {username}! Your current score is {self.current.score}")
            return True
        else:
            print("Invalid username or password")
            return False

    def choose_game(self):
        while True:
            print("\nChoose a game:")
            print("1. Quiz Game")
            print("2. Number Guessing Game")

            choice = input("Enter 1 or 2: ")

            if choice == "1":
                quiz = QuizGame(self.current)
                quiz.play()
            elif choice == "2":
                number_guessing = NumberGuessing(self.current)
                number_guessing.play()
            else:
                print("Invalid choice")

            self.users[self.current.username]["score"] = self.current.score
            self.save_users()

            print(f"Your total score is: {self.current.score}")
            continue_playing = input("Do you want to continue playing? (yes/no): ").lower()
            if continue_playing != "yes":
                print("Thank you for playing! Goodbye!")
                break

    def run(self):
        print("Welcome to the Game!")
        while True:
            print("\n1. Register")
            print("2. Login")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.sign_up()
            elif choice == "2":
                if self.login():
                    self.choose_game()
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice")
if __name__ == "__main__":
    main = Main()
    main.run()