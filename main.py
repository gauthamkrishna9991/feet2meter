"""
    A simple tkinter program to convert feet to metres.
    Copyright (C) 2019 by Goutham Krishna K V

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048*value*10000.0 + 0.5)/10000.0)
    except ValueError:
        pass
# DEFINE ROOT WINDOW
root = Tk()
root.title("Convert feet to meters")
mainFrame = ttk.Frame(root, padding="3 3 12 12")
mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))
mainFrame.columnconfigure(0, weight=1)
mainFrame.rowconfigure(0, weight=1)
# DEFINE STRING VARIABLES FOR TEXT
feet = StringVar()
meters = StringVar()
feet_entry = ttk.Entry(mainFrame, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainFrame, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainFrame, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainFrame, text="Feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainFrame, text="is Equivalent to ").grid(column=1, row=2, sticky=E)
ttk.Label(mainFrame, text="Meter").grid(column=3, row=2, sticky=W)

for child in mainFrame.winfo_children():
    child.grid_configure(padx=5, pady=5)
feet_entry.focus()
root.bind('<Return>', calculate)
root.mainloop()