import random
emojis = {
    'r': '🪨',
    'p': '📃',
    's': '✂️'
}
choices = ['r', 'p', 's']


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
            choice == 'r' and comp_choice == 's' or \
            choice == 's' and comp_choice == 'p' or \
            choice == 'p' and comp_choice == 'r':
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
