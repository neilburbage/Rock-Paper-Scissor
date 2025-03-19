
import random
print("\n")
print("Rock, Paper, Scissor game.\n")
print("Game Rules:\n")
print("Rock versus Paper, then Paper wins.\n")
print("Rock versus Scissor, then Rock wins.\n")
print("Paper versus Scissor, then Scissor wins.\n")

while True:
    while True:
        print("Enter your choice:\n")
        print("1. For Rock.")
        print("2. For Paper.")
        print("3. For Scissor.\n")
        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= 3:
                break 
            else:
                print("Enter a valid choice (1, 2, or 3).")
        except ValueError:
            print("Invalid input, please enter a valid number.")

    if choice == 1: 
        choice_name = "Rock"
    elif choice == 2:
        choice_name = "Paper"
    else:
        choice_name = "Scissor"
    print("User choice is:", choice_name,"\n")
    print("Now it's the computer's turn:\n")
    computer_choice = random.randint(1,3)
    
    if computer_choice == 1: 
        computer_selects = "Rock"
    elif computer_choice == 2:
        computer_selects = "Paper"
    else:
        computer_selects = "Scissor"
    print("Computer choice is:", computer_selects,"\n")

    print(choice_name," ", "versus", " ",computer_selects)
    if choice == computer_choice:
        result = "draw"

    if (choice == 1 and computer_choice == 2):
        print("Paper wins...\n")
        result = "Paper"
    elif (choice == 2 and computer_choice == 1):
        print("Paper wins...\n")
        result = "Paper"

    if (choice == 2 and computer_choice == 3):
        print("Scissor wins...\n")
        result = "Scissor"
    elif (choice == 3 and computer_choice == 2):
        print("Scissor wins...\n")
        result = "Scissor"
    if (choice == 1 and computer_choice == 3):
        print("Rock wins...\n")
        result = "Rock"
    elif (choice == 3 and computer_choice == 1):
        print("Rock wins...\n")
        result = "Rock"
    
    if result == "draw":
        print("It's a tie!\n")
    elif result == choice_name:
        print("User wins\n")
    else:
        print("Computer wins\n")
    
    play_again = input("Do you want to play again? (Y/N): ")
    if play_again == 'n':
        print("Thank you for playing!\nBye bye!")
        break
    else:
        continue
    