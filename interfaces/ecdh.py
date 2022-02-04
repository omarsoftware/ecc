import tkinter as tk
import constants as cons
from ecmath import ecmath as ec
import random as rand
from PIL import Image, ImageTk


class Ecdh:
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master)
        self.elliptic_curve = None
        self.g = None
        self.bob = None
        self.alice = None
        self.ecdh = None
        self.isPredefined = False
        self.bob_shared_key = None
        self.alice_shared_key = None
        self.gen_points_dict = {}

        self.title = tk.Label(self.frame, text='Diffie-Hellman con Curva Elíptica', font='Helvetica 16 bold')
        self.title.pack(fill="x")

        # ///////////// Begin Elliptic Curve /////////////
        self.ec_frame = tk.Frame(self.frame)
        self.ec_title = tk.Label(self.ec_frame)
        self.ec_gen_eq = tk.StringVar()
        self.ec_gen_eq_label = tk.Label(self.ec_frame)

        # begin predefined curves dropdown
        self.dropdown_frame = tk.Frame(self.frame)
        self.predef_curve = None
        self.curves_list = cons.get_predef_curves_names()
        self.dropdown_str = tk.StringVar()
        self.dropdown_str.set(self.curves_list[0])
        self.predef_dropdown = tk.OptionMenu(self.dropdown_frame, self.dropdown_str, *self.curves_list)
        self.button_chosen_curve = tk.Button(self.dropdown_frame, text="Seleccionar", command=lambda: self.chosen_curve())
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

        # begin generator points dropdown
        self.g_dropdown_frame = tk.Frame(self.frame)
        self.g_points_list = [""]
        self.g_dropdown_str = tk.StringVar()
        self.g_dropdown_str.set("")
        self.g_dropdown = tk.OptionMenu(self.g_dropdown_frame, self.g_dropdown_str, *self.g_points_list)
        self.g_chosen_point_btn = tk.Button(self.g_dropdown_frame, text="Seleccionar",
                                             command=lambda: self.chosen_point())
        # end generator points dropdown

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

        # ///////////// Begin Key Generation /////////////
        self.key_gen_label = tk.Label(self.frame, text="Paso 3: generación de claves públicas y privadas",
                                      state='disabled', font='Helvetica 10 bold')
        self.key_gen_label.pack()

        # ///////////// Begin Private Key autogeneration /////////////
        self.privkey_autogen_btn = tk.Button(self.frame)
        self.privkey_autogen_btn.config(text="Generación automática", state="disabled",
                                        command=lambda: self.priv_key_autogen())
        self.privkey_autogen_btn.pack()

        # ///////////// End Private Key autogeneration /////////////

        # ///////////// Begin Bob /////////////
        self.bob_title = tk.Label(self.frame)

        self.bob_priv_frame = tk.Frame(self.frame)
        self.bob_priv_label = tk.Label(self.bob_priv_frame)
        self.bob_priv_entry = tk.Entry(self.bob_priv_frame)

        self.bob_pub_frame = tk.Frame(self.frame)
        self.bob_pub_label = tk.Label(self.bob_pub_frame)

        self.bob_pub_x_frame = tk.Frame(self.bob_pub_frame)
        self.bob_pub_x_str = tk.StringVar()
        self.bob_pub_x_label = tk.Label(self.bob_pub_x_frame)
        self.bob_pub_x_val_str = tk.StringVar()
        self.bob_pub_x_val_label = tk.Label(self.bob_pub_x_frame)

        self.bob_pub_y_frame = tk.Frame(self.bob_pub_frame)
        self.bob_pub_y_str = tk.StringVar()
        self.bob_pub_y_label = tk.Label(self.bob_pub_y_frame)
        self.bob_pub_y_val_str = tk.StringVar()
        self.bob_pub_y_val_label = tk.Label(self.bob_pub_y_frame)

        self.bob_label = tk.Label(self.bob_pub_y_frame)

        self.bob_set()
        # ///////////// End Bob /////////////

        # ///////////// Begin Alice /////////////
        self.alice_title = tk.Label(self.frame)

        self.alice_priv_frame = tk.Frame(self.frame)
        self.alice_priv_label = tk.Label(self.alice_priv_frame)
        self.alice_priv_entry = tk.Entry(self.alice_priv_frame)

        self.alice_pub_frame = tk.Frame(self.frame)
        self.alice_pub_label = tk.Label(self.alice_pub_frame)

        self.alice_pub_x_frame = tk.Frame(self.alice_pub_frame)
        self.alice_pub_x_str = tk.StringVar()
        self.alice_pub_x_label = tk.Label(self.alice_pub_x_frame)
        self.alice_pub_x_val_str = tk.StringVar()
        self.alice_pub_x_val_label = tk.Label(self.alice_pub_x_frame)

        self.alice_pub_y_frame = tk.Frame(self.alice_pub_frame)
        self.alice_pub_y_str = tk.StringVar()
        self.alice_pub_y_label = tk.Label(self.alice_pub_y_frame)
        self.alice_pub_y_val_str = tk.StringVar()
        self.alice_pub_y_val_label = tk.Label(self.alice_pub_y_frame)

        self.alice_label = tk.Label(self.alice_pub_y_frame)

        self.alice_set()
        # ///////////// End Alice /////////////

        # ///////////// Begin of End for Bob and Alice /////////////
        self.bob_alice_txt = tk.StringVar()
        self.bob_alice_label = tk.Label(self.frame, textvariable=self.bob_alice_txt)
        self.bob_alice_label.pack()

        self.bob_alice_ready_frame = tk.Frame(self.frame)
        self.bob_alice_ready_button = tk.Button(self.bob_alice_ready_frame)
        self.bob_alice_edit_button = tk.Button(self.bob_alice_ready_frame)
        self.bob_alice_load_ok = Image.open(cons.check_path)
        self.bob_alice_resized = self.bob_alice_load_ok.resize(cons.x_and_check_size, Image.ANTIALIAS)
        self.bob_alice_new_pic_ok = ImageTk.PhotoImage(self.bob_alice_resized)
        self.bob_alice_image_ok = tk.Label(self.bob_alice_ready_frame, image=self.bob_alice_new_pic_ok)

        self.bob_alice_error_frame = tk.Frame(self.frame)
        self.bob_alice_label = tk.Label(self.bob_alice_error_frame)
        self.bob_alice_err_txt = tk.StringVar()
        self.bob_alice_err = tk.Label(self.bob_alice_error_frame)
        self.bob_alice_load_err = Image.open(cons.x_path)
        self.bob_alice_resized_err = self.bob_alice_load_err.resize(cons.x_and_check_size, Image.ANTIALIAS)
        self.bob_alice_new_pic_err = ImageTk.PhotoImage(self.bob_alice_resized_err)
        self.bob_alice_image_err = tk.Label(self.bob_alice_error_frame, image=self.bob_alice_new_pic_err)

        self.bob_alice_set()
        # ///////////// Begin of End for Bob and Alice /////////////

        # ///////////// End Key Generation /////////////

        # ///////////// Begin Shared Calculations /////////////
        self.shared_title_label = tk.Label(self.frame)
        self.shared_title_label.pack()

        self.bob_shared_frame = tk.Frame(self.frame)
        self.bob_shared_label = tk.Label(self.bob_shared_frame)

        self.bob_shared_x_frame = tk.Frame(self.bob_shared_frame)
        self.bob_shared_x_str = tk.StringVar()
        self.bob_shared_x_label = tk.Label(self.bob_shared_x_frame)
        self.bob_shared_x_val_str = tk.StringVar()
        self.bob_shared_x_val_label = tk.Label(self.bob_shared_x_frame)

        self.bob_shared_y_frame = tk.Frame(self.bob_shared_frame)
        self.bob_shared_y_str = tk.StringVar()
        self.bob_shared_y_label = tk.Label(self.bob_shared_y_frame)
        self.bob_shared_y_val_str = tk.StringVar()
        self.bob_shared_y_val_label = tk.Label(self.bob_shared_y_frame)

        self.alice_shared_frame = tk.Frame(self.frame)
        self.alice_shared_label = tk.Label(self.alice_shared_frame)

        self.alice_shared_x_frame = tk.Frame(self.alice_shared_frame)
        self.alice_shared_x_str = tk.StringVar()
        self.alice_shared_x_label = tk.Label(self.alice_shared_x_frame)
        self.alice_shared_x_val_str = tk.StringVar()
        self.alice_shared_x_val_label = tk.Label(self.alice_shared_x_frame)

        self.alice_shared_y_frame = tk.Frame(self.alice_shared_frame)
        self.alice_shared_y_str = tk.StringVar()
        self.alice_shared_y_label = tk.Label(self.alice_shared_y_frame)
        self.alice_shared_y_val_str = tk.StringVar()
        self.alice_shared_y_val_label = tk.Label(self.alice_shared_y_frame)

        self.bob_alice_shared_set()
        # ///////////// End Shared Calculations /////////////

    def ec_set(self):
        self.ec_title.config(text='Paso 1: elegir curva elíptica utilizada y compartida por Bob y Alicia', font='Helvetica 10 bold')
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

            if not a_str.lstrip('-').isnumeric() or not b_str.lstrip('-').isnumeric() or not q_str.lstrip('-').isnumeric():
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
                self.generator_points = self.elliptic_curve.get_generator_points()
                if self.generator_points:
                    self.g_points_list = []
                    self.gen_points_dict = {}
                    self.g_dropdown_str.set(self.generator_points[0][0].print())

                    for point in self.generator_points:
                        self.gen_points_dict[point[0].print()] = point[0]
                        self.g_points_list.append(point[0].print())
                    menu = self.g_dropdown["menu"]
                    menu.delete(0, "end")
                    for string in self.g_points_list:
                        menu.add_command(label=string,
                                         command=lambda value=string: self.g_dropdown_str.set(value))

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
            self.g_dropdown.config(state='normal')
            self.g_chosen_point_btn.config(state='normal')
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

        self.g_clear_and_disable()
        self.bob_alice_clear_and_disable()

    def g_set(self):
        self.g_title.config(text="Paso 2: elegir punto generador utilizado y compartido por Bob y Alicia",
                            state="disabled", font='Helvetica 10 bold')
        self.g_title.pack()

        self.g_dropdown.config(state="disable")
        self.g_dropdown.pack(side="left")
        self.g_chosen_point_btn.config(state="disable")
        self.g_chosen_point_btn.pack(side="left")
        self.g_dropdown_frame.pack()

        self.g_x_label.config(text="x =", state="disabled")
        self.g_x_label.pack(side="left")
        self.g_x_entry.config(width=80, state="disabled")
        self.g_x_entry.pack(side="left")
        self.g_x_frame.pack()

        self.g_y_label.config(text="y =", state="disabled")
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

            self.key_gen_label.config(state="normal")

            self.privkey_autogen_btn.config(state="normal")

            self.bob_title.config(state="normal")
            self.bob_priv_label.config(state="normal")
            self.bob_priv_entry.config(state="normal")
            self.bob_pub_label.config(state="normal")
            self.bob_label.config(state="normal")

            self.alice_title.config(state="normal")
            self.alice_priv_label.config(state="normal")
            self.alice_priv_entry.config(state="normal")
            self.alice_priv_label.config(state="normal")
            self.alice_pub_label.config(state="normal")
            self.alice_label.config(state="normal")

            self.bob_alice_ready_button.config(state="normal")

        except Exception as msg:
            self.err_display(msg.args[0], self.g_err_txt, self.g_image_err, self.g_err, self.g_error_frame)

    def g_clear(self):
        self.privkey_autogen_btn.config(state="normal")
        self.g_dropdown.config(state="normal")
        self.g_dropdown_str.set("")
        self.g_chosen_point_btn.config(state="normal")
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

        self.bob_alice_clear_and_disable()

    def g_clear_and_disable(self):
        self.g_title.config(state="disabled")
        self.g_dropdown_str.set("")
        self.g_dropdown.config(state="disabled")
        self.g_chosen_point_btn.config(state="disabled")
        self.g_x_label.config(state="disabled")
        self.g_x_entry.config(state="normal")
        self.g_x_entry.delete(0, "end")
        self.g_x_entry.config(state="disabled")
        self.g_y_label.config(state="disabled")
        self.g_y_entry.config(state="normal")
        self.g_y_entry.delete(0, "end")
        self.g_y_entry.config(state="disabled")
        self.g_ready_button.config(state="disabled")
        self.g_ready_button.pack()
        self.g_edit_button.pack_forget()
        self.g_err_txt.set("")
        self.g_image_err.pack_forget()
        self.g_image_ok.pack_forget()
        self.g_err.pack_forget()
        self.g_error_frame.configure(height=1)
        self.g = None
        self.isPredefined = False

    def bob_set(self):
        self.bob_title.config(text="Bob", state="disabled", font='Helvetica 10 bold')
        self.bob_title.pack()

        self.bob_priv_label.config(text="Clave Privada (número secreto de Bob):", state="disabled")
        self.bob_priv_label.pack()
        self.bob_priv_entry.config(state="disabled", width=40)
        self.bob_priv_entry.pack(side="left")
        self.bob_priv_frame.pack()

        self.bob_pub_label.config(text="Clave Pública (punto visible por todos):", state="disabled")
        self.bob_pub_label.pack()

        self.bob_pub_x_str.set("x = ")
        self.bob_pub_x_label.config(textvariable=self.bob_pub_x_str, state="disabled")
        self.bob_pub_x_label.pack(side="left")
        self.bob_pub_x_val_label.config(textvariable=self.bob_pub_x_val_str, state="disabled")
        self.bob_pub_x_val_label.pack(side="left")
        self.bob_pub_x_frame.pack()

        self.bob_pub_y_str.set("y = ")
        self.bob_pub_y_label.config(textvariable=self.bob_pub_y_str, state="disabled")
        self.bob_pub_y_label.pack(side="left")
        self.bob_pub_y_val_label.config(textvariable=self.bob_pub_y_val_str, state="disabled")
        self.bob_pub_y_val_label.pack(side="left")
        self.bob_pub_y_frame.pack()

        self.bob_pub_frame.pack()

    def alice_set(self):
        self.alice_title.config(text="Alicia", state="disabled", font='Helvetica 10 bold')
        self.alice_title.pack()

        self.alice_priv_label.config(text="Clave Privada (número secreto de Alicia):", state="disabled")
        self.alice_priv_label.pack()
        self.alice_priv_entry.config(state="disabled", width=40)
        self.alice_priv_entry.pack(side="left")
        self.alice_priv_frame.pack()

        self.alice_pub_label.config(text="Clave Pública (punto visible por todos):", state="disabled")
        self.alice_pub_label.pack()

        self.alice_pub_x_str.set("x = ")
        self.alice_pub_x_label.config(textvariable=self.alice_pub_x_str, state="disabled")
        self.alice_pub_x_label.pack(side="left")
        self.alice_pub_x_val_label.config(textvariable=self.alice_pub_x_val_str)
        self.alice_pub_x_val_label.pack(side="left")
        self.alice_pub_x_frame.pack()

        self.alice_pub_y_str.set("y = ")
        self.alice_pub_y_label.config(textvariable=self.alice_pub_y_str, state="disabled")
        self.alice_pub_y_label.pack(side="left")
        self.alice_pub_y_val_label.config(textvariable=self.alice_pub_y_val_str)
        self.alice_pub_y_val_label.pack(side="left")
        self.alice_pub_y_frame.pack()

        self.alice_label.pack()
        self.alice_pub_frame.pack()

    def bob_alice_set(self):
        self.bob_alice_ready_button.config(text="Listo", state="disabled", command=lambda: self.bob_alice_ready())
        self.bob_alice_ready_button.pack()

        self.bob_alice_edit_button.config(text="Editar", command=lambda: self.bob_alice_clear())
        self.bob_alice_edit_button.pack()
        self.bob_alice_edit_button.pack_forget()
        self.bob_alice_image_ok.pack()
        self.bob_alice_image_ok.pack_forget()
        self.bob_alice_ready_frame.pack()

        self.bob_alice_err.config(textvariable=self.bob_alice_err_txt)
        self.bob_alice_image_err.pack_forget()
        self.bob_alice_err.pack(side="left")
        self.bob_alice_err.pack_forget()
        self.bob_alice_error_frame.pack()

    def bob_alice_shared_set(self):

        self.shared_title_label = tk.Label(self.frame, text="Paso 4: generación de clave compartida por Alicia y Bob",
                                           state="disabled", font='Helvetica 10 bold')
        self.shared_title_label.pack()

        self.bob_shared_label.config(text="Clave Privada (punto) compartida según Bob:", state="disabled")
        self.bob_shared_label.pack()

        self.bob_shared_x_str.set("x =")
        self.bob_shared_x_label.config(textvariable=self.bob_shared_x_str, state="disabled")
        self.bob_shared_x_label.pack(side="left")
        self.bob_shared_x_val_label.config(textvariable=self.bob_shared_x_val_str, state="disabled")
        self.bob_shared_x_val_label.pack(side="left")
        self.bob_shared_x_frame.pack()

        self.bob_shared_y_str.set("y =")
        self.bob_shared_y_label.config(textvariable=self.bob_shared_y_str, state="disabled")
        self.bob_shared_y_label.pack(side="left")
        self.bob_shared_y_val_label.config(textvariable=self.bob_shared_y_val_str, state="disabled")
        self.bob_shared_y_val_label.pack(side="left")
        self.bob_shared_y_frame.pack()

        self.bob_shared_frame.pack()

        self.alice_shared_label.config(text="Clave Privada (punto) compartida según Alice:", state="disabled")
        self.alice_shared_label.pack()

        self.alice_shared_x_str.set("x =")
        self.alice_shared_x_label.config(textvariable=self.alice_shared_x_str, state="disabled")
        self.alice_shared_x_label.pack(side="left")
        self.alice_shared_x_val_label.config(textvariable=self.alice_shared_x_val_str, state="disabled")
        self.alice_shared_x_val_label.pack(side="left")
        self.alice_shared_x_frame.pack()

        self.alice_shared_y_str.set("y =")
        self.alice_shared_y_label.config(textvariable=self.alice_shared_y_str, state="disabled")
        self.alice_shared_y_label.pack(side="left")
        self.alice_shared_y_val_label.config(textvariable=self.alice_shared_y_val_str, state="disabled")
        self.alice_shared_y_val_label.pack(side="left")
        self.alice_shared_y_frame.pack()

        self.alice_shared_frame.pack()

    def bob_alice_ready(self):
        self.bob_alice_txt.set("")

        try:
            bob_priv_str = self.bob_priv_entry.get()
            alice_priv_str = self.alice_priv_entry.get()

            if bob_priv_str == '' or alice_priv_str == '':
                raise AssertionError("clave/s privada/s sin completar")

            if not bob_priv_str.lstrip('-').isnumeric() or not alice_priv_str.lstrip('-').isnumeric():
                raise AssertionError("clave/s privada/s deben ser números")

            self.bob_alice_ready_button.pack_forget()
            self.bob_alice_edit_button.pack(side="left")
            self.bob_alice_image_ok.pack(side="right")
            self.bob_alice_err.pack_forget()
            self.bob_alice_image_err.pack_forget()
            self.bob_alice_error_frame.configure(height=1)

            self.shared_title_label.configure(state="normal")

            self.bob = ec.User()
            self.alice = ec.User()
            self.ecdh = ec.ECDH(self.elliptic_curve)

            bob_priv = int(bob_priv_str)
            alice_priv = int(alice_priv_str)

            self.privkey_autogen_btn.config(state="disabled")

            self.bob.setPrivKey(bob_priv)
            self.bob.setPubKey(self.ecdh.gen_pub_key(self.bob.getPrivKey()))

            self.alice.setPrivKey(alice_priv)
            self.alice.setPubKey(self.ecdh.gen_pub_key(self.alice.getPrivKey()))

            self.bob_shared_key = self.ecdh.calc_shared_key(self.bob.getPrivKey(), self.alice.getPubKey())
            self.alice_shared_key = self.ecdh.calc_shared_key(self.alice.getPrivKey(), self.bob.getPubKey())

            self.alice_shared_x_val_str.set(self.alice_shared_key.get_x())
            self.alice_shared_y_val_str.set(self.alice_shared_key.get_y())

            self.bob_shared_label.configure(state="normal")
            self.bob_shared_x_label.config(state="normal")
            self.bob_shared_x_val_str.set(self.bob_shared_key.get_x())
            self.bob_shared_x_val_label.config(state="normal")
            self.bob_shared_y_label.config(state="normal")
            self.bob_shared_y_val_str.set(self.bob_shared_key.get_y())
            self.bob_shared_y_val_label.config(state="normal")

            self.alice_shared_label.configure(state="normal")
            self.alice_shared_x_label.config(state="normal")
            self.alice_shared_x_val_str.set(self.alice_shared_key.get_x())
            self.alice_shared_x_val_label.config(state="normal")
            self.alice_shared_y_label.config(state="normal")
            self.alice_shared_y_val_str.set(self.alice_shared_key.get_y())
            self.alice_shared_y_val_label.config(state="normal")

            self.bob_pub_x_label.config(state="normal")
            self.bob_pub_x_val_str.set(self.bob.getPubKey().get_x())
            self.bob_pub_x_val_label.config(state="normal")
            self.bob_pub_y_label.config(state="normal")
            self.bob_pub_y_val_str.set(self.bob.getPubKey().get_y())
            self.bob_pub_y_val_label.config(state="normal")

            self.alice.setPrivKey(alice_priv)
            self.alice.setPubKey(self.ecdh.gen_pub_key(self.alice.getPrivKey()))
            self.alice_pub_x_label.config(state="normal")
            self.alice_pub_x_val_str.set(self.alice.getPubKey().get_x())
            self.alice_pub_x_val_label.config(state="normal")
            self.alice_pub_y_label.config(state="normal")
            self.alice_pub_y_val_str.set(self.alice.getPubKey().get_y())
            self.alice_pub_y_val_label.config(state="normal")

            self.bob_priv_entry.config(state="disabled")
            self.alice_priv_entry.config(state="disabled")
            self.bob_alice_ready_button.pack_forget()
            self.bob_alice_edit_button.pack()
            self.bob_alice_label.config(state="normal")

        except Exception as msg:
            self.err_display(msg.args[0], self.bob_alice_err_txt, self.bob_alice_image_err,
                             self.bob_alice_err, self.bob_alice_error_frame)

    def bob_alice_clear(self):
        self.privkey_autogen_btn.config(state="normal")

        self.bob_priv_entry.config(state="normal")
        self.bob_priv_entry.delete(0, "end")
        self.bob_pub_x_label.config(state="disabled")
        self.bob_pub_x_val_str.set("")
        self.bob_pub_y_label.config(state="disabled")
        self.bob_pub_y_val_str.set("")

        self.alice_priv_entry.config(state="normal")
        self.alice_priv_entry.delete(0, "end")
        self.alice_pub_x_label.config(state="disabled")
        self.alice_pub_x_val_str.set("")
        self.alice_pub_y_label.config(state="disabled")
        self.alice_pub_y_val_str.set("")

        self.bob = None
        self.alice = None
        self.bob_alice_edit_button.pack_forget()
        self.bob_alice_image_ok.pack_forget()
        self.bob_alice_ready_button.pack()

        self.bob_label.config(state="disabled")
        self.alice_label.config(state="disabled")
        self.shared_title_label.config(state="disabled")

        self.bob_shared_x_val_str.set("")
        self.bob_shared_y_val_str.set("")
        self.bob_shared_label.configure(state="disabled")
        self.bob_shared_x_label.config(state="disabled")
        self.bob_shared_x_val_label.config(state="disabled")
        self.bob_shared_y_label.config(state="disabled")
        self.bob_shared_y_val_label.config(state="disabled")

        self.alice_shared_x_val_str.set("")
        self.alice_shared_y_val_str.set("")
        self.alice_shared_label.configure(state="disabled")
        self.alice_shared_x_label.config(state="disabled")
        self.alice_shared_x_val_label.config(state="disabled")
        self.alice_shared_y_label.config(state="disabled")
        self.alice_shared_y_val_label.config(state="disabled")

    def bob_alice_clear_and_disable(self):
        self.key_gen_label.config(state="disabled")
        self.bob_alice_label.config(state="disabled")

        self.bob_title.config(state="disabled")
        self.bob_pub_label.config(state="disabled")
        self.bob_priv_label.config(state="disabled")
        self.bob_priv_entry.config(state="normal")
        self.bob_priv_entry.delete(0, "end")
        self.bob_priv_entry.config(state="disabled")

        self.bob_pub_x_label.config(state="disabled")
        self.bob_pub_x_val_str.set("")
        self.bob_pub_x_val_label.config(state="disabled")
        self.bob_pub_y_label.config(state="disabled")
        self.bob_pub_y_val_str.set("")
        self.bob_pub_y_val_label.config(state="disabled")

        self.alice_title.config(state="disabled")
        self.alice_pub_label.config(state="disabled")
        self.alice_priv_label.config(state="disabled")
        self.alice_priv_entry.config(state="normal")
        self.alice_priv_entry.delete(0, "end")
        self.alice_priv_entry.config(state="disabled")

        self.alice_pub_x_label.config(state="disabled")
        self.alice_pub_x_val_str.set("")
        self.alice_pub_x_val_label.config(state="disabled")
        self.alice_pub_y_label.config(state="disabled")
        self.alice_pub_y_val_str.set("")
        self.alice_pub_y_val_label.config(state="disabled")

        self.bob_alice_edit_button.pack_forget()
        self.bob_alice_txt.set("")
        self.bob_alice_image_ok.pack_forget()
        self.bob_alice_err_txt.set("")
        self.bob_alice_error_frame.config(height=1)
        self.bob_alice_image_err.pack_forget()
        self.bob_alice_ready_button.pack()
        self.bob_alice_ready_button.config(state="disabled")

        self.bob = None
        self.alice = None
        self.ecdh = None
        self.bob_alice_edit_button.pack_forget()
        self.bob_alice_image_ok.pack_forget()
        self.bob_alice_ready_button.pack()

        self.privkey_autogen_btn.config(state="disabled")

        self.bob_label.config(state="disabled")
        self.alice_label.config(state="disabled")
        self.shared_title_label.config(state="disabled")

        self.bob_shared_x_val_str.set("")
        self.bob_shared_y_val_str.set("")
        self.bob_shared_label.configure(state="disabled")
        self.bob_shared_x_label.config(state="disabled")
        self.bob_shared_x_val_label.config(state="disabled")
        self.bob_shared_y_label.config(state="disabled")
        self.bob_shared_y_val_label.config(state="disabled")

        self.alice_shared_x_val_str.set("")
        self.alice_shared_y_val_str.set("")
        self.alice_shared_label.configure(state="disabled")
        self.alice_shared_x_label.config(state="disabled")
        self.alice_shared_x_val_label.config(state="disabled")
        self.alice_shared_y_label.config(state="disabled")
        self.alice_shared_y_val_label.config(state="disabled")

    def chosen_curve(self):
        self.predef_curve = cons.get_curve(self.dropdown_str.get())
        self.isPredefined = True

        self.ec_a_entry.delete(0, "end")
        self.ec_a_entry.insert(0, self.predef_curve["a"])

        self.ec_b_entry.delete(0, "end")
        self.ec_b_entry.insert(0, self.predef_curve["b"])

        self.ec_q_entry.delete(0, "end")
        self.ec_q_entry.insert(0, self.predef_curve["q"])

    def chosen_point(self):
        self.g = self.gen_points_dict[self.g_dropdown_str.get()]

        self.g_x_entry.delete(0, "end")
        self.g_x_entry.insert(0, self.g.get_x())

        self.g_y_entry.delete(0, "end")
        self.g_y_entry.insert(0, self.g.get_y())

    def priv_key_autogen(self):
        self.bob_priv_entry.delete(0, "end")
        self.bob_priv_entry.insert(0, rand.randint(1, self.elliptic_curve.get_n()-1))

        self.alice_priv_entry.delete(0, "end")
        self.alice_priv_entry.insert(0, rand.randint(1, self.elliptic_curve.get_n()-1))

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
