import tkinter as tk
import constants as cons
import ecmath as ec

class Ecdh:
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master)
        self.elliptic_curve = None
        self.g = None
        self.bob = None
        self.alice = None

        title = tk.Label(self.frame, text='Diffie-Hellman con curva elíptica')
        title.grid(row=0, column=0, sticky="W")

        blank1 = tk.Label(self.frame, text='       ')
        blank1.grid(row=1, column=0)

        # ///////////// Begin Elliptic Curve /////////////
        self.ec_title = tk.Label(self.frame)
        self.ec_gen_eq = tk.StringVar()
        self.ec_gen_eq_label = tk.Label(self.frame)
        self.ec_frame = tk.Frame(self.frame)
        self.ec_a_label = tk.Label(self.ec_frame)
        self.ec_a_entry = tk.Entry(self.ec_frame)
        self.ec_b_label = tk.Label(self.ec_frame)
        self.ec_b_entry = tk.Entry(self.ec_frame)
        self.ec_q_label = tk.Label(self.ec_frame)
        self.ec_q_entry = tk.Entry(self.ec_frame)
        self.ec_ready_button = tk.Button(self.frame)
        self.ec_eq_text = tk.StringVar()
        self.ec_eq = tk.Label(self.frame)
        self.ec_edit_button = tk.Button(self.frame)
        self.ec_set()
        # ///////////// End Elliptic Curve /////////////

        blank2 = tk.Label(self.frame, text='       ')
        blank2.grid(row=6, column=0)

        # ///////////// Begin Generator Point /////////////
        self.g_title = tk.Label(self.frame)
        self.g_frame = tk.Frame(self.frame)
        self.g_x_label = tk.Label(self.g_frame)
        self.g_x_entry = tk.Entry(self.g_frame)
        self.g_y_label = tk.Label(self.g_frame)
        self.g_y_entry = tk.Entry(self.g_frame)
        self.g_ready_button = tk.Button(self.frame)
        self.g_text = tk.StringVar()
        self.g_label = tk.Label(self.frame)
        self.g_edit_button = tk.Button(self.frame)
        self.g_set()
        # ///////////// End Generator Point /////////////

        blank3 = tk.Label(self.frame, text='       ')
        blank3.grid(row=11, column=0)

        # ///////////// Begin Key Generation /////////////
        self.key_gen_label = tk.Label(self.frame, text="Paso 3: generación de claves públicas y privadas",state='disabled')
        self.key_gen_label.grid(row=12, column=0)

        # ///////////// Begin Bob /////////////
        self.bob_title = tk.Label(self.frame)
        self.bob_priv_label = tk.Label(self.frame)
        self.bob_priv_entry = tk.Entry(self.frame)
        self.bob_pub_label = tk.Label(self.frame)
        self.bob_pub_text = tk.StringVar()
        self.bob_label = tk.Label(self.frame)
        self.bob_set()
        # ///////////// End Bob /////////////

        blank4 = tk.Label(self.frame, text='       ')
        blank4.grid(row=16, column=0)

        # ///////////// Begin Alice /////////////
        self.alice_title = tk.Label(self.frame)
        self.alice_priv_label = tk.Label(self.frame)
        self.alice_priv_entry = tk.Entry(self.frame)
        self.alice_pub_label = tk.Label(self.frame)
        self.alice_pub_text = tk.StringVar()
        self.alice_label = tk.Label(self.frame)
        self.alice_set()
        # ///////////// End Alice /////////////

        self.bob_alice_ready_button = tk.Button(self.frame, text="Listo", command=lambda: self.bob_alice_ready(), state="disabled")
        self.bob_alice_ready_button.grid(row=20, column=0)

        self.bob_alice_text = tk.StringVar()
        self.bob_alice_label = tk.Label(self.frame, textvariable=self.bob_alice_text)
        self.bob_alice_label.grid(row=20, column=1)

        # ///////////// End Alice /////////////

        self.bob_alice_edit_button = tk.Button(self.frame, text="Editar", command=lambda: self.bob_alice_clear())
        self.bob_alice_edit_button.grid_forget()

        # ///////////// End Key Generation /////////////

        blank5 = tk.Label(self.frame, text='       ')
        blank5.grid(row=21, column=0)

        # ///////////// Begin Shared Calculations /////////////
        self.shared_title_label = tk.Label(self.frame, text="Paso 4: generación de clave compartida por Alicia y Bob",
                                    state="disabled")
        self.shared_title_label.grid(row=22, column=0)

        self.shared_bob = tk.Label(self.frame, text="Clave compartida calculada por Bob: ", state="disabled")
        self.shared_bob.grid(row=23, column=0)
        self.shared_bob_text = tk.StringVar()
        self.shared_bob_label = tk.Label(self.frame, textvariable=self.shared_bob_text)
        self.shared_bob_label.grid(row=23, column=1)

        self.shared_alice = tk.Label(self.frame, text="Clave compartida calculada por Alicia: ", state="disabled")
        self.shared_alice.grid(row=24, column=0)
        self.shared_alice_text = tk.StringVar()
        self.shared_alice_label = tk.Label(self.frame, textvariable=self.shared_alice_text, state="disabled")
        self.shared_alice_label.grid(row=24, column=1)


        # ///////////// End Shared Calculations /////////////

    def ec_set(self):
        self.ec_title.config(text='Paso 1: elegir curva elíptica utilizada por Bob y Alicia')
        self.ec_title.grid(row=2, column=0, sticky="W")

        self.ec_gen_eq.set("y\u00B2 = x\u00B3 + ax + b mod q")
        self.ec_gen_eq_label.config(textvariable=self.ec_gen_eq)
        self.ec_gen_eq_label.grid(row=3, column=0)

        self.ec_a_label.config(text="a =")
        self.ec_a_label.pack(side="left")
        self.ec_a_entry.config(width=5)
        self.ec_a_entry.pack(side="left")

        self.ec_b_label.config(text="b =")
        self.ec_b_label.pack(side="left")
        self.ec_b_entry.config(width=5)
        self.ec_b_entry.pack(side="left")

        self.ec_q_label.config(text="q =")
        self.ec_q_label.pack(side="left")
        self.ec_q_entry.config(width=5)
        self.ec_q_entry.pack(side="left")

        self.ec_frame.grid(row=4, column=0)

        self.ec_ready_button.config(text="Listo", command=lambda: self.ec_ready())
        self.ec_ready_button.grid(row=5, column=0)

        self.ec_eq.grid(row=5, column=1)

        self.ec_eq.config(textvariable=self.ec_eq_text)

        self.ec_edit_button.config(text="Editar", command=lambda: self.ec_clear())
        self.ec_edit_button.grid_forget()

    def ec_ready(self):
        try:
            a_str = self.ec_a_entry.get()
            b_str = self.ec_b_entry.get()
            q_str = self.ec_q_entry.get()

            if a_str == '' or b_str == '' or q_str == '':
                text = "a, b o q están vacíos"
                self.ec_eq_text.set(text)
                raise ValueError("Empty input")

            if not a_str.lstrip('-').isnumeric() or not b_str.lstrip('-').isnumeric():
                text = "a y b deben ser números"
                self.ec_eq_text.set(text)
                raise ValueError("Input must be numeric")

            if not q_str.isdigit():
                text = "q debe ser positivo"
                self.ec_eq_text.set(text)
                raise ValueError("Input must be numeric")

            a = int(a_str)
            b = int(b_str)
            q = int(q_str)
            self.elliptic_curve = ec.EllipticCurve(a, b, q)
            if not self.elliptic_curve.isNonSingular():
                text = "curva elíptica singular"
                self.ec_eq_text.set(text)
                raise ValueError("elliptic-curve is singular")

        except TypeError:
            text = "Ingreso inválido"
            self.ec_eq_text.set(text)
            raise ValueError("invalid input")

        self.ec_eq_text.set(self.elliptic_curve.print())
        self.ec_a_entry.config(state="disabled")
        self.ec_b_entry.config(state="disabled")
        self.ec_q_entry.config(state="disabled")

        self.ec_ready_button.grid_forget()
        self.ec_edit_button.grid(row=5, column=0)

        self.g_title.config(state='normal')
        self.g_x_label.config(state='normal')
        self.g_y_label.config(state='normal')
        self.g_x_entry.config(state='normal')
        self.g_y_entry.config(state='normal')
        self.g_ready_button.config(state='normal')

    def ec_clear(self):
        self.ec_a_entry.config(state="normal")
        self.ec_a_entry.delete(0, 'end')
        self.ec_b_entry.config(state="normal")
        self.ec_b_entry.delete(0, 'end')
        self.ec_q_entry.config(state="normal")
        self.ec_q_entry.delete(0, 'end')
        self.ec_title.grid(row=2, column=0, sticky="W")
        self.ec_eq_text.set("")
        self.ec_ready_button.grid(row=5, column=0)
        self.ec_eq.grid(row=5, column=1)
        self.ec_edit_button.grid_forget()
        self.elliptic_curve = None

        self.g_clear_and_disable()
        self.bob_alice_clear_and_disable()

    def g_set(self):
        self.g_title.config(text="Paso 2: elegir punto generador utilizado por Bob y Alicia", state="disabled")
        self.g_title.grid(row=7, column=0)

        self.g_x_label.config(text="x =", state="disabled")
        self.g_x_label.pack(side="left")
        self.g_x_entry.config(width=5, state="disabled")
        self.g_x_entry.pack(side="left")

        self.g_y_label.config(text="y =", state="disabled")
        self.g_y_label.pack(side="left")
        self.g_y_entry.config(width=5, state="disabled")
        self.g_y_entry.pack(side="left")

        self.g_frame.grid(row=8, column=0)

        self.g_ready_button.config(text="Listo", state="disabled", command=lambda: self.g_ready())
        self.g_ready_button.grid(row=9, column=0)

        self.g_label.config(textvariable=self.g_text)
        self.g_label.grid(row=9, column=1)

        self.g_edit_button.config(text="Editar", command=lambda: self.g_clear())
        self.g_edit_button.grid_forget()

    def g_ready(self):
        x_str = self.g_x_entry.get()
        y_str = self.g_y_entry.get()
        try:

            if x_str == '' or y_str == '':
                text = "x o y están vacíos"
                self.g_text.set(text)
                raise ValueError("Empty input")

            if not x_str.lstrip('-').isnumeric() or not y_str.lstrip('-').isnumeric():
                text = "x e y deben ser números"
                self.g_text.set(text)
                raise ValueError("Input must be numeric")

            self.g = ec.Point(int(x_str), int(y_str))
            if not self.elliptic_curve.belongsToCurve(self.g):
                text = "El punto no pertenece a la curva"
                self.g_text.set(text)
                raise ValueError("Point does not belong to curve")

        except TypeError:
            text = "Ingreso inválido"
            self.g_text.set(text)
            raise ValueError("invalid input")

        text = "G = "+self.g.print()
        self.g_text.set(text)

        self.g_x_entry.config(state="disabled")
        self.g_y_entry.config(state="disabled")

        self.g_ready_button.grid_forget()
        self.g_edit_button.grid(row=9, column=0)

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
        self.g_ready_button.grid(row=9, column=0)
        self.g_edit_button.grid_forget()
        self.g_text.set("")
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
        self.g_ready_button.grid(row=9, column=0)
        self.g_edit_button.grid_forget()
        self.g_text.set("")
        self.g = None

    def bob_set(self):
        self.bob_title.config(text="Bob", state="disabled")
        self.bob_title.grid(row=13, column=0)
        self.bob_priv_label.config(text="Clave Privada:", state="disabled")
        self.bob_priv_label.grid(row=14, column=0)
        self.bob_priv_entry.config(state="disabled")
        self.bob_priv_entry.grid(row=14, column=1)
        self.bob_pub_label.config(text="Clave Pública:", state="disabled")
        self.bob_pub_label.grid(row=15, column=0)
        self.bob_label.config(textvariable=self.bob_pub_text, state="disabled")
        self.bob_label.grid(row=15, column=1)

    def alice_set(self):
        self.alice_title.config(text="Alicia", state="disabled")
        self.alice_title.grid(row=17, column=0)
        self.alice_priv_label.config(text="Clave Privada:", state="disabled")
        self.alice_priv_label.grid(row=18, column=0)
        self.alice_priv_entry.config(state="disabled")
        self.alice_priv_entry.grid(row=18, column=1)
        self.alice_pub_label.config(text="Clave Pública:", state="disabled")
        self.alice_pub_label.grid(row=19, column=0)
        self.alice_label.config(textvariable=self.alice_pub_text, state="disabled")
        self.alice_label.grid(row=19, column=1)

    def bob_alice_ready(self):
        self.bob_alice_text.set("")
        bob_priv_str = self.bob_priv_entry.get()
        alice_priv_str = self.alice_priv_entry.get()

        try:
            if bob_priv_str == '' or alice_priv_str == '':
                text = "clave/s privada/s sin completar"
                self.bob_alice_text.set(text)
                raise ValueError("Empty input")

            if not bob_priv_str.lstrip('-').isnumeric() or not alice_priv_str.lstrip('-').isnumeric():
                text = "clave/s privada/s deben ser números"
                self.bob_alice_text.set(text)
                raise ValueError("Input must be numeric")

            self.bob = ec.User()
            self.alice = ec.User()

            bob_priv = int(bob_priv_str)
            alice_priv = int(alice_priv_str)

            self.bob.setPrivKey(bob_priv)
            self.bob.setPubKey(self.elliptic_curve.point_mult(self.g, self.bob.getPrivKey()))
            self.bob_pub_text.set(self.bob.getPubKey().print())

            self.alice.setPrivKey(alice_priv)
            self.alice.setPubKey(self.elliptic_curve.point_mult(self.g, self.alice.getPrivKey()))
            self.alice_pub_text.set(self.alice.getPubKey().print())

            self.shared_bob_text.set(
                self.elliptic_curve.point_mult(self.alice.getPubKey(), self.bob.getPrivKey()).print())
            self.shared_alice_text.set(
                self.elliptic_curve.point_mult(self.bob.getPubKey(), self.alice.getPrivKey()).print())

        except TypeError:
            text = "Ingreso inválido"
            self.g_text.set(text)
            raise ValueError("invalid input")

        self.bob_priv_entry.config(state="disabled")
        self.alice_priv_entry.config(state="disabled")
        self.bob_alice_ready_button.grid_forget()
        self.bob_alice_edit_button.grid(row=20, column=0)
        self.bob_alice_label.config(state="normal")

        self.shared_title_label.config(state="normal")
        self.shared_alice_label.config(state="normal")
        self.shared_alice.config(state="normal")
        self.shared_bob_label.config(state="normal")
        self.shared_bob.config(state="normal")        

    def bob_alice_clear(self):
        self.bob_priv_entry.config(state="normal")
        self.bob_priv_entry.delete(0, "end")
        self.bob_pub_text.set("")
        self.alice_priv_entry.config(state="normal")
        self.alice_priv_entry.delete(0, "end")
        self.alice_pub_text.set("")
        self.bob = None
        self.alice = None
        self.bob_alice_edit_button.grid_forget()
        self.bob_alice_ready_button.grid(row=20, column=0)
        self.shared_bob_text.set("")
        self.shared_alice_text.set("")

    def bob_alice_clear_and_disable(self):
        self.key_gen_label.config(state="disabled")
        self.bob_alice_label.config(state="disabled")
        self.bob_title.config(state="disabled")
        self.bob_label.config(state="disabled")
        self.bob_priv_label.config(state="disabled")
        self.bob_priv_entry.config(state="normal")
        self.bob_priv_entry.delete(0, "end")
        self.bob_priv_entry.config(state="disabled")
        self.alice_title.config(state="disabled")
        self.alice_label.config(state="disabled")
        self.alice_priv_label.config(state="disabled")
        self.alice_priv_entry.config(state="normal")
        self.alice_priv_entry.delete(0, "end")
        self.alice_priv_entry.config(state="disabled")
        self.bob_alice_edit_button.grid_forget()
        self.bob_alice_text.set("")
        self.bob_alice_ready_button.grid(row=20, column=0)
        self.bob_alice_ready_button.config(state="disabled")
        self.bob = None
        self.alice = None
        self.shared_title_label.config(state="disabled")
        self.shared_bob.config(state="disabled")
        self.shared_alice.config(state="disabled")
        self.bob_pub_text.set("")
        self.alice_pub_text.set("")
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

