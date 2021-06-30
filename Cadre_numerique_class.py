import sys
import tkinter as tk

class Full_screen_window :
    def __init__(self):
        #tkinter object
        self.tk = tk.Tk()
        marge = 100
        height = self.tk.winfo_screenheight() - marge
        width = self.tk.winfo_screenwidth() - marge

        print(width,height)
        self.tk.geometry ("{0}x{1}+0+0".format(width,height))

        self.tk.attributes("-fullscreen", True)
        self.tk.bind("<F11>", lambda event: self.tk.attributes("-fullscreen", not self.tk.attributes("-fullscreen")))
        self.tk.bind("<Escape>", lambda event: self.tk.attributes("-fullscreen", False))