import random  # For selecting a random sentence from the list
import time    # For calculating typing start and end time

# Function to calculate typing mistakes
def mistake(computer_text, user_text):
    error = 0  # Initialize error count
    for i in range(len(computer_text)):  # Loop through each character in the original text
        try:
            if (computer_text[i] != user_text[i]):  # Compare each character
                error += 1  # Increment error if characters don't match
        except:
            error += 1  # If user_text is shorter, count remaining as errors
    return error  # Return total errors


# Function to calculate typing speed
def speed(start_time, end_time, user_text):
    delay = end_time - start_time  # Total time taken to type
    delay_round = round(delay, 2)  # Round time to 2 decimal places
    speed = len(user_text) / delay_round  # Characters typed per second
    speed_round = round(speed)  # Round speed to nearest whole number
    return speed_round  # Return the typing speed


while True:
    conf = input('Do you want to practice (yes/no) : ').lower()
    if conf == 'yes':
        
        text = [
            'The sun rises in the east.', 
            'I love learning Python.', 
            'Practice makes a person perfect. Typing fast requires focus.', 
            'Typing speed improves with daily practice. Programming needs logical thinking.', 
            'Python is used in web development, data science, and automation. Accuracy is important.', 
            'This code is written by Akash.'
        ]
        print()
        print('***************TYPING SPEED TEST***************')  # Display title
        print()
        computer_text = random.choice(text)  # Randomly select a sentence for typing
        print(computer_text)  # Display sentence for user
        print()
        print()

        start_time = time.time()  # Record start time
        user_text = input("Enter the Above text :")  # User types the sentence
        end_time = time.time()  # Record end time

        total_error = mistake(computer_text, user_text)  # Calculate total mistakes
        Net_speed = speed(start_time, end_time, user_text)  # Calculate typing speed

        # Display results
        print()
        print('Result:')
        print('Total :', len(computer_text), 'Charactares(including space,.)')  # Total characters
        print('Total typing Error : ', total_error)  # Total mistakes
        print('Speed :', Net_speed, 'chars/sec')  # Typing speed in characters per second

        print('--------------------------------------')
    
    elif conf == 'no':
        break

    else:
        print('❌ invalid input!!')



print()
print('____________THE END ________________')


print('Thank you !')

print('This is coded by Akash coder.')