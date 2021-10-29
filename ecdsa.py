from ecmath import *
from tkinter import *


class Ecdsa:

    def __init__(self, frame):
        self.frame = frame

    def display(self):
        ecdsa_label = Label(self.frame, text="Elliptic-Curve Digital Signature Algorithm").pack()
        self.frame.pack(fill="both", expand=1)

    def print(self):
        pass
