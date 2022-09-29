from do import execute as do
from undo import execute as undo

from tkinter import *


root = Tk()
# make widgets
between_spacing = 20
inner_spacing = 5
padding_horizontal = (10,10)

L1 = Label(root, text="Click below to rename")
L1.pack(anchor=W, pady=(between_spacing,0), padx=padding_horizontal)
B1 = Button(root, text="Rename", command=do)
B1.pack(anchor=W, pady=(inner_spacing,0), padx=padding_horizontal)

L2 = Label(root, text="Click below to undo renaming")
L2.pack(anchor=W, pady=(between_spacing,0), padx=padding_horizontal)
B2 = Button(root, text="Undo rename", command=undo)
B2.pack(anchor=W, pady=(inner_spacing,between_spacing), padx=padding_horizontal)

# show
root.mainloop()
