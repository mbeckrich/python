import tkinter as tk


def conversion_calculator():
    km = 1.6
    km *= float(input.get())
    return km_label.config(text=f"{round(km, 2)} km")


# Window
window = tk.Tk()
window.title("Miles to KM Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

# Labels
miles_label = tk.Label(
    text="miles is equal to", font=("Mononoki Nerd Font Mono", 18)
)
miles_label.grid(column=2, row=0, padx=5, pady=0)

km_label = tk.Label(
    text="0 km",
    font=("Mononoki Nerd Font Mono", 18),
)
km_label.grid(column=2, row=1)

# Input
input = tk.Entry(width=5)
input.grid(column=1, row=0)
input.insert(0, "0")

# Button
button = tk.Button(text="Calculate", command=conversion_calculator)
button.grid(column=2, row=2, pady=25)

window.mainloop()
