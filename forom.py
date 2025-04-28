import random
import time

class ChatBot:
    def __init__(self,name,birth_year):
        self.name=name
        self.birth_year=birth_year
        self.user_name=None


    def greet(self):
        print(f"\nHello! my name is !{self.name}.")
        print(f"I was created in {self.birth_year}.")
        time.sleep(1)
        print("\nI'm here to assist you today. How can I help?")
        time.sleep(0.5)

    def get_ser_name(self):
        print("\n Before staring can you tell me ypur name?")
        while True:
            name=input("> ").strip()
            if name:
                self.user_name=name
                print(f"what a wonderfull name u have! {self.user_name}!")
                break
            print("Please enter a valid name.")

    def guess_age(self):
        print("\n Let me guess ur age throough a siple math trick1")
        print("Ill just need remianders when ur age is divided by 3,5 and 7.")

        remainders=[]
        for divisor in [3,5,7]:
            while True:
                try:
                    rem=int(input(f"Remainder when divided by {divisor}:"))
                    if 0<=rem<divisor:
                        remainders.append(rem)
                        break
                    print(f"Please enter a number between 0 and {divisor-1}")
                except ValueError:
                    print("Please enter a valid number.")

            age=(remainders[0]*70+remainders[1]*21+remainders[2]*15)%105
            print(f"\nYour age is {age}; what a great time to be alive!")

    def count_numbers(self):
        print("\n Now ill show you that i can count!")

        while True:
            try:
                num=int(input("enter a number ud like me to count to: "))
                if num>0:
                    break
                print("Please enter a positive number.")    
            except ValueError:
                print("Please enter a valid number.")

        
        print("\n Counting...")

        for i in range(num+1):
            print(i,end=" ",flush=True)
            time.sleep(0.3)
        print("tada!")


    def run_quiz(self):
        print("\n now lets play a quiz")
        questions=[
            {
                "question": "What is the capital of France?",
                "options": ["1. Paris", "2. London", "3. Berlin", "4. Madrid"],
                "answer": 1
            },
            {
                "question": "What is 2 + 2?",
                "options": ["1. 3", "2. 4", "3. 5", "4. 6"],
                "answer": 2
            },
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["1. Earth", "2. Mars", "3. Jupiter", "4. Saturn"],
                "answer": 3
            }
        ]

        for q in questions:
            print(f"\n{q['question']}")
            for option in q['options']:
                print(option)

            while True:
                try:
                    ans=int(input("Your answer (1-4): "))
                    if 1<=ans<=4:
                        break
                    print("Please enter a number between 1 and 4.")
                except ValueError:
                    print("Please enter a valid number.")

                
            if ans==q['answer']:
                print("Correct!")
                score+=1   
            else:
                print("Incorrect!")
                print(f"The correct answer is {q['answer']}.")

        
        print("\nQuiz completed!")
        print(f"your score is {score}/{len(questions)}")
        print("Thanks for playing!")


    def farewell(self):
        print("our time is up!")
        time.sleep(1)
        print(f" {self.name}: I hope you enjoyed our time together {self.user_name}.")
        time.sleep(1)
        print(f"is there anything with which i can help!(yes/no)")
        final_question=input("> ").lower()
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
        





bot = ChatBot("TE-Chatbot", "2022")
bot.run()