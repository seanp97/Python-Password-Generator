import random
from tkinter import *
import sys
import tkinter

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"  "k", "l", "m", "n",
"o", "p", "q",  "r", "s", "t", "u", "v", "w", "x", "y", "z"]
alphabetLen = len(alphabet)

myNewPass = []
finishedPass = ""

def generatePassword():
    passwordLength = Entry.get(passLenEnt)
    for i in range(int(passwordLength)):
        global finishedPass
        randPass = random.randrange(alphabetLen)
        myNewPass = alphabet[randPass]
        finishedPass += str(myNewPass)

    newPass = finishedPass
    passEmptyLabel.configure(text=newPass)
    myNewPass = []
    finishedPass = ""

app = Tk()
app.title("Calculator")
app.geometry("900x450")


passLabel = Label(app, text="Random Password Generator A-Z", padx=10, pady=10, font='Helvetica 14 bold')
passLabel.grid(column=0, row=0)

passLenLabel = Label(app, text="How long do you want your password to be?", padx=10, pady=10, font='Helvetica 8 bold')
passLenLabel.grid(column=0, row=1)
passLenEnt = Entry(app, bd=5)
passLenEnt.grid(column=0, row=2)
passLenBtn = Button(app, bd=5, text="Sumbit", padx=5, pady=5, command=generatePassword)
passLenBtn.grid(column=0, row=3)

passEmptyLabel = Label(app, text="", padx=10, pady=15, font='Helvetica 8 bold')
passEmptyLabel.grid(column=0, row=4)

app.mainloop()
