import random

def rock_paper_scissors_game():
    while True:
        print("\nOptions:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Quit")

        user_choice = input("Enter your choice (1/2/3/4): ")

        if user_choice == "4":
            break

        choices = ["rock", "paper", "scissors"]
        user_choice = choices[int(user_choice) - 1]
        computer_choice = random.choice(choices)

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win!")
        else:
            print("Computer wins!")

def main():
    print("Welcome to the app!")
    while True:
        print("\nOptions:")
        print("1. Rock-Paper-Scissors Game")
        print("2. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            rock_paper_scissors_game()
        elif choice == "2":
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()