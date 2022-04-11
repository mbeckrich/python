import tkinter as tk
from calculator import Calculator

# Window
window = tk.Tk()
window.title("Miles to KM Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

calc = Calculator()

calc.conversion_calculator()

# Label
miles_label = tk.Label(
    text="miles is equal to", font=("Mononoki Nerd Font Mono", 18)
)
miles_label.grid(column=2, row=0, padx=5, pady=0)

# show number before text=km
km_label = tk.Label(text="km", font=("Mononoki Nerd Font Mono", 18))
km_label.grid(column=2, row=1)

# Button
button = tk.Button(text="Calculate")
button.grid(column=2, row=2, pady=25)

# Input
input = tk.Entry(width=5)
input.grid(column=1, row=0)

window.mainloop()
