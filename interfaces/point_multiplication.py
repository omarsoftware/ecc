import tkinter as tk
from draw import ecdraw as draw
import constants as cons
from ecmath import ecmath as ec
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(1)
import time
import decimal
from PIL import Image, ImageTk


class PointMultiplication:
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master)

        self.title = tk.Label(self.frame, text='Multiplicación de Punto', font='Helvetica 16 bold')
        self.title.pack(fill="x")

        self.elliptic_curve = None
        self.p = None
        self.q = None
        self.r_1 = None
        self.r_2 = None
        self.selected_points = None

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

        self.space1 = tk.Label(self.frame, text=" ")
        self.space1.pack()

        # ///////////// Begin Plot1 /////////////
        self.plot1_frame = tk.Frame(self.frame)
        self.plot1_title = tk.Label(self.plot1_frame)

        self.plot1_graph_frame = tk.Frame(self.plot1_frame)
        self.plot1_button = tk.Button(master=self.plot1_graph_frame,
                                      command=self.plot1_graph,
                                      height=2,
                                      width=20,
                                      text="Seleccionar Punto")

        self.plot1_p_frame = tk.Frame(self.plot1_frame)
        self.plot1_p_label = tk.Label(self.plot1_p_frame)
        self.plot1_p_val_str = tk.StringVar()
        self.plot1_p_val_label = tk.Label(self.plot1_p_frame, textvariable=self.plot1_p_val_str)

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

        self.space2 = tk.Label(self.frame, text=" ")
        self.space2.pack()

        # //////////// Begin scalar number ///////////
        self.scalar_frame = tk.Frame(self.frame)
        self.scalar_title = tk.Label(self.scalar_frame)

        self.scalar_n_frame = tk.Frame(self.frame)
        self.scalar_n_label = tk.Label(self.scalar_n_frame)
        self.scalar_n_entry = tk.Entry(self.scalar_n_frame)

        self.scalar_ready_frame = tk.Frame(self.frame)
        self.scalar_ready_button = tk.Button(self.scalar_ready_frame)
        self.scalar_edit_button = tk.Button(self.scalar_ready_frame)
        self.scalar_load_ok = Image.open(cons.check_path)
        self.scalar_resized = self.scalar_load_ok.resize(cons.x_and_check_size, Image.ANTIALIAS)
        self.scalar_new_pic_ok = ImageTk.PhotoImage(self.scalar_resized)
        self.scalar_image_ok = tk.Label(self.scalar_ready_frame, image=self.scalar_new_pic_ok)

        self.scalar_error_frame = tk.Frame(self.frame)
        self.scalar_load_err = Image.open(cons.x_path)
        self.scalar_resized_err = self.scalar_load_err.resize(cons.x_and_check_size, Image.ANTIALIAS)
        self.scalar_new_pic_err = ImageTk.PhotoImage(self.scalar_resized_err)
        self.scalar_image_err = tk.Label(self.scalar_error_frame, image=self.scalar_new_pic_err)
        self.scalar_err_txt = tk.StringVar()
        self.scalar_err_label = tk.Label(self.scalar_error_frame)

        self.scalar_set()

        # //////////// End scalar number ///////////

        self.space3 = tk.Label(self.frame, text=" ")
        self.space3.pack()

        # ///////////// Begin Multiplication /////////////
        self.mult_frame = tk.Frame(self.frame)
        self.mult_title = tk.Label(self.mult_frame)

        self.mult_result_point_frame = tk.Frame(self.mult_frame)
        self.mult_result_point_title_lbl = tk.Label(self.mult_result_point_frame)
        self.mult_result_point_str = tk.StringVar()
        self.mult_result_point_lbl = tk.Label(self.mult_result_point_frame, textvariable=self.mult_result_point_str)

        self.space4 = tk.Label(self.mult_frame, text=" ")

        self.mult_direct_frame = tk.Frame(self.mult_frame)
        self.mult_direct_title_lbl = tk.Label(self.mult_direct_frame)
        self.mult_direct_result_str = tk.StringVar()
        self.mult_direct_result_lbl = tk.Label(self.mult_direct_frame, textvariable=self.mult_direct_result_str)

        self.space5 = tk.Label(self.mult_frame, text=" ")

        self.mult_d_a_a_frame = tk.Frame(self.mult_frame)
        self.mult_d_a_a_title_lbl = tk.Label(self.mult_d_a_a_frame)
        self.mult_d_a_a_result_str = tk.StringVar()
        self.mult_d_a_a_result_lbl = tk.Label(self.mult_d_a_a_frame, textvariable=self.mult_d_a_a_result_str)

        self.mult_set()

        # ///////////// End Multiplication /////////////

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
        self.scalar_clear_and_disable()
        self.mult_clear_and_disable()

    def ec_auto_selection(self):
        self.ec_a_entry.delete(0, "end")
        self.ec_a_entry.insert(0, 10)

        self.ec_b_entry.delete(0, "end")
        self.ec_b_entry.insert(0, 15)

        self.ec_q_entry.delete(0, "end")
        self.ec_q_entry.insert(0, 23)

    def plot1_set(self):
        self.plot1_title.config(text='Paso 2: elegir punto P a multiplicar', font='Helvetica 10 bold', state="disabled")
        self.plot1_title.pack()
        self.plot1_frame.pack()

        self.plot1_button.config(state="disabled")
        self.plot1_button.pack()
        self.plot1_graph_frame.pack()

        self.plot1_p_label.config(text="P = ", state="disabled")
        self.plot1_p_label.pack(side="left")
        self.plot1_p_val_label.config(state="disabled")
        self.plot1_p_val_label.pack(side="left")
        self.plot1_p_frame.pack()

        self.plot1_ready_button.config(text="Listo", command=lambda: self.plot1_ready(), state="disabled")
        self.plot1_ready_button.pack()

        self.plot1_edit_button.config(text="Editar", command=lambda: self.plot1_clear())
        self.plot1_edit_button.pack()
        self.plot1_edit_button.pack_forget()
        self.plot1_image_ok.pack(side="left")
        self.plot1_image_ok.pack_forget()
        self.plot1_ready_frame.pack()

        self.plot1_err_label.config(textvariable=self.plot1_err_txt)
        self.plot1_image_err.pack(side="left")
        self.plot1_image_err.pack_forget()
        self.plot1_err_label.pack(side="left")
        self.plot1_err_label.pack_forget()
        self.plot1_error_frame.pack()

    def plot1_ready(self):

        self.plot1_button.config(state="disabled")
        self.plot1_p_label.config(state="disabled")
        self.plot1_p_val_label.config(state="disabled")

        self.plot1_ready_button.pack_forget()
        self.plot1_image_err.pack_forget()
        self.plot1_err_label.pack_forget()
        self.plot1_error_frame.configure(height=1)
        self.plot1_edit_button.pack(side="left")
        self.plot1_image_ok.pack(side="right")

        self.scalar_title.config(state="normal")
        self.scalar_n_label.config(state="normal")
        self.scalar_n_entry.config(state="normal")
        self.scalar_ready_button.config(state="normal")

    def plot1_clear(self):
        self.plot1_button.config(state="normal")
        self.plot1_p_val_str.set("")
        self.plot1_p_label.config(state="disable")
        self.plot1_p_val_label.config(state="disable")
        self.plot1_err_txt.set("")
        self.plot1_ready_button.config(state="disable")
        self.plot1_ready_button.pack()
        self.plot1_image_ok.pack_forget()
        self.plot1_err_label.pack_forget()
        self.plot1_error_frame.configure(height=1)
        self.plot1_edit_button.pack_forget()

        self.scalar_clear_and_disable()
        self.mult_clear_and_disable()

    def plot1_clear_and_disable(self):
        self.plot1_title.config(state="disable")
        self.plot1_p_val_str.set("")
        self.plot1_button.config(state="disable")
        self.plot1_p_label.config(state="disable")
        self.plot1_p_val_label.config(state="disable")
        self.plot1_err_txt.set("")
        self.plot1_ready_button.config(state="disable")
        self.plot1_ready_button.pack()
        self.plot1_image_ok.pack_forget()
        self.plot1_err_label.pack_forget()
        self.plot1_error_frame.configure(height=1)
        self.plot1_edit_button.pack_forget()

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
        af = draw.DrawSinglePoint(x_coords, y_coords, ax=ax)
        fig.canvas.mpl_connect('button_press_event', af)

        plt.show()
        self.selected_points = af.get_selected_points()
        self.p = ec.Point(self.selected_points['P'][0], self.selected_points['P'][1])
        self.plot1_p_val_str.set(self.p.print())

        self.plot1_p_label.config(state="normal")
        self.plot1_p_val_label.config(state="normal")
        self.plot1_ready_button.config(state="normal")

    def scalar_set(self):
        self.scalar_title.config(text='Paso 3: elegir escalar n para luego calcular R = n * P', font='Helvetica 10 bold', state="disabled")
        self.scalar_title.pack()
        self.scalar_frame.pack()

        self.scalar_n_label.config(text="n =", state="disabled")
        self.scalar_n_label.pack(side="left")
        self.scalar_n_entry.config(width=20, state="disabled")
        self.scalar_n_entry.pack(side="left")
        self.scalar_n_frame.pack()

        self.scalar_ready_button.config(text="Listo", command=lambda: self.scalar_ready(), state="disabled")
        self.scalar_ready_button.pack()
        self.scalar_edit_button.config(text="Editar", command=lambda: self.scalar_clear())
        self.scalar_edit_button.pack()
        self.scalar_edit_button.pack_forget()
        self.scalar_ready_button.pack(side="left")
        self.scalar_image_ok.pack(side="left")
        self.scalar_image_ok.pack_forget()
        self.scalar_ready_frame.pack()

        self.scalar_err_label.config(textvariable=self.scalar_err_txt)
        self.scalar_image_err.pack(side="left")
        self.scalar_image_err.pack_forget()
        self.scalar_err_label.pack(side="left")
        self.scalar_err_label.pack_forget()
        self.scalar_error_frame.pack()

    def scalar_ready(self):
        try:
            n_str = self.scalar_n_entry.get()

            if n_str == '':
                raise AssertionError("n está vacío")

            if not n_str.lstrip('-').isnumeric():
                raise AssertionError("n debe ser un número entero")

            n = int(self.scalar_n_entry.get())

            if not 1 <= n <= cons.max_n_size:
                raise AssertionError("n debe ser mayor o igual a 1 y menor o igual a \n"
                                     + str(cons.max_n_size) +
                                     " para evitar tiempos de espera excesivos.")

            start_1 = time.process_time()
            self.r_1 = self.elliptic_curve.direct_mult(self.p, n)
            end_1 = time.process_time() - start_1
            self.mult_direct_result_str.set(decimal.Decimal(end_1))

            start_2 = time.process_time()
            self.r_2 = self.elliptic_curve.double_and_add(self.p, n)
            end_2 = time.process_time() - start_2
            self.mult_d_a_a_result_str.set(decimal.Decimal(end_2))

            if not self.r_1 == self.r_2:
                raise AssertionError("El resultado de ambas multiplicaciones no coincide")

            self.scalar_n_label.config(state="disable")
            self.scalar_n_entry.config(state="disable")

            self.scalar_ready_button.pack_forget()
            self.scalar_image_err.pack_forget()
            self.scalar_err_label.pack_forget()
            self.scalar_error_frame.configure(height=1)
            self.scalar_edit_button.pack(side="left")
            self.scalar_image_ok.pack(side="right")

            self.mult_title.config(state="normal")
            self.mult_result_point_str.set(self.r_1.print())
            self.mult_result_point_title_lbl.config(state="normal")
            self.mult_result_point_lbl.config(state="normal")
            self.mult_direct_title_lbl.config(state="normal")
            self.mult_direct_result_lbl.config(state="normal")
            self.mult_d_a_a_title_lbl.config(state="normal")
            self.mult_d_a_a_result_lbl.config(state="normal")

            points = self.elliptic_curve.get_points()
            x_coords = ()
            y_coords = ()

            for point in points:
                x_coords = x_coords + (point.get_x(),)
                y_coords = y_coords + (point.get_y(),)

            if not self.r_1.is_infinity():
                fig2, ax2 = plt.subplots()
                ax2.scatter(x_coords, y_coords)
                draw_points = [(self.p, 'P'), (self.r_1, 'R')]
                af2 = draw.DrawOnly(x_coords, y_coords, draw_points, ax=ax2)
                # fig.canvas.mpl_connect('button_press_event', af2)
                plt.show()

        except Exception as msg:
            self.err_display(msg.args[0], self.scalar_err_txt, self.scalar_image_err, self.scalar_err_label, self.scalar_error_frame)

    def scalar_clear(self):
        self.scalar_n_label.config(state="normal")
        self.scalar_n_entry.config(state="normal")
        self.scalar_n_entry.delete(0, 'end')

        self.scalar_ready_button.pack()
        self.scalar_image_ok.pack_forget()
        self.scalar_err_label.pack_forget()
        self.scalar_error_frame.configure(height=1)
        self.scalar_edit_button.pack_forget()

        self.mult_clear_and_disable()

    def scalar_clear_and_disable(self):
        self.scalar_title.config(state="disable")
        self.scalar_n_label.config(state="disable")

        self.scalar_n_entry.config(state="normal")
        self.scalar_n_entry.delete(0, 'end')
        self.scalar_n_entry.config(state="disable")

        self.scalar_ready_button.config(state="disabled")
        self.scalar_ready_button.pack()
        self.scalar_edit_button.pack_forget()
        self.scalar_err_txt.set("")
        self.scalar_image_err.pack_forget()
        self.scalar_image_ok.pack_forget()
        self.scalar_err_label.pack_forget()
        self.scalar_error_frame.configure(height=1)

    def mult_set(self):
        self.mult_title.config(text='Paso 4: se realiza la multiplicación R = n * P', font='Helvetica 10 bold', state="disabled")
        self.mult_title.pack()
        self.mult_frame.pack()

        self.mult_result_point_title_lbl.config(text="R = ", state="disabled")
        self.mult_result_point_title_lbl.pack(side="left")
        self.mult_result_point_str.set("")
        self.mult_result_point_lbl.config(state="disabled")
        self.mult_result_point_lbl.pack(side="left")
        self.mult_result_point_frame.pack()

        self.space4.pack()

        self.mult_direct_title_lbl.config(text="Método directo (segundos): ", state="disabled")
        self.mult_direct_title_lbl.pack()
        self.mult_direct_result_str.set("")
        self.mult_direct_result_lbl.config(state="disabled")
        self.mult_direct_result_lbl.pack()
        self.mult_direct_frame.pack()

        self.space5.pack()

        self.mult_d_a_a_title_lbl.config(text="Método double-and-add (segundos): ", state="disabled")
        self.mult_d_a_a_title_lbl.pack()
        self.mult_d_a_a_result_str.set("")
        self.mult_d_a_a_result_lbl.config(state="disabled")
        self.mult_d_a_a_result_lbl.pack()
        self.mult_d_a_a_frame.pack()

    def mult_clear_and_disable(self):
        self.mult_title.config(state="disable")
        self.r_1 = None
        self.r_2 = None
        self.mult_result_point_title_lbl.config(state="disable")
        self.mult_result_point_str.set("")
        self.mult_result_point_lbl.config(state="disable")
        self.mult_direct_title_lbl.config(state="disable")
        self.mult_direct_result_str.set("")
        self.mult_direct_result_lbl.config(state="disable")
        self.mult_d_a_a_title_lbl.config(state="disable")
        self.mult_d_a_a_result_str.set("")
        self.mult_d_a_a_result_lbl.config(state="disable")

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
