from tkinter import *        # Import all Tkinter classes for GUI creation
import random                # Import random module to generate random values

# Create the main application window
window = Tk()
window.title("Akash Dice")   # Set the window title
window.geometry("500x400")   # Set window size (width x height)

# Label to display the dice symbols
# Uses a large bold Helvetica font
l1 = Label(
    window,
    font=("helventica", 250, 'bold'),
    text="",              # Initially empty (dice will appear after button click)
    bd=10                 # Border width
)
# l1.pack()               # Not packed initially (shown only after rolling dice)

# Label to display the author's name
l2 = Label(
    window,
    font=('helventica'),
    text='Aakash kumar'
)
l2.pack()                  # Display the label in the window

# Function that runs when the button is clicked
def rolldice():
    # Unicode characters for dice faces (1 to 6)
    dice = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    
    # Randomly select two dice faces and display them
    l1.configure(text=f'{random.choice(dice)}{random.choice(dice)}')
    
    # Show the dice label in the window
    l1.pack()

# Button to roll the dice
B1 = Button(
    window,
    font=('helventica', 25, 'bold'),
    text='roll dice',
    command=rolldice,     # Calls rolldice() when clicked
    bg='yellow',          # Button background color
    fg='red'              # Button text color
)
B1.pack()                 # Display the button

# Start the Tkinter event loop
window.mainloop()
