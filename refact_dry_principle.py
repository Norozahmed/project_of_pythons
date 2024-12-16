import random

ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'
emojis = {
    ROCK: '🪨',
    PAPER: '📃',
    SCISSORS: '✂️'
}
choices = tuple(emojis.keys())


def get_user_choice():
    while True:
        choice = input("Rock, paper, or scissors? (r/p/s): ").lower()
        if choice in choices:
            return choice
        else:
            print('Invalid choice!')


def display_choices(choice, comp_choice):
    print(f"You chose {emojis[choice]}")
    print(f"Computer chose {emojis[comp_choice]}")


def determine_winner(choice, comp_choice):
    if choice == comp_choice:
        print('Tie!')
    elif  \
            choice == ROCK and comp_choice == SCISSORS or \
            choice == SCISSORS and comp_choice == PAPER or \
            choice == PAPER and comp_choice == ROCK:
        print('You Win')
    else:
        print('You Lost to Computer!')


def play_game():
    while True:
        choice = get_user_choice()

        comp_choice = random.choice(choices)

        display_choices(choice, comp_choice)

        determine_winner(choice, comp_choice)

        will_continue = input('Continue? (y/n): ').lower()
        if will_continue == 'n':
            break


play_game()
