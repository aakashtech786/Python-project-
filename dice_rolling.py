# Importing random module to generate random numbers
import random

# Variable to count how many times the dice is rolled
count = 0

# Infinite loop to keep asking the user until they choose to quit
while True:
    # Asking user whether they want to roll the dice
    choice = input('Roll The Dice? (y/n) : ').lower()

    # If user chooses 'y', roll the dice
    if choice == 'y':
        # Generate two random numbers between 1 and 6 (dice values)
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        # Print the dice results
        print(f'{dice1}, {dice2}')

        # Increase roll count by 1
        count = count + 1

    # If user chooses 'n', stop the game
    elif choice == 'n':
        print('Thanks for Playing!')
        print(f'You rolled the Dice {count} times')
        break  # Exit the loop

    # If input is neither 'y' nor 'n'
    else:
        print('Invalid input!!!!')

# Asking a friendly question after the game ends
n = input('Now when will you come brother to play : ')

# Final messages
print('Ok! I will wait, Thank you Again!')
print('Created by Aakash Kumar')
