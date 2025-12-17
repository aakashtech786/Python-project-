# Importing random module to generate a random number
import random

# Variable to count the number of attempts
count = 0

# Generate a random number between 1 and 50
guess_numer = random.randint(1, 50)

# (Optional) Printing the guessed number for testing/debugging
print(guess_numer)

# Infinite loop until the user guesses the correct number
while True:
    try:
        # Taking user input and converting it to integer
        number = int(input('Enter number between 1 and 50 : '))

        # Increase attempt count
        count = count + 1

        # Check if the guessed number is smaller
        if number < guess_numer:
            print('It is too low!!')

        # Check if the guessed number is greater
        elif number > guess_numer:
            print('It is too high!!')

        # If the guessed number is correct
        else:
            print(f'Congratulations! You have guessed the number in {count} attempts')
            break  # Exit the loop

    # Handle invalid (non-numeric) input
    except ValueError:
        print('Enter number only!')

# Final credit message
print('Created by Aakash Coder')
