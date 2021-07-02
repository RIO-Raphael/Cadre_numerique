import sys
import tkinter as tk

class Full_screen_window :
    def __init__(self):
        #tkinter object
        self.tk = tk.Tk()
        self.marge = 100
        self.height = self.tk.winfo_screenheight()
        self.width = self.tk.winfo_screenwidth()

        print("fen width=",self.width," | fen height=",self.height," | marge=", self.marge)
        self.tk.geometry ("{0}x{1}+0+0".format(self.width - self.marge,self.height - self.marge))

        self.tk.attributes("-fullscreen", True)
        self.tk.bind("<F11>", lambda event: self.tk.attributes("-fullscreen", not self.tk.attributes("-fullscreen")))
        self.tk.bind("<Escape>", lambda event: self.tk.attributes("-fullscreen", False))