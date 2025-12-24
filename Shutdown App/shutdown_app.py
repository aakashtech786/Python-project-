from tkinter import *              # Import all Tkinter GUI components
import os                           # Import OS module to execute system commands

def restart():                      # Define function to restart the system
    os.system('shutdown /r /t 1')   # Run Windows restart command with 1-second delay
              
def restart_time():                 # Define function to restart system after delay
    os.system('shutdown /r /t 15')  # Restart system after 15 seconds

def logout():                       # Define function to log out current user
    os.system('shutdown -l')        # Execute logout command

def shutdown():                     # Define function to shut down the system
    os.system('shutdown /s /t 1')   # Shut down system after 1 second


main_win = Tk()                     # Create the main Tkinter window
main_win.title('Akasha Shutdown App')  # Set the title of the window
main_win.iconbitmap('shutdown.ico')    # Set the window icon
main_win.geometry('500x500')         # Set window size to 500x500 pixels
main_win.config(bg='#6F6F6F')        # Change window background color


r_button = Button(                  # Create Restart button widget
    main_win,                       # Set parent window
    text='Restart',                 # Text displayed on button
    font=("Arial",20,"bold"),        # Font type, size, and style
    command=restart                 # Function called when button is clicked
)
r_button.place(x=150,y=60,height=50,width=200)  # Set button position and size
r_button.config(bd=7,bg="#C6BDBD",fg="#070707") # Set button border, background & text color


rt_button = Button(                 # Create Restart Time button widget
    main_win,                       # Set parent window
    text='Restart Time',             # Text displayed on button
    font=("Arial",20,"bold"),        # Font settings
    command=restart_time             # Function executed on click
)
rt_button.place(x=150,y=120,height=50,width=200) # Position the button
rt_button.config(bd=7,bg="#C6BDBD",fg="#070707")  # Style the button


lg_button = Button(                 # Create Log-Out button widget
    main_win,                       # Set parent window
    text='Log-Out',                  # Button label text
    font=("Arial",20,"bold"),        # Font settings
    command=logout                   # Function executed on click
)
lg_button.place(x=150,y=180,height=50,width=200) # Position the button
lg_button.config(bd=7,bg="#C6BDBD",fg="#070707")  # Style the button


st_button = Button(                 # Create Shutdown button widget
    main_win,                       # Set parent window
    text='Shutdown',                 # Button label text
    font=("Arial",20,"bold"),        # Font settings
    command=shutdown                 # Function executed on click
)
st_button.place(x=150,y=240,height=50,width=200) # Position the button
st_button.config(bd=7,bg="#C6BDBD",fg="#070707")  # Style the button


L = Label(main_win,text='Created by Akash Coder.') # Create label widget
L.place(x=100,y=360)                               # Set label position
L.config(bg="#D8D6CB",height=1,width=40,fg="#1A1617",font=('Arial',10,'bold'))  
                                                   # Set label background, size, color & font


main_win.mainloop()              # Start the Tkinter event loop and display window
