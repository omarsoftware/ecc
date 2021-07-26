import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
from tkinter import *
from constants import *

root = Tk()
root.title('Analysis of Elliptic Curve Cryptography')
root.geometry(screen_size)

main_menu = Menu(root)
root.config(menu=main_menu)

# Creating frames
point_operations_frame = Frame(root, width=500, height=500)
ecdh_frame = Frame(root, width=500, height=500)
ecdsa_frame = Frame(root, width=500, height=500)

point_operations_label = Label(point_operations_frame, text="Analysis of Elliptic Curves Point Operations").pack()
def point_operations():
    hide_all_frames()
    '''
    a = -1
    b = 1
    y, x = np.ogrid[-5:5:100j, -5:5:100j]
    plt.contour(x.ravel(), y.ravel(), pow(y, 2) - pow(x, 3) - x * a - b, [0])        
    plt.grid()
    plt.show()
    '''
    fig = Figure(figsize=(5, 5), dpi=100)
    y = [i**2 for i in range(101)]
    plot1 = fig.add_subplot(111)
    plot1.plot(y)
    canvas = FigureCanvasTkAgg(fig, master=point_operations_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas, point_operations_frame)
    toolbar.update()
    point_operations_frame.pack(fill="both", expand=1)


ecdh_label = Label(ecdh_frame, text="Elliptic-Curve Diffie-Hellman algorithm").pack()
def ecdh():
    hide_all_frames()
    ecdh_frame.pack(fill="both", expand=1)

ecdsa_label = Label(ecdsa_frame, text="Elliptic-Curve Digital Signature Algorithm").pack()
def ecdsa():
    hide_all_frames()
    ecdsa_frame.pack(fill="both", expand=1)


#Creating exit
file_menu = Menu(main_menu)
main_menu.add_cascade(label="Actions", menu=file_menu)
file_menu.add_command(label="Salir", command=root.quit)

#Creating Analysis menu
analysis_menu = Menu(main_menu)
main_menu.add_cascade(label="Analysis", menu=analysis_menu)
analysis_menu.add_command(label="Point Operations", command=point_operations)

#Creating Encrypt menu
encrypt_menu = Menu(main_menu)
main_menu.add_cascade(label="Encrypt", menu=encrypt_menu)
encrypt_menu.add_command(label="Elliptic-Curve Diffie-Hellman (ECDH)", command=ecdh)
encrypt_menu.add_command(label="Elliptic-Curve Digital Signature Algorithm (ECDSA)", command=ecdsa)

#Hide all frames
def hide_all_frames():
    point_operations_frame.pack_forget()
    ecdh_frame.pack_forget()
    ecdsa_frame.pack_forget()




root.mainloop()