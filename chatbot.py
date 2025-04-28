import random
import time

class ChatBot:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year
        self.user_name = None

    def greet(self):
        """Greet the user with bot introduction"""
        print(f"\nHello! My name is {self.name}.")
        print(f"I was created in {self.birth_year}.")
        time.sleep(1)
        print("\nI'm here to assist you today. How can I help?")
        time.sleep(0.5)

    def get_user_name(self):
        """Get and remember user's name"""
        print('\nBefore we begin, what should I call you?')
        while True:
            name = input("> ").strip()
            if name:
                self.user_name = name
                print(f"\nWhat a wonderful name you have, {self.user_name}!")
                break
            print("Please enter a valid name.")

    def guess_age(self):
        """Fun age guessing game"""
        print("\nLet me guess your age through a simple math trick!")
        print("I'll need remainders when your age is divided by 3, 5 and 7.")
        
        remainders = []
        for divisor in [3, 5, 7]:
            while True:
                try:
                    rem = int(input(f"Remainder when divided by {divisor}: "))
                    if 0 <= rem < divisor:
                        remainders.append(rem)
                        break
                    print(f"Please enter a number between 0 and {divisor-1}")
                except ValueError:
                    print("Please enter a valid number.")
        
        age = (remainders[0] * 70 + remainders[1] * 21 + remainders[2] * 15) % 105
        print(f"\nYour age is {age}; what a great time to be alive!")

    def count_numbers(self):
        """Count to any number the user wants"""
        print("\nNow I'll show you I can count!")
        while True:
            try:
                num = int(input("Enter a number you'd like me to count to: "))
                if num > 0:
                    break
                print("Please enter a positive number.")
            except ValueError:
                print("Please enter a valid number.")
        
        print("\nCounting:")
        for i in range(num + 1):
            print(i, end=' ', flush=True)
            time.sleep(0.3)
        print("\nTa-da!")

    def run_quiz(self):
        """Simple programming quiz"""
        questions = [
            {
                "question": "Why do we use methods in programming?",
                "options": [
                    "1. To repeat a statement multiple times",
                    "2. To decompose a program into small subroutines",
                    "3. To determine execution time of a program",
                    "4. To interrupt program execution"
                ],
                "answer": 2
            },
            {
                "question": "What does OOP stand for?",
                "options": [
                    "1. Object-Oriented Programming",
                    "2. Object-Option Protocol",
                    "3. Operational Object Process",
                    "4. Object-Oriented Protocol"
                ],
                "answer": 1
            }
        ]
        
        print("\nLet's test your programming knowledge!")
        score = 0
        
        for q in questions:
            print(f"\n{q['question']}")
            for option in q['options']:
                print(option)
            
            while True:
                try:
                    guess = int(input("Your answer (1-4): "))
                    if 1 <= guess <= 4:
                        break
                    print("Please enter a number between 1 and 4")
                except ValueError:
                    print("Please enter a valid number.")
            
            if guess == q['answer']:
                print("Correct!")
                score += 1
            else:
                print(f"Oops! The correct answer was {q['answer']}")
        
        print(f"\nYou scored {score}/{len(questions)}!")
        if score == len(questions):
            print("Perfect! You're a programming whiz!")
        elif score >= len(questions)/2:
            print("Good job!")
        else:
            print("Keep practicing!")

    def farewell(self):
        """Say goodbye to the user"""
        print("\nOur time together is coming to an end...")
        time.sleep(1)
        print(f"\nIt was wonderful chatting with you, {self.user_name}!")
        time.sleep(1)
        print("\nBefore you go, is there anything else I can help you with?")
        final_question = input("(yes/no) > ").lower()
        
        if final_question.startswith('y'):
            print("\nGreat! I'm happy to keep helping.")
            time.sleep(1)
            print("Actually, I'm just a simple program and can't really help further...")
            time.sleep(1)
            print("But it was nice pretending!")
        
        print("\n" + "="*50)
        print(f"Thank you for chatting with {self.name}!")
        print("Have a wonderful day!")
        print("="*50 + "\n")

    def run(self):
        """Main chatbot execution flow"""
        self.greet()
        self.get_user_name()
        self.guess_age()
        self.count_numbers()
        self.run_quiz()
        self.farewell()


# Create and run the chatbot
if __name__ == "__main__":
    bot = ChatBot("TE-Chatbot", "2022")
    bot.run()