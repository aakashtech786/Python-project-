import random

emojis = {'r':'🪨','p':'📜','s':'✂️'}
choices = ('r','p','s')

while True:
    user_choice = input('Rock, paper, or scissors (r/p/s) : ').lower()
    if user_choice not in choices:
        print('Invalid Choice!!!!')
        continue
    
    computer_choice = random.choice(choices)
    print(f'You chose {emojis[user_choice]}')
    print(f'Computer chose {emojis[computer_choice]}') 

    if (user_choice == 'p' and computer_choice == 's') or \
       (user_choice=='r' and computer_choice == 'p') or \
       (user_choice == 's' and computer_choice == 'r') :
        print('You are the winner!')
    elif user_choice == computer_choice :
        print('Ties!')
    else:
        print('you lose!')

    user_opinion = input('Do you want play again? (y/n) : ').lower()

    if user_opinion != 'y':
        break
print('Thank you for Playing!')
print('Created by Akash coder.')

