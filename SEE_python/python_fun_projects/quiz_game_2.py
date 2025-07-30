#!/usr/bin/env python3
"""
🎯 Interactive Quiz Game 🎯
A fun multiple-choice quiz covering Python, Movies, and General Knowledge!
"""

import random
import time

# Quiz questions organized by category
quiz_data = {
    "Python Programming 🐍": [
        {
            "question": "What is the correct way to create a list in Python?",
            "options": ["A) list = {1, 2, 3}", "B) list = [1, 2, 3]", "C) list = (1, 2, 3)", "D) list = <1, 2, 3>"],
            "correct": "B",
            "explanation": "Square brackets [] are used to create lists in Python!"
        },
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["A) function", "B) define", "C) def", "D) func"],
            "correct": "C",
            "explanation": "'def' is the keyword used to define functions in Python."
        },
        {
            "question": "What will len('Hello World') return?",
            "options": ["A) 10", "B) 11", "C) 12", "D) 9"],
            "correct": "B",
            "explanation": "'Hello World' has 11 characters including the space!"
        },
        {
            "question": "Which of these is NOT a valid Python data type?",
            "options": ["A) int", "B) string", "C) list", "D) dict"],
            "correct": "B",
            "explanation": "It's 'str', not 'string' in Python!"
        },
        {
            "question": "What does PEP stand for in Python?",
            "options": ["A) Python Enhancement Proposal", "B) Python Executive Program", "C) Python Error Protocol", "D) Python Extension Package"],
            "correct": "A",
            "explanation": "PEP stands for Python Enhancement Proposal - guidelines for Python development!"
        }
    ],
    
    "Movies & Entertainment 🎬": [
        {
            "question": "Which movie won the Academy Award for Best Picture in 2020?",
            "options": ["A) 1917", "B) Joker", "C) Parasite", "D) Once Upon a Time in Hollywood"],
            "correct": "C",
            "explanation": "Parasite made history as the first non-English film to win Best Picture!"
        },
        {
            "question": "Who directed the movie 'Inception'?",
            "options": ["A) Steven Spielberg", "B) Christopher Nolan", "C) Martin Scorsese", "D) Quentin Tarantino"],
            "correct": "B",
            "explanation": "Christopher Nolan is famous for his mind-bending films like Inception!"
        },
        {
            "question": "In which movie series would you find the character 'Hermione Granger'?",
            "options": ["A) Lord of the Rings", "B) Harry Potter", "C) Chronicles of Narnia", "D) Percy Jackson"],
            "correct": "B",
            "explanation": "Hermione Granger is one of the main characters in the Harry Potter series!"
        },
        {
            "question": "What is the highest-grossing film of all time (as of 2024)?",
            "options": ["A) Avengers: Endgame", "B) Avatar (2009)", "C) Titanic", "D) Star Wars: The Force Awakens"],
            "correct": "B",
            "explanation": "Avatar reclaimed the top spot after its 2022 re-release!"
        },
        {
            "question": "Which animated movie features the song 'Let It Go'?",
            "options": ["A) Moana", "B) Tangled", "C) Frozen", "D) Encanto"],
            "correct": "C",
            "explanation": "'Let It Go' is the iconic song from Disney's Frozen!"
        }
    ],
    
    "General Knowledge 🌍": [
        {
            "question": "What is the capital of Australia?",
            "options": ["A) Sydney", "B) Melbourne", "C) Canberra", "D) Perth"],
            "correct": "C",
            "explanation": "Canberra is the capital, though Sydney and Melbourne are larger cities!"
        },
        {
            "question": "Which planet is known as the 'Red Planet'?",
            "options": ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
            "correct": "B",
            "explanation": "Mars appears red due to iron oxide (rust) on its surface!"
        },
        {
            "question": "What is the largest mammal in the world?",
            "options": ["A) African Elephant", "B) Blue Whale", "C) Giraffe", "D) Hippopotamus"],
            "correct": "B",
            "explanation": "Blue whales can grow up to 100 feet long and weigh up to 200 tons!"
        },
        {
            "question": "In which year did World War II end?",
            "options": ["A) 1944", "B) 1945", "C) 1946", "D) 1947"],
            "correct": "B",
            "explanation": "World War II ended in 1945 with Japan's surrender in September."
        },
        {
            "question": "What is the smallest country in the world?",
            "options": ["A) Monaco", "B) San Marino", "C) Vatican City", "D) Liechtenstein"],
            "correct": "C",
            "explanation": "Vatican City is only about 0.17 square miles (0.44 square kilometers)!"
        }
    ]
}

