print("Welcome to the Quiz Game!")
print("******************************************")
print("You will be asked a series of questions.")
print("******************************************")
print("Let's get started!\n")
score = 0
print("******************************************")
print("Question 1:")
print("What is the capital of France?")
print("A. Paris\nB. London\nC. Berlin")
print("******************************************")
question1 = input("Please enter your answer: ")
if question1 == "A" or question1.lower() == "paris":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is Paris.")
print("******************************************")
print("Question 2:")
print("What is 2 + 2?")
print("A. 3\nB. 4\nC. 5")
question2 = input("Please enter your answer: ")
if question2 == "B" or question2 == "4":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is 4.")
print("******************************************")
print("Question 3:")
print("What is the largest planet in our solar system?")
print("A. Earth\nB. Mars\nC. Jupiter")
question3 = input("Please enter your answer: ")
if question3 == "C" or question3.lower() == "jupiter":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is Jupiter.")
print(f"\nYour final score is {score} out of 3.")
print("Thank you for playing the Quiz Game!")
print("******************************************")
print("Goodbye!")
