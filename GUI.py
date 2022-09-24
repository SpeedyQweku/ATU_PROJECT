

# Importing the moudle tkinter
from tkinter import *


root = Tk() # Displaying the root window


def crypt(n): # The Function for the encryption

    msg = Tk() # Displaying the msg window

    if n == "encrypt":
        msg.title("Encrypt Message")
    elif n == "decrypt":
        msg.title("Decrypt Message")
    Label_2 = Label(msg, text="Enter your message") # Creating a Label Widget
    Entry_1 = Entry(msg, width=50) # Creating a Entry Widget

    Label_2.grid(row=0, column=0) # Positioning it in the msg window
    Entry_1.grid(row=1, column=0) # Positioning it in the msg window


    def work(s): # Function work()

        don = Tk() # Displaying the don window

        Entry_1.delete(0, END)
        done = ''.join([ s[x:x+2][::-1] for x in range(0, len(s), 2) ])#this is where the encryption is done
        if n == "encrypt":
            don.title("Encrypted Message")
        elif n == "decrypt":
            don.title("Decrypted Message")
        don.geometry("250x150+0+0")

        Label_3 = Label(don , text=done) # Creating a Label Widget

        Label_3.grid(row=0, column=0) # Positioning it in the don window

        don.mainloop() # Keeping the don display at loop


    send = Button(msg, text="Send", padx=15, pady=6, command=lambda: work(Entry_1.get())) # Creating a Button Widget

    send.grid(row=2, column=0) # Positioning it in the msg window

    msg.mainloop() # Keeping the don display at loop


def box(): # Function box()

    Label_1 = Label(root, text="How do you wish to use this App") # Creating a Label Widget
    encrypt = Button(root, text= "encrypt", padx=15, pady=6 , command=lambda: crypt('encrypt')) # Creating a Button Widget
    decrypt = Button(root, text= "decrypt", padx=16, pady=6, command=lambda: crypt('decrypt')) # Creating a Button Widget

    Label_1.grid(row=0, column=0, columnspan=4) # Positioning it in the root window
    encrypt.grid(row=1, column=0) # Positioning it in the root window
    decrypt.grid(row=1, column=1,columnspan=2) # Positioning it in the root window

    root.mainloop() # Keeping the don display at loop

""" Calling the function box(), this function is going to call the crypt()
function and it with call the work() function """
box()
