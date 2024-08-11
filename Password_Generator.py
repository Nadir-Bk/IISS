import tkinter as tk
import random
import string


def pass_4():
    passcode = ""
    # To Generate Passcode
    characters = ""
    characters += string.ascii_letters + string.digits + string.punctuation
    for i in range(4):
        passcode += str(random.choice(characters))
    # To Display Passcode
    l_pass = tk.Label(text='Your Passcode:', font=("arial", 12, "bold"))
    l_pass.place(x=240, y=200)
    pass4 = tk.Label(text=passcode, font=("arial", 12, "bold"), width=8)
    pass4.place(x=260, y=225)


def pass_6():
    passcode = ""
    # To Generate Passcode
    characters = ""
    characters += string.ascii_letters + string.digits + string.punctuation
    for i in range(6):
        passcode += str(random.choice(characters))
    # To Display Passcode
    l_pass = tk.Label(text='Your Passcode:', font=("arial", 12, "bold"))
    l_pass.place(x=240, y=200)
    pass6 = tk.Label(text=passcode, font=("arial", 12, "bold"), width=8)
    pass6.place(x=260, y=225)


def pass_8():
    passcode = ""
    # To Generate Passcode
    characters = ""
    characters += string.ascii_letters + string.digits + string.punctuation
    for i in range(8):
        passcode += str(random.choice(characters))
    # To Display Passcode
    l_pass = tk.Label(text='Your Passcode:', font=("arial", 12, "bold"))
    l_pass.place(x=240, y=200)
    pass8 = tk.Label(text=passcode, font=("arial", 12, "bold"))
    pass8.place(x=265, y=225)


window = tk.Tk()    # Defines the Window
window.resizable(False, False)
window.title("Random Password Generator")
window.geometry("600x500+400+100")  # Size of Window

# Labels Defined
hi = tk.Label(text='Random Password Generator', font=("arial", 15, "bold", "underline"))
click = tk.Label(text='Click to Generate', font=("arial", 10, "bold"))

# Labels Placed
hi.place(x=170, y=25)
click.place(x=248, y=100)

# Buttons Defined
p4 = tk.Button(text="4-Digit Password", font=("arial", 10), command=pass_4)
p6 = tk.Button(text="6-Digit Password", font=("arial", 10), command=pass_6)
p8 = tk.Button(text="8-Digit Password", font=("arial", 10), command=pass_8)

# Buttons Placed
p4.place(x=100, y=150)
p6.place(x=250, y=150)
p8.place(x=400, y=150)

window.mainloop()   # Keeps the Window Running
