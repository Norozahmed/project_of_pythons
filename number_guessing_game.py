import random
print("Number Guessing Game")
number = random.randint(1, 100)
while True:
    try:
        guess = int(input("Enter your guess: "))
        if guess < number:
            print("Too low")
        elif guess > number:
            print("Too high")
        else:
            print("Congrats you guessed the correct number.")
            break
    except ValueError:
        print('Please enter a valid number')



