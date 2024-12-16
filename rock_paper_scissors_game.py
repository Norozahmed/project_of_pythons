import random
emojis = {
    'r': '🪨',
    'p': '📃',
    's': '✂️'
}
choices = ['r', 'p', 's']

while True:
    choice = input("Rock, paper, or scissors? (r/p/s): ").lower()
    if choice not in choices:
        print('Invalid choice!')
        continue

    comp_choice = random.choice(choices)

    print(f"You chose {emojis[choice]}")
    print(f"Computer chose {emojis[comp_choice]}")

    if choice == comp_choice:
        print('Tie!')
    elif  \
            choice == 'r' and comp_choice == 's' or \
            choice == 's' and comp_choice == 'p' or \
            choice == 'p' and comp_choice == 'r':
        print('You Win')
    else:
        print('You Lost to Computer!')

    will_continue = input('Continue? (y/n): ').lower()
    if will_continue == 'n':
        break
