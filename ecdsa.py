import tkinter as tk
import constants as cons

class Ecdsa:
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master)
        tk.Label(self.frame, text='ECDSA Page!!!').pack()
        # tk.Button(self.frame, text='Go back', command=self.go_back).pack()

    def start_page(self):
        self.frame.pack()

    def go_back(self):
        self.frame.pack_forget()
        self.app.main_page()

    def get_frame(self):
        return self.frame

'''
class Ecdsa:

    def __init__(self, frame):
        self.frame = frame

    def display(self):
        ecdsa_label = Label(self.frame, text="Elliptic-Curve Digital Signature Algorithm").pack()
        self.frame.pack(fill="both", expand=1)

    def print(self):
        pass
    '''
