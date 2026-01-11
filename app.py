import json
import random
import os

class QuizBackend:
    def __init__(self, filepath="questions.json"):
        self.filepath = filepath
        self.questions = []
        self.score = 0
    
    def load_questions(self):
        if not os.path.exists(self.filepath):
            print(f"Error: File '{self.filepath}' not found.")
            return False
            
        try:
            with open(self.filepath, 'r') as file:
                self.questions = json.load(file)
            return True
        except json.JSONDecodeError:
            print("Error: Invalid JSON format.")
            return False

    def start_quiz(self):
        if not self.load_questions():
            return

        random.shuffle(self.questions)
        total_questions = len(self.questions)
        
        print("\n" + "="*40)
        print(f"  WELCOME TO THE QUIZ ({total_questions} Questions)")
        print("="*40 + "\n")

        for index, item in enumerate(self.questions):
            print(f"Q{index + 1}: {item['question']}")
            
            for idx, option in enumerate(item['options']):
                print(f"   {idx + 1}. {option}")
            
            user_choice = self.get_valid_input(len(item['options']))
            
            # Check answer (input is 1-based, index is 0-based)
            if (user_choice - 1) == item['answer_index']:
                print("   ✅ Correct!\n")
                self.score += 1
            else:
                correct_opt = item['options'][item['answer_index']]
                print(f"   ❌ Wrong. Answer: {correct_opt}\n")

        self.show_results(total_questions)

    def get_valid_input(self, num_options):
        while True:
            try:
                choice = int(input("   Your Answer (Number): "))
                if 1 <= choice <= num_options:
                    return choice
                print(f"   Please enter 1-{num_options}.")
            except ValueError:
                print("   Invalid input.")

    def show_results(self, total):
        percentage = (self.score / total) * 100
        print("="*40)
        print("             QUIZ COMPLETE")
        print("="*40)
        print(f"Final Score: {self.score} / {total}")
        print(f"Percentage : {percentage:.1f}%")
        
        if percentage == 100:
            print("Rating     : 🏆 Perfect!")
        elif percentage >= 70:
            print("Rating     : 👏 Great Job!")
        else:
            print("Rating     : 📚 Keep Practicing")
        print("="*40 + "\n")

if __name__ == "__main__":
    app = QuizBackend()
    app.start_quiz()
