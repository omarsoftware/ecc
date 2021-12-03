import tkinter as tk
import constants as cons
import ecmath as ec
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

        self.title = tk.Label(self.frame, text='Diffie-Hellman con Curva Elíptica', font='Helvetica 16 bold')
        self.title.pack(fill="x")

        # ///////////// Begin Elliptic Curve /////////////
        self.ec_frame = tk.Frame(self.frame)
        self.ec_title = tk.Label(self.ec_frame)
        self.ec_gen_eq = tk.StringVar()
        self.ec_gen_eq_label = tk.Label(self.ec_frame)

        # begin predfined curves dropdown
        self.dropdown_frame = tk.Frame(self.frame)
        self.predef_curve = None
        self.curves_list = cons.get_predef_curves_names()
        self.dropdown_str = tk.StringVar()
        self.dropdown_str.set(self.curves_list[0])
        self.predef_dropdown = tk.OptionMenu(self.dropdown_frame, self.dropdown_str, *self.curves_list)
        self.button_chosen_curve = tk.Button(self.dropdown_frame, text="Seleccionar", command=lambda: self.chosen_curve())
        # end predfined curves dropdown

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
        self.ec_resized = self.ec_load_ok.resize((20, 20), Image.ANTIALIAS)
        self.ec_new_pic_ok = ImageTk.PhotoImage(self.ec_resized)
        self.ec_image_ok = tk.Label(self.ec_ready_frame, image=self.ec_new_pic_ok)

        self.ec_error_frame = tk.Frame(self.frame)
        self.ec_load_err = Image.open(cons.x_path)
        self.ec_resized_err = self.ec_load_err.resize((20, 20), Image.ANTIALIAS)
        self.ec_new_pic_err = ImageTk.PhotoImage(self.ec_resized_err)
        self.ec_image_err = tk.Label(self.ec_error_frame, image=self.ec_new_pic_err)
        self.ec_err_text = tk.StringVar()
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
        self.g_resized = self.g_load_ok.resize((20, 20), Image.ANTIALIAS)
        self.g_new_pic_ok = ImageTk.PhotoImage(self.g_resized)
        self.g_image_ok = tk.Label(self.g_ready_frame, image=self.g_new_pic_ok)

        self.g_error_frame = tk.Frame(self.frame)
        self.g_label = tk.Label(self.g_error_frame)
        self.g_err_txt = tk.StringVar()
        self.g_err = tk.Label(self.g_error_frame)
        self.g_load_err = Image.open(cons.x_path)
        self.g_resized_err = self.g_load_err.resize((20, 20), Image.ANTIALIAS)
        self.g_new_pic_err = ImageTk.PhotoImage(self.g_resized_err)
        self.g_image_err = tk.Label(self.g_error_frame, image=self.g_new_pic_err)

        self.g_set()
        # ///////////// End Generator Point /////////////

        # ///////////// Begin Key Generation /////////////
        self.key_gen_label = tk.Label(self.frame, text="Paso 3: generación de claves públicas y privadas", state='disabled', font='Helvetica 10 bold')
        self.key_gen_label.pack()

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
        self.bob_alice_text = tk.StringVar()
        self.bob_alice_label = tk.Label(self.frame, textvariable=self.bob_alice_text)
        self.bob_alice_label.pack()

        self.bob_alice_ready_frame = tk.Frame(self.frame)
        self.bob_alice_ready_button = tk.Button(self.bob_alice_ready_frame)
        self.bob_alice_edit_button = tk.Button(self.bob_alice_ready_frame)
        self.bob_alice_load_ok = Image.open(cons.check_path)
        self.bob_alice_resized = self.bob_alice_load_ok.resize((20, 20), Image.ANTIALIAS)
        self.bob_alice_new_pic_ok = ImageTk.PhotoImage(self.bob_alice_resized)
        self.bob_alice_image_ok = tk.Label(self.bob_alice_ready_frame, image=self.bob_alice_new_pic_ok)

        self.bob_alice_error_frame = tk.Frame(self.frame)
        self.bob_alice_label = tk.Label(self.bob_alice_error_frame)
        self.bob_alice_err_txt = tk.StringVar()
        self.bob_alice_err = tk.Label(self.bob_alice_error_frame)
        self.bob_alice_load_err = Image.open(cons.x_path)
        self.bob_alice_resized_err = self.bob_alice_load_err.resize((20, 20), Image.ANTIALIAS)
        self.bob_alice_new_pic_err = ImageTk.PhotoImage(self.bob_alice_resized_err)
        self.bob_alice_image_err = tk.Label(self.bob_alice_error_frame, image=self.bob_alice_new_pic_err)

        self.bob_alice_set()
        # ///////////// Begin of End for Bob and Alice /////////////

        # ///////////// End Key Generation /////////////

        # ///////////// Begin Shared Calculations /////////////
        self.shared_title_label = tk.Label(self.frame, text="Paso 4: generación de clave compartida por Alicia y Bob",
                                    state="disabled", font='Helvetica 10 bold')
        self.shared_title_label.pack()

        self.shared_bob = tk.Label(self.frame, text="Clave compartida calculada por Bob: ", state="disabled")
        self.shared_bob.pack()
        self.shared_bob_text = tk.StringVar()
        self.shared_bob_label = tk.Label(self.frame, textvariable=self.shared_bob_text)
        self.shared_bob_label.pack()

        self.shared_alice = tk.Label(self.frame, text="Clave compartida calculada por Alicia: ", state="disabled")
        self.shared_alice.pack()
        self.shared_alice_text = tk.StringVar()
        self.shared_alice_label = tk.Label(self.frame, textvariable=self.shared_alice_text, state="disabled")
        self.shared_alice_label.pack()

        # ///////////// End Shared Calculations /////////////

    def chosen_curve(self):
        self.predef_curve = cons.get_curve(self.dropdown_str.get())
        self.isPredefined = True

        self.ec_a_entry.delete(0, "end")
        self.ec_a_entry.insert(0, self.predef_curve["a"])

        self.ec_b_entry.delete(0, "end")
        self.ec_b_entry.insert(0, self.predef_curve["b"])

        self.ec_q_entry.delete(0, "end")
        self.ec_q_entry.insert(0, self.predef_curve["q"])

        # self.elliptic_curve = ec.EllipticCurve(self.predef_curve["a"], self.predef_curve["b"], self.predef_curve["q"])


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

        self.ec_err_label.config(textvariable=self.ec_err_text)
        self.ec_image_err.pack(side="left")
        self.ec_image_err.pack_forget()
        self.ec_err_label.pack(side="left")
        self.ec_err_label.pack_forget()
        self.ec_error_frame.pack()

    def ec_ready(self):
        try:
            a = int(self.ec_a_entry.get())
            b = int(self.ec_b_entry.get())
            q = int(self.ec_q_entry.get())

            if self.isPredefined:
                self.elliptic_curve = ec.EllipticCurve(self.predef_curve["a"], self.predef_curve["b"],
                                                       self.predef_curve["q"],
                                                       ec.Point(self.predef_curve["g"][0], self.predef_curve["g"][1]))
            else:
                self.elliptic_curve = ec.EllipticCurve(a, b, q)

            if not self.elliptic_curve.isNonSingular():
                text = "curva elíptica singular"
                self.ec_err_text.set(text)
                self.ec_image_err.pack(side="left")
                self.ec_err_label.pack(side="left")
                self.ec_error_frame.pack()
                raise ValueError("elliptic-curve is singular")

            self.ec_a_entry.config(state="disabled")
            self.ec_b_entry.config(state="disabled")
            self.ec_q_entry.config(state="disabled")

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

            self.g_x_entry.delete(0, "end")
            self.g_x_entry.insert(0, self.elliptic_curve.get_g().get_x())
            self.g_y_entry.delete(0, "end")
            self.g_y_entry.insert(0, self.elliptic_curve.get_g().get_y())

        except Exception as msg:
            self.err_display(msg.args[0], self.ec_err_text, self.ec_image_err, self.ec_err_label, self.ec_error_frame)
            '''
            text = msg.args[0]
            self.ec_err_text.set(text)
            self.ec_image_err.pack(side="left")
            self.ec_err_label.pack(side="left")
            self.ec_error_frame.pack()
            '''

    def err_display(self, text, err_text, image_err, err_label, error_frame):
        err_text.set(text)
        image_err.pack(side="left")
        err_label.pack(side="left")
        error_frame.pack()

    def ec_clear(self):
        self.ec_a_entry.config(state="normal")
        self.ec_a_entry.delete(0, 'end')
        self.ec_b_entry.config(state="normal")
        self.ec_b_entry.delete(0, 'end')
        self.ec_q_entry.config(state="normal")
        self.ec_q_entry.delete(0, 'end')
        self.ec_title.pack()
        self.ec_err_text.set("")
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
        x_str = self.g_x_entry.get()
        y_str = self.g_y_entry.get()
        try:
            if x_str == '' or y_str == '':
                text = "x o y están vacíos"
                self.g_err_txt.set(text)
                self.g_image_err.pack(side="left")
                self.g_err.pack(side="left")
                self.g_error_frame.pack()
                raise ValueError("Empty input")

            if not x_str.lstrip('-').isnumeric() or not y_str.lstrip('-').isnumeric():
                text = "x e y deben ser números"
                self.g_err_txt.set(text)
                self.g_image_err.pack(side="left")
                self.g_err.pack(side="left")
                self.g_error_frame.pack()
                raise ValueError("Input must be numeric")

            self.g = ec.Point(int(x_str), int(y_str))

            if not self.elliptic_curve.belongsToCurve(self.g):
                text = "El punto no pertenece a la curva"
                self.g_err_txt.set(text)
                self.g_image_err.pack(side="left")
                self.g_err.pack(side="left")
                self.g_error_frame.pack()
                raise ValueError("Point does not belong to curve")

        except TypeError:
            text = "Ingreso inválido"
            self.g_err_txt.set(text)
            self.g_image_err.pack(side="left")
            self.g_err.pack(side="left")
            self.g_error_frame.pack()
            raise ValueError("invalid input")

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

    def g_clear(self):
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

    def bob_alice_ready(self):
        self.bob_alice_text.set("")
        bob_priv_str = self.bob_priv_entry.get()
        alice_priv_str = self.alice_priv_entry.get()

        try:
            if bob_priv_str == '' or alice_priv_str == '':
                text = "clave/s privada/s sin completar"
                self.bob_alice_err_txt.set(text)
                self.bob_alice_image_err.pack(side="left")
                self.bob_alice_err.pack(side="left")
                self.bob_alice_error_frame.pack()
                raise ValueError("Empty input")

            if not bob_priv_str.lstrip('-').isnumeric() or not alice_priv_str.lstrip('-').isnumeric():
                text = "clave/s privada/s deben ser números"
                self.bob_alice_err_txt.set(text)
                self.bob_alice_image_err.pack(side="left")
                self.bob_alice_err.pack(side="left")
                self.bob_alice_error_frame.pack()
                raise ValueError("Input must be numeric")

            self.bob_alice_ready_button.pack_forget()
            self.bob_alice_edit_button.pack(side="left")
            self.bob_alice_image_ok.pack(side="right")
            self.bob_alice_err.pack_forget()
            self.bob_alice_image_err.pack_forget()
            self.bob_alice_error_frame.configure(height=1)

            self.bob = ec.User()
            self.alice = ec.User()
            self.ecdh = ec.ECDH(self.elliptic_curve)

            bob_priv = int(bob_priv_str)
            alice_priv = int(alice_priv_str)

            self.bob.setPrivKey(bob_priv)
            # self.bob.setPubKey(self.elliptic_curve.point_mult(self.g, self.bob.getPrivKey()))
            self.bob.setPubKey(self.ecdh.gen_pub_key(self.bob.getPrivKey()))
            self.bob_pub_x_label.config(state="normal")
            self.bob_pub_x_val_str.set(self.bob.getPubKey().get_x())
            self.bob_pub_x_val_label.config(state="normal")
            self.bob_pub_y_label.config(state="normal")
            self.bob_pub_y_val_str.set(self.bob.getPubKey().get_y())
            self.bob_pub_y_val_label.config(state="normal")

            self.alice.setPrivKey(alice_priv)
            # self.alice.setPubKey(self.elliptic_curve.point_mult(self.g, self.alice.getPrivKey()))
            self.alice.setPubKey(self.ecdh.gen_pub_key(self.alice.getPrivKey()))
            self.alice_pub_x_label.config(state="normal")
            self.alice_pub_x_val_str.set(self.alice.getPubKey().get_x())
            self.alice_pub_x_val_label.config(state="normal")
            self.alice_pub_y_label.config(state="normal")
            self.alice_pub_y_val_str.set(self.alice.getPubKey().get_y())
            self.alice_pub_y_val_label.config(state="normal")

            self.shared_bob_text.set(
                self.ecdh.calc_shared_key(self.bob.getPrivKey(), self.alice.getPubKey()).print())
            self.shared_alice_text.set(
                self.ecdh.calc_shared_key(self.alice.getPrivKey(), self.bob.getPubKey()).print())

        except TypeError:
            text = "Ingreso inválido"
            self.bob_alice_err_txt.set(text)
            self.bob_alice_image_err.pack(side="left")
            self.bob_alice_err.pack(side="left")
            self.bob_alice_error_frame.pack()
            raise ValueError("invalid input")

        self.bob_priv_entry.config(state="disabled")
        self.alice_priv_entry.config(state="disabled")
        self.bob_alice_ready_button.pack_forget()
        self.bob_alice_edit_button.pack()
        self.bob_alice_label.config(state="normal")

        self.shared_title_label.config(state="normal")
        self.shared_alice_label.config(state="normal")
        self.shared_alice.config(state="normal")
        self.shared_bob_label.config(state="normal")
        self.shared_bob.config(state="normal")        

    def bob_alice_clear(self):
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
        self.shared_bob_text.set("")
        self.shared_alice_text.set("")
        self.shared_title_label.config(state="disabled")
        self.shared_bob.config(state="disabled")
        self.shared_alice.config(state="disabled")
        self.bob_label.config(state="disabled")
        self.alice_label.config(state="disabled")

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
        self.bob_alice_text.set("")
        self.bob_alice_image_ok.pack_forget()
        self.bob_alice_err_txt.set("")
        self.bob_alice_error_frame.config(height=1)
        self.bob_alice_image_err.pack_forget()
        self.bob_alice_ready_button.pack()
        self.bob_alice_ready_button.config(state="disabled")

        self.bob = None
        self.alice = None
        self.ecdh = None
        self.shared_title_label.config(state="disabled")
        self.shared_bob.config(state="disabled")
        self.shared_alice.config(state="disabled")
        self.bob_label.config(state="disabled")
        self.alice_label.config(state="disabled")
        self.shared_bob_text.set("")
        self.shared_alice_text.set("")
        self.bob_pub_label.config(state="disabled")
        self.alice_pub_label.config(state="disabled")

    def start_page(self):
        self.frame.grid(column=0, row=0, sticky="NWES")

    def go_back(self):
        self.frame.pack_forget()
        self.app.main_page()

    def get_frame(self):
        return self.frame
