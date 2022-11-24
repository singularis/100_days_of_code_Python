from tkinter import *

window = Tk()
window.title("test")
window.minsize(width=500, height=300)

#label
label = Label(text="Test label", font=("Arial", 24, "bold"))
label.pack()

def button_clicked():
    print("Clicked")
    button = input.get()
    label.config(text=button)
    return button


button = Button(text="Click", command=button_clicked)
button.pack()

input = Entry()
input.pack()


window.mainloop()

