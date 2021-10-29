from constants import *
from tkinter import *
from ecdh import *
from ecdsa import *
from pointops import *


class Start:

    def __init__(self, root):

        self.root = root

        self.root.title('Analysis of Elliptic Curve Cryptography')
        self.root.geometry(screen_size)
        self.main_menu = Menu(self.root)
        self.root.config(menu=self.main_menu)

        # Creating frames
        self.point_operations_frame = Frame(self.root, width=800, height=800)
        self.point_ops = PointOps(self.point_operations_frame)

        self.ecdh_frame = Frame(self.root, width=800, height=800)
        self.ecdh = Ecdh(self.ecdh_frame)

        self.ecdsa_frame = Frame(self.root, width=800, height=800)
        self.ecdsa = Ecdsa(self.ecdsa_frame)

        self.frames = [self.point_operations_frame, self.ecdh_frame, self.ecdsa_frame]

    def start(self):
        # Creating exit
        file_menu = Menu(self.main_menu)
        self.main_menu.add_cascade(label="Actions", menu=file_menu)
        file_menu.add_command(label="Exit", command=self.root.quit)

        # Creating Encrypt menu
        encrypt_menu = Menu(self.main_menu)
        self.main_menu.add_cascade(label="Encrypt", menu=encrypt_menu)
        encrypt_menu.add_command(label="Elliptic-Curve Diffie-Hellman (ECDH)",
                                 command=lambda: self.change_frame(self.ecdh))

        encrypt_menu.add_command(label="Elliptic-Curve Digital Signature Algorithm (ECDSA)",
                                 command=lambda: self.change_frame(self.ecdsa))

        # Creating frames
        # point_operations_frame = Frame(self.root, width=800, height=800)

        # ecdsa_frame = Frame(self.root, width=500, height=800)



        '''
        # Creating Analysis menu
        analysis_menu = Menu(main_menu)
        main_menu.add_cascade(label="Analysis", menu=analysis_menu)
        analysis_menu.add_command(label="Point Operations", command=point_operations)
        '''



        # encrypt_menu.add_command(label="Elliptic-Curve Digital Signature Algorithm (ECDSA)", command=ecdsa)
        # ecdsa_label = Label(ecdsa_frame, text="Elliptic-Curve Digital Signature Algorithm").pack()

    def change_frame(self, frame):
        self.hide_all_frames()
        frame.display()

    # Hide all frames
    def hide_all_frames(self):
        length = len(self.frames)
        for i in range(length):
            self.clear_frame(self.frames[i])
            self.frames[i].pack_forget()

    def clear_frame(self, frame):
        for widgets in frame.winfo_children():
            widgets.destroy()