class QuizGame:
    def __init__(self):
        self.total_score = 0
        self.total_questions = 0
        self.categories_completed = []
    
    def display_welcome(self):
        """Display welcome message and game info"""
        print("🎉" * 20)
        print("🎯 WELCOME TO THE ULTIMATE QUIZ GAME! 🎯")
        print("🎉" * 20)
        print("\n📚 Categories available:")
        for i, category in enumerate(quiz_data.keys(), 1):
            print(f"   {i}. {category}")
        print("\n🏆 Answer questions correctly to earn points!")
        print("💡 You'll get explanations for each answer!")
        print("🎮 Let's test your knowledge!\n")
    
    def select_category(self):
        """Let user select a quiz category"""
        categories = list(quiz_data.keys())
        
        print("🎯 CATEGORY SELECTION")
        print("-" * 30)
        for i, category in enumerate(categories, 1):
            status = "✅ Completed" if category in self.categories_completed else "⭐ Available"
            print(f"{i}. {category} - {status}")
        print(f"{len(categories) + 1}. 🎲 Random Mix")
        print(f"{len(categories) + 2}. 🏁 Finish Game")
        
        while True:
            try:
                choice = int(input(f"\nChoose category (1-{len(categories) + 2}): "))
                if 1 <= choice <= len(categories):
                    return categories[choice - 1]
                elif choice == len(categories) + 1:
                    return "random"
                elif choice == len(categories) + 2:
                    return "finish"
                else:
                    print("❌ Invalid choice! Try again.")
            except ValueError:
                print("❌ Please enter a number!")
    
    def get_questions(self, category):
        """Get questions for the selected category"""
        if category == "random":
            all_questions = []
            for cat_questions in quiz_data.values():
                all_questions.extend(cat_questions)
            return random.sample(all_questions, min(5, len(all_questions)))
        else:
            return quiz_data[category].copy()
    
    def ask_question(self, question_data, question_num, total_questions):
        """Ask a single question and return if it was answered correctly"""
        print(f"\n🔥 QUESTION {question_num}/{total_questions}")
        print("=" * 50)
        print(f"❓ {question_data['question']}")
        print()
        
        for option in question_data['options']:
            print(f"   {option}")
        
        print("-" * 50)
        
        while True:
            answer = input("Your answer (A, B, C, or D): ").upper().strip()
            if answer in ['A', 'B', 'C', 'D']:
                break
            print("❌ Please enter A, B, C, or D!")
        
        # Show result with suspense
        print("\nChecking answer", end="")
        for _ in range(3):
            time.sleep(0.5)
            print(".", end="", flush=True)
        print()
        
        if answer == question_data['correct']:
            print("🎉 CORRECT! 🎉")
            print(f"💡 {question_data['explanation']}")
            return True
        else:
            print("❌ Incorrect!")
            print(f"✅ The correct answer was: {question_data['correct']}")
            print(f"💡 {question_data['explanation']}")
            return False
    
    def run_quiz(self, category):
        """Run a complete quiz for the selected category"""
        questions = self.get_questions(category)
        random.shuffle(questions)
        
        category_name = category.title() if category == "random" else category
        print(f"\n🎯 Starting {category_name} Quiz!")
        print(f"📊 {len(questions)} questions coming up!")
        input("⌨️  Press Enter when ready...")
        
        score = 0
        for i, question in enumerate(questions, 1):
            if self.ask_question(question, i, len(questions)):
                score += 1
            
            if i < len(questions):
                input("\n⌨️  Press Enter for next question...")
        
        # Update totals
        self.total_score += score
        self.total_questions += len(questions)
        
        if category != "random" and category not in self.categories_completed:
            self.categories_completed.append(category)
        
        # Show category results
        print("\n" + "🏆" * 20)
        print("📊 CATEGORY RESULTS")
        print("🏆" * 20)
        print(f"✅ Correct answers: {score}/{len(questions)}")
        percentage = (score / len(questions)) * 100
        print(f"📈 Category score: {percentage:.1f}%")
        
        if percentage >= 80:
            print("🌟 Excellent work! You're a quiz master!")
        elif percentage >= 60:
            print("👍 Good job! Keep it up!")
        elif percentage >= 40:
            print("📚 Not bad! Room for improvement!")
        else:
            print("💪 Keep studying! You'll get better!")
        
        print("🏆" * 20)
    
    def show_final_results(self):
        """Display final game statistics"""
        if self.total_questions == 0:
            print("👋 Thanks for playing! Come back anytime!")
            return
        
        print("\n" + "🎊" * 25)
        print("🏆 FINAL GAME RESULTS 🏆")
        print("🎊" * 25)
        
        overall_percentage = (self.total_score / self.total_questions) * 100
        
        print(f"📊 Total Questions: {self.total_questions}")
        print(f"✅ Correct Answers: {self.total_score}")
        print(f"❌ Incorrect Answers: {self.total_questions - self.total_score}")
        print(f"📈 Overall Score: {overall_percentage:.1f}%")
        print(f"🎯 Categories Completed: {len(self.categories_completed)}")
        
        print("\n🏅 PERFORMANCE RATING:")
        if overall_percentage >= 90:
            print("🌟 QUIZ LEGEND! Outstanding performance!")
        elif overall_percentage >= 80:
            print("🥇 QUIZ MASTER! Excellent knowledge!")
        elif overall_percentage >= 70:
            print("🥈 QUIZ CHAMPION! Great job!")
        elif overall_percentage >= 60:
            print("🥉 QUIZ APPRENTICE! Good effort!")
        else:
            print("📚 QUIZ STUDENT! Keep learning!")
        
        print("🎊" * 25)
        print("🙏 Thanks for playing the Ultimate Quiz Game!")
        print("🧠 Keep learning and come back for more challenges!")
        print("🎊" * 25)
    
    def play(self):
        """Main game loop"""
        self.display_welcome()
        
        while True:
            category = self.select_category()
            
            if category == "finish":
                break
            
            self.run_quiz(category)
            
            print(f"\n🎮 Current overall score: {self.total_score}/{self.total_questions}")
            
            play_again = input("\n🔄 Continue with another category? (y/n): ").lower().strip()
            if play_again != 'y':
                break
        
        self.show_final_results()

def main():
    """Start the quiz game"""
    game = QuizGame()
    game.play()

if __name__ == "__main__":
    main()