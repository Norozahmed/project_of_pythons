import random
# playing = True
while True:
    choice = input("Roll the Dice? (y/n)")
    if choice == "y":
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"({die1}, {die2})")
    elif choice == 'n':
        print("Thank You for playing!")
        break
    else:
        print("Invalid choice")

