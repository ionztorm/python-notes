"""Miles to Kilometers Converter."""

import tkinter as tk

# =========[Events]==============

def calc_km() -> None:
    """Convert miles to kilometers."""
    result = float(input_miles.get()) * 1.60934
    label_result.config(text=round(result,2))
    input_miles.delete(0,tk.END)

# =========[Window]==============

window = tk.Tk()
window.title("Convert miles to kilometers.")
window.minsize(width=200, height=100)
window.config(padx=15,pady=15)

# =========[Top Row]=============

input_miles = tk.Entry(width=15)
input_miles.grid(column=2, row=1)

label_miles = tk.Label(text="miles")
label_miles.grid(column=3,row=1)

# =========[Middle Row]==========

label_equal_to = tk.Label(text="is equal to")
label_equal_to.grid(column=1,row=2)

label_result = tk.Label(text=0)
label_result.grid(column=2,row=2)

label_km = tk.Label(text="km")
label_km.grid(column=3, row=2)

# =========[Bottom Row]==========

button_calculate = tk.Button(text="Calculate", command=calc_km)
button_calculate.grid(column=2,row=3)

# =========[Keep Window Open]====

window.mainloop()
