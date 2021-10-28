from constants import *
from tkinter import *


class Start:

    def __init__(self, root):
        root.title('Analysis of Elliptic Curve Cryptography')
        root.geometry(screen_size)
        main_menu = Menu(root)
        root.config(menu=main_menu)
        # Creating frames
        point_operations_frame = Frame(root, width=800, height=800)
        ecdh_frame = Frame(root, width=800, height=800)
        ecdsa_frame = Frame(root, width=500, height=800)


        # Creating exit
        file_menu = Menu(main_menu)
        main_menu.add_cascade(label="Actions", menu=file_menu)
        file_menu.add_command(label="Salir", command=root.quit)

        '''
        # Creating Analysis menu
        analysis_menu = Menu(main_menu)
        main_menu.add_cascade(label="Analysis", menu=analysis_menu)
        analysis_menu.add_command(label="Point Operations", command=point_operations)

        # Creating Encrypt menu
        encrypt_menu = Menu(main_menu)
        main_menu.add_cascade(label="Encrypt", menu=encrypt_menu)
        encrypt_menu.add_command(label="Elliptic-Curve Diffie-Hellman (ECDH)", command=ecdh)
        encrypt_menu.add_command(label="Elliptic-Curve Digital Signature Algorithm (ECDSA)", command=ecdsa)

        ecdh_label = Label(ecdh_frame, text="Elliptic-Curve Diffie-Hellman algorithm").pack()
        ecdsa_label = Label(ecdsa_frame, text="Elliptic-Curve Digital Signature Algorithm").pack()
        '''

    def start(self):
        print("este es el comienzo")