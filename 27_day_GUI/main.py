import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500 ,height=500)


my_lable = tkinter.Label(text="I am a label",font=("Arial " , 24 ,"bold"))
my_lable.pack()












window.mainloop()