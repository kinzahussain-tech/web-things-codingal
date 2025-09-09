class Quiz:
    def __init__(self):
        # Constructor initializes questions and answers
        self.questions = [
            {"question": "1. What is the capital of Pakistan?", "answer": "Islamabad"},
            {"question": "2. What is 5 + 7?", "answer": "12"},
            {"question": "3. Which language is this quiz written in?", "answer": "Python"},
            {"question": "4. Who is the founder of Microsoft?", "answer": "Bill Gates"},
            {"question": "5. What is the square root of 64?", "answer": "8"}
        ]
        self.score = 0

    # Function to start the quiz
    def start_quiz(self):
        print("=== Welcome to the Quiz ===")
        for q in self.questions:
            print(q["question"])
            user_answer = input("Your answer: ")

            # Conditional check
            if user_answer.strip().lower() == q["answer"].lower():
                print("✅ Correct!\n")
                self.score += 1
            else:
                print(f"❌ Wrong! The correct answer is {q['answer']}.\n")

        print(f"=== Quiz Over! You scored {self.score}/{len(self.questions)} ===")


# Main program
quiz = Quiz()
quiz.start_quiz()