'''
class Ecdh:

    def __init__(self, frame):
        self.frame = frame

    def display(self):
        ecdh_label = Label(self.frame, text="Elliptic-Curve Diffie-Hellman algorithm").pack()
        self.frame.pack(fill="both", expand=1)

    def print(self):
        print("Operaciones de Puntos:")
        curve = EllipticCurve(-7, 10)
        p = Point(1, 2)
        # q = Point(3, 4)
        r = curve.point_mult(p, 4)
        print("-------")
        print(r.get_x())
        print("-------")
        print(r.get_y())
        print("////////////////////////")
        print("ECDH:")
        bob = User()
        alice = User()
        g = Point(1, 2)
        print("El punto generador G es:")
        print(g.print())
        print("-------")

        print("Clave PRIVADA de Alice:")
        alice.setPrivKey(6)
        print(alice.getPrivKey())
        print("Clave PÚBLICA de Alice:")
        alice.setPubKey(curve.point_mult(g, alice.getPrivKey()))
        print(alice.getPubKey().print())
        print("-------")

        print("Clave PRIVADA de Bob:")
        bob.setPrivKey(8)
        print(bob.getPrivKey())
        print("Clave PÚBLICA de Bob:")
        bob.setPubKey(curve.point_mult(g, bob.getPrivKey()))
        print(bob.getPubKey().print())
        print("-------")

        print("Clave COMPARTIDA calculada por ALICE:")
        print(curve.point_mult(bob.getPubKey(), alice.getPrivKey()).print())
        print("-------")

        print("Clave COMPARTIDA calculada por BOB:")
        print(curve.point_mult(alice.getPubKey(), bob.getPrivKey()).print())
        print("-------")
        '''
