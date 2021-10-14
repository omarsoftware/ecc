import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from tkinter import *
from constants import *
from ecmath import *

root = Tk()
root.title('Analysis of Elliptic Curve Cryptography')
root.geometry(screen_size)

main_menu = Menu(root)
root.config(menu=main_menu)

# Creating frames
point_operations_frame = Frame(root, width=800, height=800)
ecdh_frame = Frame(root, width=800, height=800)
ecdsa_frame = Frame(root, width=500, height=800)

def update(a, b, frame):
    for widget in frame.winfo_children():
        widget.destroy()
    graph_frame = Frame(frame, width=500, height=500, borderwidth=2, bg="YELLOW")
    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(111)

    y, x = np.ogrid[-5:5:100j, -5:5:100j]
    ax.contour(x.ravel(), y.ravel(), pow(y, 2) - pow(x, 3) - x * a - b, [0])
    ax.grid()

    canvas = FigureCanvasTkAgg(fig, master=frame)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack() 


def point_operations():
    hide_all_frames()
    top_frame = Frame(point_operations_frame, width=100, height=100, borderwidth=2, bg="RED")
    top_frame.grid(row=0, column=0)
    left_frame = Frame(point_operations_frame, width=500, height=500, borderwidth=2, bg="BLUE")
    left_frame.grid(row=1, column=0)
    right_frame = Frame(point_operations_frame, width=500, height=500, borderwidth=2, bg="GREEN")
    graph_frame = Frame(right_frame, width=500, height=500, borderwidth=2, bg="YELLOW")
    right_frame.grid(row=1, column=1)

    #point_operations_label = Label(top_frame, text="Analysis of Elliptic Curves Point Operations").pack()
    #right_frame_title = Label(right_frame, text="Graph")
    #left_frame_title = Label(left_frame, text="Parameters")

    label_a = Label(left_frame, text= "y^2 = x^3 + ")
    #label_a.grid(row=0, column=0)
    label_a.pack(side=LEFT)

    entry_a = Entry(left_frame, width=3)
    entry_a.insert(END, "-1")
    #entry_a.grid(row=0, column=0)
    entry_a.pack(side=LEFT)

    label_b = Label(left_frame, text="x + ")
    # label_a.grid(row=0, column=0)
    label_b.pack(side=LEFT)

    entry_b = Entry(left_frame, width=3)
    entry_b.insert(END, "1")
    # entry_a.grid(row=0, column=0)
    entry_b.pack(side=LEFT)

    update_graph = Button(master=left_frame, text='Update', command=lambda: update(int(entry_a.get()), int(entry_b.get()), right_frame))
    update_graph.pack()

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