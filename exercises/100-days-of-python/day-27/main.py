import tkinter


def button_clicked():
    my_label.config(text=input.get())


# Window
window = tkinter.Tk()
window.title("GUI")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = tkinter.Label(text="Label", font=("Comic Helvetic", 25, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Same:
# my_label["text"] = "New Text"
# my_label.config(text ="New Text")

# Button
button = tkinter.Button(text="Click here", command=button_clicked)
button.grid(column=1, row=1)

button_2 = tkinter.Button(text="Second button")
button_2.grid(column=2, row=0)


# Entry
input = tkinter.Entry(width=10)
input.grid(column=3, row=3)


window.mainloop()
