class QuizGame:
    def __init__(self, user):
        self.questions = [
            "How many elements are in the periodic table?:",
            "Which animal lays the largest eggs?:",
            "What is the most abundant gas in Earth's atmosphere?:",
            "How many bones are in the human body?:",
            "Which planet in the solar system is the hottest?:"
        ]
        self.options = [
            ["A. 116", "B. 117", "C. 118", "D. 119"],
            ["A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"],
            ["A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"],
            ["A. 206", "B. 207", "C. 208", "D. 209"],
            ["A. Mercury", "B. Venus", "C. Earth", "D. Mars"]
        ]
        self.answers = ["C", "D", "A", "A", "B"]
        self.user = user

    def ask_question(self, question_num):
        print("----------------------")
        print(self.questions[question_num])
        for option in self.options[question_num]:
            print(option)

        guess = input("Enter (A, B, C, D): ").upper()
        if guess == self.answers[question_num]:
            self.user.score += 1
            print("CORRECT!")
        else:
            print("INCORRECT!")
            print(f"The correct answer is: {self.answers[question_num]}")

    def play(self):
        for question_num in range(len(self.questions)):
            self.ask_question(question_num)
        print(f"Your total score is: {self.user.score}")