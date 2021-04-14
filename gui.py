# This file contains the Graphical User Interface for the chat bot.
# The GUI is made using Tkinter, image functionalities from Pillow are used.
# The chat() function from 'chatbot.py' is imported to get bot's appropriate response to user input

from tkinter import *
from chatbot import chat
from PIL import ImageTk, Image


# Create unresizable window and title it "Interactive Chatbot"
root = Tk()
root.resizable(0,0)
root.title("Interactive Chatbot")


# Create label for name of the bot, add the name, and place it on the window
name = Label(root, width = 39, height = 3, font = ("Helvetica", 16, "bold italic"))
name.config(text = "Justin Trudeau")
name.grid(row = 0, column = 0, columnspan = 2)


# Load image from specified path, resize it to fit top-left of window. Then, create a label with the image and insert it in the window
path = "images/justin.jpg"
img = Image.open(path).resize((100,80), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
header = Label(root, image = img)
header.grid(row = 0, column = 0, sticky = 'W')


# Create main Text box containing all the chat messages.
# Create Scrollbar for the text box and bind its function to the text box's yview.
# Show initial message for user to get started/quit program
text = Text(root, width = 60, height = 30, padx = 5, font = ("Times", 13, "bold"))
text.grid(row = 1, column = 0, columnspan = 2)
scroll = Scrollbar(root, command = text.yview())
text['yscrollcommand'] = scroll.set
scroll.place(relx = 0.97, rely = 0.12, height = 572)
text.insert(END, "Enter your message(type 'quit' to exit):\n")


# This method takes input from the entry box, calls the chat() function from 'chatbot.py' and prints both the input and the bot's response in the text box
# If user chooses to quit, the window is shut and the program is terminated.
def present_and_clear(event = '<Return>'):
    out = "You: " + msg.get()
    text.insert(END, "\n" + out)
    if msg.get().lower() == "quit":
        root.destroy()
    else:
        text.insert(END,"\n" + "Justin: " + chat(msg.get()))
        text.see(END)
        msg.delete(0, 'end')


# Create a button that is used to enter the input and call present_and_clear().
# The 'Enter' key is also bound to the function so that it performs the same action.
send = Button(root, text = "Send", command = present_and_clear, font = ("Times", 14), bd = 4)
root.bind('<Return>', lambda x: present_and_clear())
send.grid(row = 2, column = 1)

# Create Empty string to store user input from Entry box.
user_inp = ""

# Create Entry box for user input and place it on the window.
# Set focus to entry box (cursor placement on startup)
msg = Entry(root, width = 80, textvariable = user_inp, bg = 'grey60', bd = 3)
msg.grid(row = 2, column = 0)
msg.focus_set()


root.mainloop()
