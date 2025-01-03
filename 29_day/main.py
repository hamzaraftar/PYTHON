from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20 , pady=20)
canves = Canvas(height=200 , width=200)
logo_img  = PhotoImage(file='logo.png')
canves.create_image(100 , 100  , image = logo_img)
canves.pack()


window.mainloop()