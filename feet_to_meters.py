from tkinter import *
from tkinter import ttk

# called when a user presses the Calculate button or hits the Return key. It performs the feet to meters calculation.
# 1 feet = 0.3048 m
# 1 manzana = 0,698896 ha


def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass


root = Tk()
root.title("Feet to Meters")

# The widget Frame allows some features like general bgcolor for other widgets if this one on the frame is changed
# paddings correspond to left, top, right and bottom
mainframe = ttk.Frame(root, padding="3 3 12 12")
# place the frame corner con col and row 0,0, sticky goes for changing size while user resizing the window.
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Creating an entry
# Define what will receive, in this case a String Variable
feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))


# command attribute will call the calculate function.
ttk.Button(mainframe, text="Calculate", command=calculate).grid(
    column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
# The result of calling the function Calculate, will be visualize over this label.
meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

# Select all the children widgets inside the mainframe parent
for child in mainframe.winfo_children():
    # on every child, configure the grid to add padding on 4 sides of the cell
    child.grid_configure(padx=5, pady=5)
# Tells Tk to put the focus on our entry widget. That way, the cursor will start in that field
feet_entry.focus()
# Tells Tk that if a user presses the Return key (Enter on Windows), it should call our calculate routine, the same as if they pressed the Calculate button.
root.bind("<Return>", calculate)

root.mainloop()
