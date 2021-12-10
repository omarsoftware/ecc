import tkinter as tk
import constants as cons
import ecmath as ec
import random as rand
from PIL import Image, ImageTk


class Associativity:
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master)

        self.title = tk.Label(self.frame, text='Propiedad de Asociatividad', font='Helvetica 16 bold')
        self.title.pack(fill="x")


    def start_page(self):
        self.frame.grid(column=0, row=0, sticky="NWES")

    def go_back(self):
        self.frame.pack_forget()
        self.app.main_page()

    def get_frame(self):
        return self.frame
