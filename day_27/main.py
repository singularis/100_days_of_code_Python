from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=150)


def convert():
    km = entry.get()
    miles_converted = round(float(km) * 1.60934, 3)
    result_label.config(text=miles_converted)


is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

entry = Entry(width=10)
entry.focus()
entry.insert(END, string="0")

entry.grid(column=1, row=0)

ml_label = Label(text="Miles")
ml_label.grid(column=2, row=0)

result_label = Label(text="0")
result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

button = Button(text="Convert", command=convert)
button.grid(column=1, row=2)

window.config(padx=20, pady=20)
window.mainloop()
