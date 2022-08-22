from tkinter import *

root = Tk()

def crypt(n):
    msg = Tk()
    if n == "encrypt":
        msg.title("Encrypt Message")
    elif n == "decrypt":
        msg.title("Decrypt Message")
    lb = Label(msg, text="Enter your message")
    inp = Entry(msg, width=50)
    lb.grid(row=0, column=0)
    inp.grid(row=1, column=0)
    def work(s):
        don = Tk()
        inp.delete(0, END)
        done = ''.join([ s[x:x+2][::-1] for x in range(0, len(s), 2) ])
        if n == "encrypt":
            don.title("Encrypted Message")
        elif n == "decrypt":
            don.title("Decrypted Message")
        don.geometry("250x150+0+0")
        l = Label(don , text=done)
        l.grid(row=0, column=0)
        don.mainloop()
    send = Button(msg, text="Send", padx=15, pady=6, command=lambda: work(inp.get()))
    send.grid(row=2, column=0)
    msg.mainloop()

def box():
    te = Label(root, text="How do you wish to use this App")
    ebu = Button(root, text="encrypt", padx=15, pady=6 , command=lambda:crypt('encrypt'))
    debu = Button(root, text="decrypt", padx=16, pady=6, command=lambda: crypt('decrypt'))
    te.grid(row=0, column=0, columnspan=4)
    ebu.grid(row=1, column=0)
    debu.grid(row=1, column=1,columnspan=2)
    root.mainloop()

box()