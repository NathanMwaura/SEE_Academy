#!/usr/bin/env python3
"""
Python Joke Generator 🐍😄
A fun program that displays random programming jokes!
"""

import random
import time

# Collection of Python and programming jokes
jokes = [
    "Why do Python programmers prefer dark mode?\nBecause light attracts bugs! 🐛",
    
    "How do you comfort a JavaScript bug?\nYou console it! 😢",
    
    "Why don't programmers like nature?\nIt has too many bugs! 🌿🐞",
    
    "Why did the Python break up with Java?\nBecause Java was too verbose and Python wanted something more... compact! 💔",
    
    "What's a programmer's favorite hangout place?\nFoo Bar! 🍺",
    
    "Why do programmers hate the outdoors?\nThere are too many trees and not enough binary! 🌳",
    
    "How many programmers does it take to change a light bulb?\nNone. That's a hardware problem! 💡",
    
    "Why did the programmer quit his job?\nHe didn't get arrays! 📊",
    
    "What do you call a programmer from Finland?\nNils! (Nils = None in Python) 🇫🇮",
    
    "Why do Python developers wear glasses?\nBecause they can't C! 👓",
    
    "What's the object-oriented way to become wealthy?\nInheritance! 💰",
    
    "Why did the variable break up with the constant?\nBecause she never changed! 💔",
    
    "How do you generate a random string?\nPut a Windows user in front of vi and tell them to exit! 😅",
    
    "Why don't programmers like to go outside?\nThe sun gives them arrays! ☀️",
    
    "What did the Python say to the C++?\nYou've got no class! 🐍",
    
    "Why do programmers prefer iOS development?\nBecause the Swift documentation is... swift to read! 📱",
    
    "What's a programmer's favorite type of music?\nAlgorithmic! 🎵",
    
    "Why did the programmer break up with their keyboard?\nIt wasn't their type! ⌨️",
    
    "How do you know a programmer is extroverted?\nThey look at YOUR shoes when talking to you! 👞",
    
    "Why don't programmers like parallel lines?\nBecause they never meet! Even in infinite loops! ∞"
]

def display_joke():
    """Display a random joke with some visual flair"""
    print("=" * 50)
    print("🐍 PYTHON JOKE GENERATOR 🐍")
    print("=" * 50)
    print()
    
    # Add suspense with dots
    print("Generating joke", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print("\n")
    
    # Select and display random joke
    joke = random.choice(jokes)
    print(joke)
    print()
    print("-" * 50)
    print("😄 Hope that made you smile! 😄")
    print("-" * 50)

def add_custom_joke():
    """Allow user to add their own joke"""
    print("\n🎯 Add Your Own Joke!")
    print("-" * 30)
    custom_joke = input("Enter your programming joke: ").strip()
    
    if custom_joke:
        jokes.append(custom_joke)
        print(f"✅ Great! Added your joke to the collection!")
        print(f"📊 Total jokes now: {len(jokes)}")
    else:
        print("❌ No joke entered!")

def show_menu():
    """Display the main menu"""
    print("\n🎮 MENU OPTIONS:")
    print("1. 😂 Show me a joke!")
    print("2. ➕ Add my own joke")
    print("3. 📊 Show joke count")
    print("4. 🚪 Exit")
    print("-" * 30)

def main():
    """Main program loop"""
    print("🎉 Welcome to the Python Joke Generator! 🎉")
    
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == "1":
            display_joke()
        elif choice == "2":
            add_custom_joke()
        elif choice == "3":
            print(f"\n📈 Current joke collection: {len(jokes)} jokes!")
        elif choice == "4":
            print("\n👋 Thanks for using Python Joke Generator!")
            print("🐍 Keep coding and keep laughing! 🐍")
            break
        else:
            print("\n❌ Invalid choice! Please enter 1, 2, 3, or 4.")
        
        # Pause before showing menu again
        input("\n⌨️  Press Enter to continue...")

if __name__ == "__main__":
    main()