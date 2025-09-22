# Test Bath - A Menu Driven Quiz Program

def show_menu():
    print("\n=== Test Bath ===")
    print("1. Take Quiz")
    print("2. View Score")
    print("3. Exit")

def take_quiz():
    print("\n--- Quiz Started ---")
    questions = {
        "What is the capital of France? ": "paris",
        "Which planet is known as the Red Planet? ": "mars",
        "Who developed the theory of relativity? ": "einstein",
        "What is the largest mammal? ": "blue whale",
        "What is the square root of 64? ": "8",
        "What is the chemical symbol for water? ": "h2o",
        "Who wrote 'Romeo and Juliet'? ": "shakespeare",
        "In which year did World War II end? ": "1945",
        "Which is the fastest land animal? ": "cheetah",
        "What is the boiling point of water in Celsius? ": "100",
        "Which country is known as the Land of the Rising Sun? ": "japan",
        "How many continents are there on Earth? ": "7",
        "Which gas do humans inhale to survive? ": "oxygen",
        "Who painted the Mona Lisa? ": "da vinci",
        "What is the hardest natural substance on Earth? ": "diamond"
    }

    score = 0
    for q, ans in questions.items():
        user_ans = input(q).strip().lower()
        if user_ans == ans:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {ans.capitalize()}")
    print(f"\nYou scored {score}/{len(questions)}")
    return score

def main():
    total_score = 0
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            total_score = take_quiz()
        elif choice == "2":
            print(f"\nYour latest score is: {total_score}")
        elif choice == "3":
            print("\nThanks for playing Test Bath! 👋")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
