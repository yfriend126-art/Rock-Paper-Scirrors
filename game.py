import random
print("Welcome to Rock, Paper, Scissors!")
print("Rules:")
print("  - Rock beats scissors")
print("  - Paper beats rock")
print("  - Scissors beats paper")

choose=("rock", "paper", "scissors")
while True:
    print("Choose your option:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    user_choice=input("Enter the number of your choice (1-3): ")
    user_choice=int(user_choice)-1
    computer_choice=random.randint(0,2)
    if user_choice==computer_choice:
        print("It's a tie!")
    elif user_choice==1 and computer_choice==2:
        print("You win! Rock beats scissors.")
    elif user_choice==2 and computer_choice==0:
        print("You win! Paper beats rock.")
    elif user_choice==0 and computer_choice==1:
        print("You win! Scissors beats paper.")
    else:
        print("Invalid choice. Please try again.")
        break
