"""Tinter practice."""

import tkinter


def button_clicked() -> None:
    """Event listener for button."""
    input_text = input.get()
    label.config(text=input_text)

window = tkinter.Tk() # create a new window.
window.title("My first GUI.") # set the GUI title
window.minsize(width=500, height=300) # set a minimum size
window.config(padx=20, pady=20) # set padding. Also possible on widgets.


label = tkinter.Label(text="I am a label.", font=("Arial", 24, "bold"))
# label["text"] = "New text."
label.config(text="New Text.")
# label.pack()
label.grid(column=0, row=0)

new_button = tkinter.Button(text="Click me, I'm new!", command=button_clicked)
new_button.grid(column=2, row = 0)

button = tkinter.Button(text="Click me!", command=button_clicked)
# button.pack()
button.grid(column=1,row=1)

input = tkinter.Entry(width=10)
# input.pack()
input.grid(column=3,row=2)

"""
Layout managers include pack(), grid(), and place().

pack() is the simplest and most commonly used layout manager. it packs widgets in a block before moving to the next block, typically one on top of the other. It is difficult to control the exact position of widgets using pack().

place(x=x,y=y) allows you to specify the exact position of widgets. It is not commonly used because it is difficult to maintain the layout when the window is resized.

grid(column=x,row=y) is the most flexible layout manager. It allows you to specify the row and column number in the grid. It is the most commonly used layout manager. It is however, relative to other widgets in the grid. So if your first item you t ry to place at column 5, row 5, it will be placed at column 0, row 0 because there are no other widgets in the grid yet. It is best practice then to place your widgets in the grid in the order you want them to appear on the screen.
"""



# window has access to .mainloop() method that keeps the program running.
# It should always be at the end of the program.
window.mainloop()


