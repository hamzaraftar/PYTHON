from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500 ,height=500)


my_lable = Label(text="I am a label",font=("Arial " , 24 ,"bold"))
my_lable.pack()

my_lable['text'] = "New Text"
my_lable.config(text="New Text")


def button_click():
    new_text = input.get()

    # print("i got click")
    my_lable.config(text=new_text)


button = Button(text="Click me" ,command=button_click)
button.pack()

input = Entry()
input.pack()
print(input.get())














window.mainloop()