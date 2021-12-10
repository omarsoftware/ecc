import tkinter as tk
import constants as cons
import ecmath as ec
import random as rand
from PIL import Image, ImageTk


class Commutativity:
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master)

        self.title = tk.Label(self.frame, text='Propiedad de Conmutatividad', font='Helvetica 16 bold')
        self.title.pack(fill="x")

        self.elliptic_curve = None
        self.g = None
        self.p = None
        self.q = None
        self.isPredefined = False

        # ///////////// Begin Elliptic Curve /////////////
        self.ec_frame = tk.Frame(self.frame)
        self.ec_title = tk.Label(self.ec_frame)
        self.ec_gen_eq = tk.StringVar()
        self.ec_gen_eq_label = tk.Label(self.ec_frame)

        # Begin predefined curves dropdown
        self.dropdown_frame = tk.Frame(self.frame)
        self.predef_curve = None
        self.curves_list = cons.get_predef_curves_names()
        self.dropdown_str = tk.StringVar()
        self.dropdown_str.set(self.curves_list[0])
        self.predef_dropdown = tk.OptionMenu(self.dropdown_frame, self.dropdown_str, *self.curves_list)
        self.button_chosen_curve = tk.Button(self.dropdown_frame, text="Seleccionar",
                                             command=lambda: self.chosen_curve())
        # end predefined curves dropdown

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

        # ///////////// Begin Generator Point /////////////
        self.g_title = tk.Label(self.frame)

        self.g_x_frame = tk.Frame(self.frame)
        self.g_x_label = tk.Label(self.g_x_frame)
        self.g_x_entry = tk.Entry(self.g_x_frame)

        self.g_y_frame = tk.Frame(self.frame)
        self.g_y_label = tk.Label(self.g_y_frame)
        self.g_y_entry = tk.Entry(self.g_y_frame)

        self.g_ready_frame = tk.Frame(self.frame)
        self.g_ready_button = tk.Button(self.g_ready_frame)
        self.g_edit_button = tk.Button(self.g_ready_frame)
        self.g_load_ok = Image.open(cons.check_path)
        self.g_resized = self.g_load_ok.resize(cons.x_and_check_size, Image.ANTIALIAS)
        self.g_new_pic_ok = ImageTk.PhotoImage(self.g_resized)
        self.g_image_ok = tk.Label(self.g_ready_frame, image=self.g_new_pic_ok)

        self.g_error_frame = tk.Frame(self.frame)
        self.g_label = tk.Label(self.g_error_frame)
        self.g_err_txt = tk.StringVar()
        self.g_err = tk.Label(self.g_error_frame)
        self.g_load_err = Image.open(cons.x_path)
        self.g_resized_err = self.g_load_err.resize(cons.x_and_check_size, Image.ANTIALIAS)
        self.g_new_pic_err = ImageTk.PhotoImage(self.g_resized_err)
        self.g_image_err = tk.Label(self.g_error_frame, image=self.g_new_pic_err)

        self.g_set()
        # ///////////// End Generator Point /////////////

        # //////////// Begin points P and Q /////////////
        self.p_q_title = tk.Label(self.frame)
        self.p_q_frame = tk.Frame(self.frame)

        self.p_x_frame = tk.Frame(self.p_q_frame)
        self.p_x_label = tk.Label(self.p_x_frame)
        self.p_x_entry = tk.Entry(self.p_x_frame)
        self.p_y_frame = tk.Frame(self.p_q_frame)
        self.p_y_label = tk.Label(self.p_y_frame)
        self.p_y_entry = tk.Entry(self.p_y_frame)

        self.q_x_frame = tk.Frame(self.p_q_frame)
        self.q_x_label = tk.Label(self.q_x_frame)
        self.q_x_entry = tk.Entry(self.q_x_frame)
        self.q_y_frame = tk.Frame(self.p_q_frame)
        self.q_y_label = tk.Label(self.q_y_frame)
        self.q_y_entry = tk.Entry(self.q_y_frame)

        self.p_q_ready_frame = tk.Frame(self.p_q_frame)
        self.p_q_ready_button = tk.Button(self.p_q_ready_frame)
        self.p_q_edit_button = tk.Button(self.p_q_ready_frame)
        self.p_q_load_ok = Image.open(cons.check_path)
        self.p_q_resized = self.p_q_load_ok.resize(cons.x_and_check_size, Image.ANTIALIAS)
        self.p_q_new_pic_ok = ImageTk.PhotoImage(self.p_q_resized)
        self.p_q_image_ok = tk.Label(self.p_q_ready_frame, image=self.p_q_new_pic_ok)

        self.p_q_error_frame = tk.Frame(self.frame)
        self.p_q_load_err = Image.open(cons.x_path)
        self.p_q_resized_err = self.ec_load_err.resize(cons.x_and_check_size, Image.ANTIALIAS)
        self.p_q_new_pic_err = ImageTk.PhotoImage(self.p_q_resized_err)
        self.p_q_image_err = tk.Label(self.p_q_error_frame, image=self.p_q_new_pic_err)
        self.p_q_err_txt = tk.StringVar()
        self.p_q_err_label = tk.Label(self.p_q_error_frame)

        self.p_q_set()
        # //////////// End points P and Q /////////////

        # //////////// Begin Calculations /////////////
        self.calc_title = tk.Label(self.frame)

        self.calc_frame = tk.Frame(self.frame)

        self.p_plus_q_frame = tk.Frame(self.calc_frame)
        self.p_plus_q_title = tk.Label(self.p_plus_q_frame)

        self.p_plus_q_x_frame = tk.Frame(self.p_plus_q_frame)
        self.p_plus_q_x_label = tk.Label(self.p_plus_q_x_frame)
        self.p_plus_q_x_str = tk.StringVar()
        self.p_plus_q_x_val_label = tk.Label(self.p_plus_q_x_frame, textvariable=self.p_plus_q_x_str)

        self.p_plus_q_y_frame = tk.Frame(self.p_plus_q_frame)
        self.p_plus_q_y_label = tk.Label(self.p_plus_q_y_frame)
        self.p_plus_q_y_str = tk.StringVar()
        self.p_plus_q_y_val_label = tk.Label(self.p_plus_q_y_frame, textvariable=self.p_plus_q_y_str)

        self.q_plus_p_frame = tk.Frame(self.calc_frame)
        self.q_plus_p_title = tk.Label(self.q_plus_p_frame)

        self.q_plus_p_x_frame = tk.Frame(self.q_plus_p_frame)
        self.q_plus_p_x_label = tk.Label(self.q_plus_p_x_frame)
        self.q_plus_p_x_str = tk.StringVar()
        self.q_plus_p_x_val_label = tk.Label(self.q_plus_p_x_frame, textvariable=self.q_plus_p_x_str)

        self.q_plus_p_y_frame = tk.Frame(self.q_plus_p_frame)
        self.q_plus_p_y_label = tk.Label(self.q_plus_p_y_frame)
        self.q_plus_p_y_str = tk.StringVar()
        self.q_plus_p_y_val_label = tk.Label(self.q_plus_p_y_frame, textvariable=self.q_plus_p_y_str)

        self.calc_set()
        # //////////// Begin Calculations /////////////

    def chosen_curve(self):
        self.predef_curve = cons.get_curve(self.dropdown_str.get())
        self.isPredefined = True

        self.ec_a_entry.delete(0, "end")
        self.ec_a_entry.insert(0, self.predef_curve["a"])

        self.ec_b_entry.delete(0, "end")
        self.ec_b_entry.insert(0, self.predef_curve["b"])

        self.ec_q_entry.delete(0, "end")
        self.ec_q_entry.insert(0, self.predef_curve["q"])

    def ec_set(self):
        self.ec_title.config(text='Paso 1: elegir la curva elíptica a utilizar', font='Helvetica 10 bold')
        self.ec_title.pack()
        self.ec_gen_eq.set("y\u00B2 \u2261 x\u00B3 + ax + b mod q")
        self.ec_gen_eq_label.config(textvariable=self.ec_gen_eq)
        self.ec_gen_eq_label.pack()
        self.ec_frame.pack()

        self.predef_dropdown.pack(side="left")
        self.button_chosen_curve.pack(side="left")
        self.dropdown_frame.pack()

        self.ec_a_label.config(text="a =")
        self.ec_a_label.pack(side="left")
        self.ec_a_entry.config(width=80)
        self.ec_a_entry.pack(side="left")
        self.ec_a_frame.pack()

        self.ec_b_label.config(text="b =")
        self.ec_b_label.pack(side="left")
        self.ec_b_entry.config(width=80)
        self.ec_b_entry.pack(side="left")
        self.ec_b_frame.pack()

        self.ec_q_label.config(text="q =")
        self.ec_q_label.pack(side="left")
        self.ec_q_entry.config(width=80)
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

            if self.isPredefined:
                self.elliptic_curve = ec.EllipticCurve(self.predef_curve["a"], self.predef_curve["b"],
                                                       self.predef_curve["q"],
                                                       ec.Point(self.predef_curve["g"][0], self.predef_curve["g"][1]),
                                                       self.predef_curve["n"], self.predef_curve["h"])
            else:
                self.elliptic_curve = ec.EllipticCurve(a, b, q)

            self.ec_a_entry.config(state="disabled")
            self.ec_b_entry.config(state="disabled")
            self.ec_q_entry.config(state="disabled")
            self.predef_dropdown.config(state="disabled")
            self.button_chosen_curve.config(state="disabled")

            self.ec_ready_button.pack_forget()
            self.ec_image_err.pack_forget()
            self.ec_err_label.pack_forget()
            self.ec_error_frame.configure(height=1)
            self.ec_edit_button.pack(side="left")
            self.ec_image_ok.pack(side="right")

            self.g_title.config(state='normal')
            self.g_x_label.config(state='normal')
            self.g_y_label.config(state='normal')
            self.g_x_entry.config(state='normal')
            self.g_y_entry.config(state='normal')
            self.g_ready_button.config(state='normal')

            if self.isPredefined:
                self.g_x_entry.delete(0, "end")
                self.g_x_entry.insert(0, self.elliptic_curve.get_g().get_x())
                self.g_y_entry.delete(0, "end")
                self.g_y_entry.insert(0, self.elliptic_curve.get_g().get_y())

        except Exception as msg:
            self.err_display(msg.args[0], self.ec_err_txt, self.ec_image_err, self.ec_err_label, self.ec_error_frame)

    def ec_clear(self):
        self.ec_a_entry.config(state="normal")
        self.ec_a_entry.delete(0, 'end')
        self.ec_b_entry.config(state="normal")
        self.ec_b_entry.delete(0, 'end')
        self.ec_q_entry.config(state="normal")
        self.ec_q_entry.delete(0, 'end')
        self.predef_dropdown.config(state="normal")
        self.button_chosen_curve.config(state="normal")
        self.ec_title.pack()
        self.ec_err_txt.set("")
        self.ec_ready_button.pack()
        self.ec_image_ok.pack_forget()
        self.ec_err_label.pack_forget()
        self.ec_error_frame.configure(height=1)
        self.ec_edit_button.pack_forget()
        self.elliptic_curve = None

        # self.g_clear_and_disable()
        # self.bob_alice_clear_and_disable()

    def g_set(self):
        self.g_title.config(text="Paso 2: elegir punto generador utilizado y compartido por Bob y Alicia",
                            state="disabled", font='Helvetica 10 bold')
        self.g_title.pack()

        self.g_x_label.config(text="Gx =", state="disabled")
        self.g_x_label.pack(side="left")
        self.g_x_entry.config(width=80, state="disabled")
        self.g_x_entry.pack(side="left")
        self.g_x_frame.pack()

        self.g_y_label.config(text="Gy =", state="disabled")
        self.g_y_label.pack(side="left")
        self.g_y_entry.config(width=80, state="disabled")
        self.g_y_entry.pack(side="left")
        self.g_y_frame.pack()

        self.g_ready_button.config(text="Listo", state="disabled", command=lambda: self.g_ready())
        self.g_ready_button.pack()
        self.g_edit_button.config(text="Editar", command=lambda: self.g_clear())
        self.g_edit_button.pack()
        self.g_edit_button.pack_forget()
        self.g_image_ok.pack()
        self.g_image_ok.pack_forget()
        self.g_ready_frame.pack()

        self.g_err.config(textvariable=self.g_err_txt)
        self.g_image_err.pack_forget()
        self.g_err.pack(side="left")
        self.g_err.pack_forget()
        self.g_error_frame.pack()

    def g_ready(self):
        try:
            x_str = self.g_x_entry.get()
            y_str = self.g_y_entry.get()

            if x_str == '' or y_str == '':
                raise AssertionError("x o y están vacíos")

            if not x_str.lstrip('-').isnumeric() or not y_str.lstrip('-').isnumeric():
                raise AssertionError("x e y deben ser números")

            self.g = ec.Point(int(x_str), int(y_str))

            if not self.elliptic_curve.belongsToCurve(self.g):
                raise AssertionError("el punto no pertenece a la curva")

            if not self.elliptic_curve.get_g():
                self.elliptic_curve.set_g(self.g)

            self.g_x_entry.config(state="disabled")
            self.g_y_entry.config(state="disabled")

            self.g_ready_button.pack_forget()
            self.g_edit_button.pack(side="left")
            self.g_image_ok.pack(side="right")
            self.g_err.pack_forget()
            self.g_image_err.pack_forget()
            self.g_error_frame.configure(height=1)

            self.p_x_label.configure(state="normal")
            self.p_x_entry.configure(state="normal")
            self.p_y_label.configure(state="normal")
            self.p_y_entry.configure(state="normal")

            self.q_x_label.configure(state="normal")
            self.q_x_entry.configure(state="normal")
            self.q_y_label.configure(state="normal")
            self.q_y_entry.configure(state="normal")

        except Exception as msg:
            self.err_display(msg.args[0], self.g_err_txt, self.g_image_err, self.g_err, self.g_error_frame)

    def g_clear(self):
        # self.privkey_autogen_btn.config(state="normal")
        self.g_x_entry.config(state="normal")
        self.g_x_entry.delete(0, "end")
        self.g_y_entry.config(state="normal")
        self.g_y_entry.delete(0, "end")
        self.g_edit_button.pack_forget()
        self.g_image_ok.pack_forget()
        self.g_ready_button.pack(side="left")
        self.g_err_txt.set("")
        self.g_image_err.pack_forget()
        self.g_err.pack_forget()
        self.g_error_frame.configure(height=1)
        self.g = None

        # self.bob_alice_clear_and_disable()

    def p_q_set(self):
        self.p_q_title.config(text="Paso 3: elegir dos puntos P y Q para sumarlos",
                              state="disabled", font='Helvetica 10 bold')
        self.p_q_title.pack()

        self.p_x_label.config(text="Px =", state="disabled")
        self.p_x_label.pack(side="left")
        self.p_x_entry.config(width=80, state="disabled")
        self.p_x_entry.pack(side="left")
        self.p_x_frame.pack()

        self.p_y_label.config(text="Py =", state="disabled")
        self.p_y_label.pack(side="left")
        self.p_y_entry.config(width=80, state="disabled")
        self.p_y_entry.pack(side="left")
        self.p_y_frame.pack()

        self.q_x_label.config(text="Qx =", state="disabled")
        self.q_x_label.pack(side="left")
        self.q_x_entry.config(width=80, state="disabled")
        self.q_x_entry.pack(side="left")
        self.q_x_frame.pack()

        self.q_y_label.config(text="Qy =", state="disabled")
        self.q_y_label.pack(side="left")
        self.q_y_entry.config(width=80, state="disabled")
        self.q_y_entry.pack(side="left")
        self.q_y_frame.pack()

        self.p_q_ready_frame.pack()

        self.p_q_frame.pack()

        self.p_q_ready_button.config(text="Listo", command=lambda: self.p_q_ready())
        self.p_q_ready_button.pack()
        self.p_q_edit_button.config(text="Editar", command=lambda: self.p_q_clear())
        self.p_q_edit_button.pack()
        self.p_q_edit_button.pack_forget()
        self.p_q_ready_button.pack(side="left")
        self.p_q_image_ok.pack(side="left")
        self.p_q_image_ok.pack_forget()
        self.p_q_ready_frame.pack()

        self.p_q_err_label.config(textvariable=self.p_q_err_txt)
        self.p_q_image_err.pack(side="left")
        self.p_q_image_err.pack_forget()
        self.p_q_err_label.pack(side="left")
        self.p_q_err_label.pack_forget()
        self.p_q_error_frame.pack()

    def p_q_ready(self):
        try:
            px_str = self.p_x_entry.get()
            py_str = self.p_y_entry.get()
            qx_str = self.q_x_entry.get()
            qy_str = self.q_y_entry.get()

            if px_str == '' or py_str == '' or qx_str == '' or qy_str == '':
                raise AssertionError("alguna coordenada se encuentra vacía")

            if not px_str.lstrip('-').isnumeric() or not py_str.lstrip('-').isnumeric() or not \
                    qx_str.lstrip('-').isnumeric() or not qy_str.lstrip('-').isnumeric():
                raise AssertionError("x e y deben ser números")

            self.p = ec.Point(int(px_str), int(py_str))
            self.q = ec.Point(int(qx_str), int(qy_str))

            if not self.elliptic_curve.belongsToCurve(self.p):
                raise AssertionError("el punto P no pertenece a la curva")

            if not self.elliptic_curve.belongsToCurve(self.q):
                raise AssertionError("el punto Q no pertenece a la curva")

            if not self.elliptic_curve.get_g():
                self.elliptic_curve.set_g(self.g)

            p_q_addition = self.elliptic_curve.point_addition(self.p, self.q)
            q_p_addition = self.elliptic_curve.point_addition(self.p, self.q)

            self.p_x_entry.config(state="disabled")
            self.p_y_entry.config(state="disabled")
            self.q_x_entry.config(state="disabled")
            self.q_y_entry.config(state="disabled")

            self.p_q_ready_button.pack_forget()
            self.p_q_edit_button.pack(side="left")
            self.p_q_image_ok.pack(side="right")
            self.p_q_err_label.pack_forget()
            self.p_q_image_err.pack_forget()
            self.p_q_error_frame.configure(height=1)

            self.calc_title.config(state="normal")
            self.p_plus_q_title.config(state="normal")
            self.p_plus_q_x_label.config(state="normal")
            self.p_plus_q_x_str.set(p_q_addition.get_x())
            self.p_plus_q_x_val_label.config(state="normal")
            self.p_plus_q_y_label.config(state="normal")
            self.p_plus_q_y_str.set(p_q_addition.get_y())
            self.p_plus_q_y_val_label.config(state="normal")

            self.q_plus_p_title.config(state="normal")
            self.q_plus_p_x_label.config(state="normal")
            self.q_plus_p_x_str.set(q_p_addition.get_x())
            self.q_plus_p_x_val_label.config(state="normal")
            self.q_plus_p_y_label.config(state="normal")
            self.q_plus_p_y_str.set(q_p_addition.get_y())
            self.q_plus_p_y_val_label.config(state="normal")

        except Exception as msg:
            self.err_display(msg.args[0], self.p_q_err_txt, self.p_q_image_err, self.p_q_err_label, self.p_q_error_frame)

    def p_q_clear(self):
        pass

    def calc_set(self):
        self.calc_title.config(text="Paso 4: comprobar que P + Q = Q + P", state="disabled", font='Helvetica 10 bold')
        self.calc_title.pack()

        self.p_plus_q_title.config(text="P + Q:", state="disabled")
        self.p_plus_q_title.pack()

        self.p_plus_q_x_label.config(text="x =", state="disabled")
        self.p_plus_q_x_label.pack(side="left")
        self.p_plus_q_x_str.set("")
        self.p_plus_q_x_val_label.pack(side="left")
        self.p_plus_q_x_frame.pack()

        self.p_plus_q_y_label.config(text="y =", state="disabled")
        self.p_plus_q_y_label.pack(side="left")
        self.p_plus_q_y_str.set("")
        self.p_plus_q_y_val_label.pack(side="left")
        self.p_plus_q_y_frame.pack()

        self.p_plus_q_frame.pack()

        self.q_plus_p_title.config(text="Q + P:", state="disabled")
        self.q_plus_p_title.pack()

        self.q_plus_p_x_label.config(text="x =", state="disabled")
        self.q_plus_p_x_label.pack(side="left")
        self.q_plus_p_x_str.set("")
        self.q_plus_p_x_val_label.pack(side="left")
        self.q_plus_p_x_frame.pack()

        self.q_plus_p_y_label.config(text="y =", state="disabled")
        self.q_plus_p_y_label.pack(side="left")
        self.q_plus_p_y_str.set("")
        self.q_plus_p_y_val_label.pack(side="left")
        self.q_plus_p_y_frame.pack()

        self.q_plus_p_frame.pack()

        self.calc_frame.pack()

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
