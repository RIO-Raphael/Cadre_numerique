import sys
from tkinter import *
from Cadre_numerique_class import * 
from Cadre_numerique_cst import *
from PIL import Image, ImageTk

fen = Full_screen_window()

#We make an image object
photo = Image.open("aa.jpg")
ratio = photo.width/photo.height
fen_ratio = fen.width/fen.height
print ("fenetre ratio = ",fen_ratio," | ratio image = ",ratio)
if fen_ratio>ratio :
    photo = photo.resize((int(fen.height*ratio),fen.height),Image.LANCZOS)
else :
    photo = photo.resize((fen.width,int(fen.width/ratio)),Image.LANCZOS)
#Load an image in the script
img = ImageTk.PhotoImage(photo)

canvas = Canvas(fen.tk, height=fen.height, width=fen.width)
canvas.pack()

canvas.create_image(0,0,anchor=NW,image=img)
 
# label = tk.Label(fen, image=photo)
# label.pack()

# We open the window
fen.tk.mainloop()