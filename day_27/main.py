import tkinter

window = tkinter.Tk()
window.title("test")
window.minsize(width=500, height=300)

#label
label = tkinter.Label(text="Test label", font=("Arial", 24, "bold"))
label.pack(side="left")



window.mainloop()

