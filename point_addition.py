import tkinter as tk
import ecdraw as draw
import constants as cons
import ecmath as ec
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(1)
from PIL import Image, ImageTk


class PointAddition:
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master)

        self.title = tk.Label(self.frame, text='Suma de Puntos', font='Helvetica 16 bold')
        self.title.pack(fill="x")

        self.elliptic_curve = None
        self.p = None
        self.q = None
        self.selected_points = None

        # ///////////// Begin Elliptic Curve /////////////
        self.ec_frame = tk.Frame(self.frame)
        self.ec_title = tk.Label(self.ec_frame)
        self.ec_gen_eq = tk.StringVar()
        self.ec_gen_eq_label = tk.Label(self.ec_frame)

        self.ec_a_frame = tk.Frame(self.frame)
        self.ec_a_label = tk.Label(self.ec_a_frame)
        self.ec_a_entry = tk.Entry(self.ec_a_frame)

        self.ec_b_frame = tk.Frame(self.frame)
        self.ec_b_label = tk.Label(self.ec_b_frame)
        self.ec_b_entry = tk.Entry(self.ec_b_frame)

        self.ec_q_frame = tk.Frame(self.frame)
        self.ec_q_label = tk.Label(self.ec_q_frame)
        self.ec_q_entry = tk.Entry(self.ec_q_frame)

        self.ec_ready_frame = tk.Frame(self.frame)
        self.ec_ready_button = tk.Button(self.ec_ready_frame)
        self.ec_edit_button = tk.Button(self.ec_ready_frame)
        self.ec_load_ok = Image.open(cons.check_path)
        self.ec_resized = self.ec_load_ok.resize(cons.x_and_check_size, Image.ANTIALIAS)
        self.ec_new_pic_ok = ImageTk.PhotoImage(self.ec_resized)
        self.ec_image_ok = tk.Label(self.ec_ready_frame, image=self.ec_new_pic_ok)

        self.ec_error_frame = tk.Frame(self.frame)
        self.ec_load_err = Image.open(cons.x_path)
        self.ec_resized_err = self.ec_load_err.resize(cons.x_and_check_size, Image.ANTIALIAS)
        self.ec_new_pic_err = ImageTk.PhotoImage(self.ec_resized_err)
        self.ec_image_err = tk.Label(self.ec_error_frame, image=self.ec_new_pic_err)
        self.ec_err_txt = tk.StringVar()
        self.ec_err_label = tk.Label(self.ec_error_frame)

        self.ec_set()
        # ///////////// End Elliptic Curve /////////////

        self.space1 = tk.Label(self.frame, text=" ")
        self.space1.pack()

        # ///////////// Begin Plot1 ///////////
        self.plot1_frame = tk.Frame(self.frame)
        self.plot1_title = tk.Label(self.plot1_frame)

        self.plot1_graph_frame = tk.Frame(self.plot1_frame)
        self.plot1_button = tk.Button(master=self.plot1_graph_frame,
                                      command=self.plot1_graph,
                                      height=2,
                                      width=20,
                                      text="Seleccionar Puntos")

        self.plot1_p_frame = tk.Frame(self.frame)
        self.plot1_p_label = tk.Label(self.plot1_p_frame)
        self.plot1_p_val_str = tk.StringVar()
        self.plot1_p_val_label = tk.Label(self.plot1_p_frame, textvariable=self.plot1_p_val_str)

        self.plot1_q_frame = tk.Frame(self.frame)
        self.plot1_q_label = tk.Label(self.plot1_q_frame)
        self.plot1_q_val_str = tk.StringVar()
        self.plot1_q_val_label = tk.Label(self.plot1_q_frame, textvariable=self.plot1_q_val_str)

        self.plot1_ready_frame = tk.Frame(self.plot1_frame)
        self.plot1_ready_button = tk.Button(self.plot1_ready_frame)
        self.plot1_edit_button = tk.Button(self.plot1_ready_frame)
        self.plot1_load_ok = Image.open(cons.check_path)
        self.plot1_resized = self.plot1_load_ok.resize(cons.x_and_check_size, Image.ANTIALIAS)
        self.plot1_new_pic_ok = ImageTk.PhotoImage(self.plot1_resized)
        self.plot1_image_ok = tk.Label(self.plot1_ready_frame, image=self.plot1_new_pic_ok)

        self.plot1_error_frame = tk.Frame(self.plot1_frame)
        self.plot1_load_err = Image.open(cons.x_path)
        self.plot1_resized_err = self.plot1_load_err.resize(cons.x_and_check_size, Image.ANTIALIAS)
        self.plot1_new_pic_err = ImageTk.PhotoImage(self.plot1_resized_err)
        self.plot1_image_err = tk.Label(self.ec_error_frame, image=self.plot1_new_pic_err)
        self.plot1_err_txt = tk.StringVar()
        self.plot1_err_label = tk.Label(self.plot1_error_frame)

        self.plot1_set()
        # //////////// End Plot1 ///////////


    def ec_set(self):
        self.ec_title.config(text='Paso 1: elegir la curva elíptica a utilizar', font='Helvetica 10 bold')
        self.ec_title.pack()
        self.ec_gen_eq.set("y\u00B2 \u2261 x\u00B3 + ax + b mod q")
        self.ec_gen_eq_label.config(textvariable=self.ec_gen_eq)
        self.ec_gen_eq_label.pack()
        self.ec_frame.pack()

        self.ec_a_label.config(text="a =")
        self.ec_a_label.pack(side="left")
        self.ec_a_entry.config(width=20)
        self.ec_a_entry.pack(side="left")
        self.ec_a_frame.pack()

        self.ec_b_label.config(text="b =")
        self.ec_b_label.pack(side="left")
        self.ec_b_entry.config(width=20)
        self.ec_b_entry.pack(side="left")
        self.ec_b_frame.pack()

        self.ec_q_label.config(text="q =")
        self.ec_q_label.pack(side="left")
        self.ec_q_entry.config(width=20)
        self.ec_q_entry.pack(side="left")
        self.ec_q_frame.pack()

        self.ec_ready_button.config(text="Listo", command=lambda: self.ec_ready())
        self.ec_ready_button.pack()
        self.ec_edit_button.config(text="Editar", command=lambda: self.ec_clear())
        self.ec_edit_button.pack()
        self.ec_edit_button.pack_forget()
        self.ec_ready_button.pack(side="left")
        self.ec_image_ok.pack(side="left")
        self.ec_image_ok.pack_forget()
        self.ec_ready_frame.pack()

        self.ec_err_label.config(textvariable=self.ec_err_txt)
        self.ec_image_err.pack(side="left")
        self.ec_image_err.pack_forget()
        self.ec_err_label.pack(side="left")
        self.ec_err_label.pack_forget()
        self.ec_error_frame.pack()

    def ec_ready(self):
        try:
            a_str = self.ec_a_entry.get()
            b_str = self.ec_b_entry.get()
            q_str = self.ec_q_entry.get()

            if a_str == '' or b_str == '' or q_str == '':
                raise AssertionError("a, b o q están vacíos")

            if not a_str.lstrip('-').isnumeric() or not b_str.lstrip('-').isnumeric() or not q_str.lstrip(
                    '-').isnumeric():
                raise AssertionError("a, b y q deben ser números enteros")

            a = int(self.ec_a_entry.get())
            b = int(self.ec_b_entry.get())
            q = int(self.ec_q_entry.get())

            self.elliptic_curve = ec.EllipticCurve(a, b, q)

            self.ec_a_entry.config(state="disabled")
            self.ec_b_entry.config(state="disabled")
            self.ec_q_entry.config(state="disabled")

            self.ec_ready_button.pack_forget()
            self.ec_image_err.pack_forget()
            self.ec_err_label.pack_forget()
            self.ec_error_frame.configure(height=1)
            self.ec_edit_button.pack(side="left")
            self.ec_image_ok.pack(side="right")

            self.plot1_title.config(state="normal")
            self.plot1_button.config(state="normal")
            self.plot1_ready_button.config(state="normal")

        except Exception as msg:
            self.err_display(msg.args[0], self.ec_err_txt, self.ec_image_err, self.ec_err_label, self.ec_error_frame)

    def ec_clear(self):
        self.ec_a_entry.config(state="normal")
        self.ec_a_entry.delete(0, 'end')
        self.ec_b_entry.config(state="normal")
        self.ec_b_entry.delete(0, 'end')
        self.ec_q_entry.config(state="normal")
        self.ec_q_entry.delete(0, 'end')
        self.ec_title.pack()
        self.ec_err_txt.set("")
        self.ec_ready_button.pack()
        self.ec_image_ok.pack_forget()
        self.ec_err_label.pack_forget()
        self.ec_error_frame.configure(height=1)
        self.ec_edit_button.pack_forget()
        self.elliptic_curve = None

    def plot1_set(self):
        self.plot1_title.config(text='Paso 2: elegir puntos P y Q a sumar', font='Helvetica 10 bold', state="disabled")
        self.plot1_title.pack()
        self.plot1_frame.pack()

        self.plot1_button.config(state="disabled")
        self.plot1_button.pack()
        self.plot1_graph_frame.pack()

        self.plot1_ready_button.config(text="Listo", command=lambda: self.plot1_ready(), state="disabled")
        self.plot1_ready_button.pack()
        self.plot1_edit_button.config(text="Editar", command=lambda: self.plot1_clear(), state="disabled")
        self.plot1_edit_button.pack()
        self.plot1_edit_button.pack_forget()
        self.plot1_ready_button.pack(side="left")
        self.plot1_image_ok.pack(side="left")
        self.plot1_image_ok.pack_forget()
        self.plot1_ready_frame.pack()

        self.plot1_p_label.config(text="P = ", state="disabled")
        self.plot1_p_label.pack(side="left")
        self.plot1_p_val_label.pack(side="left")
        self.plot1_p_frame.pack()

        self.plot1_q_label.config(text="Q = ", state="disabled")
        self.plot1_q_label.pack(side="left")
        self.plot1_q_val_label.pack(side="left")
        self.plot1_q_frame.pack()

        self.plot1_err_label.config(textvariable=self.plot1_err_txt)
        self.plot1_image_err.pack(side="left")
        self.plot1_image_err.pack_forget()
        self.plot1_err_label.pack(side="left")
        self.plot1_err_label.pack_forget()
        self.plot1_error_frame.pack()

    def plot1_ready(self):
        pass

    def plot1_clear(self):
        pass

    def plot1_graph(self):

        self.selected_points = None

        points = self.elliptic_curve.getPoints()

        x_coords = ()
        y_coords = ()

        for point in points:
            x_coords = x_coords + (point[0],)
            y_coords = y_coords + (point[1],)

        # x = (1, 2, 3, 4)
        # y = (1, 2, 3, 4)
        # annotes = ['a', 'b', 'c', 'd']

        fig, ax = plt.subplots()
        ax.scatter(x_coords, y_coords)
        af = draw.AnnoteFinder(x_coords, y_coords, ax=ax)
        fig.canvas.mpl_connect('button_press_event', af)

        plt.show()
        self.selected_points = af.get_selected_points()

        self.p = ec.Point(self.selected_points['P'][0], self.selected_points['P'][1])
        self.q = ec.Point(self.selected_points['Q'][0], self.selected_points['Q'][1])

        self.plot1_p_val_str.set(self.p.print())
        self.plot1_q_val_str.set(self.q.print())

        self.plot1_p_label.config(state="normal")
        self.plot1_p_val_label.config(state="normal")
        self.plot1_q_label.config(state="normal")
        self.plot1_q_val_label.config(state="normal")


    def err_display(self, text, err_txt, image_err, err_label, error_frame):
        err_txt.set(text)
        image_err.pack(side="left")
        err_label.pack(side="left")
        error_frame.pack()

    def start_page(self):
        self.frame.grid(column=0, row=0, sticky="NWES")

    def go_back(self):
        self.frame.pack_forget()
        self.app.main_page()

    def get_frame(self):
        return self.frame
