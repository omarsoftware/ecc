import tkinter as tk
from draw import ecdraw as draw
import constants as cons
from ecmath import ecmath as ec
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(1)
from PIL import Image, ImageTk


class Commutativity:
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master)

        self.title = tk.Label(self.frame, text='Propiedad de Conmutatividad', font='Helvetica 16 bold')
        self.title.pack(fill="x")

        self.elliptic_curve = None
        self.p = None
        self.q = None
        self.r1 = None
        self.r2 = None
        self.selected_points = None
        self.p_q_addition = None
        self.q_p_addition = None
        self.is_predefined = False

        # ///////////// Begin Elliptic Curve /////////////
        self.ec_frame = tk.Frame(self.frame)
        self.ec_title = tk.Label(self.ec_frame)
        self.ec_gen_eq = tk.StringVar()
        self.ec_gen_eq_label = tk.Label(self.ec_frame)

        self.ec_auto_sel_frame = tk.Frame(self.frame)
        self.ec_auto_sel_btn = tk.Button(self.ec_auto_sel_frame)

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

        # //////////// Begin points P and Q /////////////
        self.plot1_frame = tk.Frame(self.frame)
        self.plot1_title = tk.Label(self.plot1_frame)

        self.plot1_graph_frame = tk.Frame(self.plot1_frame)
        self.plot1_button = tk.Button(master=self.plot1_graph_frame,
                                      command=self.plot1_graph,
                                      height=2,
                                      width=20,
                                      text="Seleccionar Puntos")

        self.plot1_p_frame = tk.Frame(self.plot1_frame)
        self.plot1_p_label = tk.Label(self.plot1_p_frame)
        self.plot1_p_val_str = tk.StringVar()
        self.plot1_p_val_label = tk.Label(self.plot1_p_frame, textvariable=self.plot1_p_val_str)

        self.plot1_q_frame = tk.Frame(self.plot1_frame)
        self.plot1_q_label = tk.Label(self.plot1_q_frame)
        self.plot1_q_val_str = tk.StringVar()
        self.plot1_q_val_label = tk.Label(self.plot1_q_frame, textvariable=self.plot1_q_val_str)

        self.plot1_set()
        # //////////// End points P and Q /////////////

        # //////////// Begin Calculations /////////////
        self.calc_title = tk.Label(self.frame)

        self.calc_frame = tk.Frame(self.frame)

        self.p_plus_q_frame = tk.Frame(self.calc_frame)
        self.p_plus_q_label = tk.Label(self.p_plus_q_frame)
        self.p_plus_q_str = tk.StringVar()
        self.p_plus_q_val_label = tk.Label(self.p_plus_q_frame, textvariable=self.p_plus_q_str)

        self.q_plus_p_frame = tk.Frame(self.calc_frame)
        self.q_plus_p_label = tk.Label(self.q_plus_p_frame)
        self.q_plus_p_str = tk.StringVar()
        self.q_plus_p_val_label = tk.Label(self.q_plus_p_frame, textvariable=self.q_plus_p_str)

        self.space2 = tk.Label(self.frame, text=" ")
        self.space2.pack()

        self.calc_set()
        # //////////// Begin Calculations /////////////

    def ec_set(self):
        self.ec_title.config(text='Paso 1: elegir la curva elíptica a utilizar', font='Helvetica 10 bold')
        self.ec_title.pack()
        self.ec_gen_eq.set("y\u00B2 \u2261 x\u00B3 + ax + b mod q")
        self.ec_gen_eq_label.config(textvariable=self.ec_gen_eq)
        self.ec_gen_eq_label.pack()
        self.ec_frame.pack()

        self.ec_auto_sel_btn.config(text="Autocompletar", command=lambda: self.ec_auto_selection())
        self.ec_auto_sel_btn.pack()
        self.ec_auto_sel_frame.pack()

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

            if q > cons.max_q_size:
                raise AssertionError("q debe ser menor a " + str(cons.max_q_size) + " para evitar graficar demasiados puntos")

            self.elliptic_curve = ec.EllipticCurve(a, b, q)

            self.ec_auto_sel_btn.config(state="disabled")

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

        except Exception as msg:
            self.err_display(msg.args[0], self.ec_err_txt, self.ec_image_err, self.ec_err_label, self.ec_error_frame)

    def ec_clear(self):
        self.ec_auto_sel_btn.config(state="normal")
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

        self.plot1_clear_and_disable()
        self.calc_clear_and_disable()

    def plot1_set(self):
        self.plot1_title.config(text='Paso 2: elegir puntos P y Q a sumar', font='Helvetica 10 bold', state="disabled")
        self.plot1_title.pack()
        self.plot1_frame.pack()

        self.plot1_button.config(state="disabled")
        self.plot1_button.pack()
        self.plot1_graph_frame.pack()

        self.plot1_p_label.config(text="P = ", state="disabled")
        self.plot1_p_label.pack(side="left")
        self.plot1_p_val_label.pack(side="left")
        self.plot1_p_frame.pack()

        self.plot1_q_label.config(text="Q = ", state="disabled")
        self.plot1_q_label.pack(side="left")
        self.plot1_q_val_label.pack(side="left")
        self.plot1_q_frame.pack()

    def plot1_graph(self):

        self.selected_points = None

        points = self.elliptic_curve.get_points()

        x_coords = ()
        y_coords = ()

        for point in points:
            x_coords = x_coords + (point.get_x(),)
            y_coords = y_coords + (point.get_y(),)

        fig, ax = plt.subplots()
        ax.scatter(x_coords, y_coords)
        af = draw.DrawAddition(x_coords, y_coords, ax=ax)
        fig.canvas.mpl_connect('button_press_event', af)

        plt.show()
        self.selected_points = af.get_selected_points()

        if len(self.selected_points) == 2:
            self.p = ec.Point(self.selected_points['P'][0], self.selected_points['P'][1])
            self.q = ec.Point(self.selected_points['Q'][0], self.selected_points['Q'][1])

            self.plot1_p_label.config(state="normal")
            self.plot1_p_val_str.set(self.p.print())
            self.plot1_p_val_label.config(state="normal")

            self.plot1_q_label.config(state="normal")
            self.plot1_q_val_str.set(self.q.print())
            self.plot1_q_val_label.config(state="normal")

            self.r1 = self.elliptic_curve.point_addition(self.p, self.q)
            self.r2 = self.elliptic_curve.point_addition(self.q, self.p)

            self.calc_title.config(state="normal")

            self.p_plus_q_label.config(state="normal")
            if not self.r1.is_infinity():
                self.p_plus_q_str.set(self.r1.print())
            else:
                self.p_plus_q_str.set("punto en el infinito")
            self.p_plus_q_val_label.config(state="normal")

            self.q_plus_p_label.config(state="normal")
            if not self.r2.is_infinity():
                self.q_plus_p_str.set(self.r2.print())
            else:
                self.q_plus_p_str.set("punto en el infinito")
            self.q_plus_p_val_label.config(state="normal")

            fig2, ax2 = plt.subplots()
            ax2.scatter(x_coords, y_coords)
            if not self.p == self.q:
                draw_points = [(self.p, 'P'), (self.q, 'Q'), (self.r1, 'R')]
            else:
                draw_points = [(self.p, 'P = Q'), (self.r1, 'R')]
            af2 = draw.DrawOnly(x_coords, y_coords, draw_points, ax=ax2)
            # fig.canvas.mpl_connect('button_press_event', af2)
            plt.show()

    def plot1_clear_and_disable(self):
        self.plot1_title.config(state="disabled")
        self.plot1_button.config(state="disabled")

        self.plot1_p_label.config(state="disabled")
        self.plot1_p_val_str.set("")
        self.plot1_p_val_label.config(state="disabled")

        self.plot1_q_label.config(state="disabled")
        self.plot1_q_val_str.set("")
        self.plot1_q_val_label.config(state="disabled")

        self.p = None
        self.q = None

    def calc_set(self):
        self.calc_title.config(text="Paso 3: comprobar que P + Q = Q + P", state="disabled", font='Helvetica 10 bold')
        self.calc_title.pack()

        self.p_plus_q_label.config(text="P + Q = ", state="disabled")
        self.p_plus_q_label.pack(side="left")
        self.p_plus_q_str.set("")
        self.p_plus_q_val_label.pack(side="left")
        self.p_plus_q_frame.pack()

        self.p_plus_q_frame.pack()

        self.q_plus_p_label.config(text="Q + P = ", state="disabled")
        self.q_plus_p_label.pack(side="left")
        self.q_plus_p_str.set("")
        self.q_plus_p_val_label.pack(side="left")
        self.q_plus_p_frame.pack()

        self.q_plus_p_frame.pack()

        self.calc_frame.pack()

    def calc_clear_and_disable(self):
        self.calc_title.configure(state="disabled")

        self.p_plus_q_label.configure(state="disabled")
        self.p_plus_q_str.set("")
        self.p_plus_q_val_label.configure(state="disabled")

        self.q_plus_p_label.configure(state="disabled")
        self.q_plus_p_str.set("")
        self.q_plus_p_val_label.configure(state="disabled")

        self.r1 = None
        self.r2 = None

    def err_display(self, text, err_txt, image_err, err_label, error_frame):
        err_txt.set(text)
        image_err.pack(side="left")
        err_label.pack(side="left")
        error_frame.pack()

    def ec_auto_selection(self):
        self.ec_a_entry.delete(0, "end")
        self.ec_a_entry.insert(0, 10)

        self.ec_b_entry.delete(0, "end")
        self.ec_b_entry.insert(0, 15)

        self.ec_q_entry.delete(0, "end")
        self.ec_q_entry.insert(0, 23)

    def start_page(self):
        self.frame.grid(column=0, row=0, sticky="NWES")

    def go_back(self):
        self.frame.pack_forget()
        self.app.main_page()

    def get_frame(self):
        return self.frame
