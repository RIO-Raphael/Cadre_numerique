import sys
from tkinter import *
from Cadre_numerique_class import * 
from Cadre_numerique_fct import * 
from Cadre_numerique_cst import *
from PIL import Image, ImageTk

fen = Full_screen_window()

#We make an image object
photo = Image.open("aa.jpg")

#resize
photo = resize_fit_to_screen(fen, photo)

#Load an image in the script
img = ImageTk.PhotoImage(photo)

canvas = Canvas(fen.tk, height=fen.height, width=fen.width)
canvas.pack()

canvas.create_image(0,0,anchor=NW,image=img)
 
# label = tk.Label(fen, image=photo)
# label.pack()

# We open the window
# fen.tk.mainloop()