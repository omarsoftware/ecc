import tkinter as tk
import constants as cons
import ecmath as ec

class Ecdh:
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master)
        self.elliptic_curve = None
        self.g = ec.Point()

        # ///////////// Begin Elliptic Curve /////////////
        title = tk.Label(self.frame, text='Elliptic-curve Diffie-Hellman')
        title.grid(row=0, column=0, sticky="W")

        blank = tk.Label(self.frame, text='       ')
        blank.grid(row=1, column=0)

        shared_label = tk.Label(self.frame, text='Step 1: choose the elliptic curve to be used by both Bob and Alice')
        shared_label.grid(row=2, column=0, sticky="W")

        self.ec_gen_eq = tk.StringVar()
        self.ec_gen_eq.set("y\u00B2 = x\u00B3 + ax + b")
        self.ec_ge_eq_label = tk.Label(self.frame, textvariable=self.ec_gen_eq)
        self.ec_ge_eq_label.grid(row=3, column=0)

        self.ec_frame = tk.Frame(self.frame)
        ec_label_1 = tk.Label(self.ec_frame, text="a =")
        ec_label_1.pack(side=tk.LEFT)
        self.ec_a = tk.Entry(self.ec_frame, width=5)
        self.ec_a.pack(side=tk.LEFT)
        ec_label_2 = tk.Label(self.ec_frame, text="b =")
        ec_label_2.pack(side=tk.LEFT)
        self.ec_b = tk.Entry(self.ec_frame, width=5)
        self.ec_b.pack(side=tk.LEFT)
        self.ec_frame.grid(row=4, column=0)

        self.button_ready_1 = tk.Button(self.frame, text="Done", command=lambda: self.ec_ready())
        self.button_ready_1.grid(row=5, column=0)

        self.ec_eq_text = tk.StringVar()
        self.ec_eq = tk.Label(self.frame, textvariable=self.ec_eq_text)
        self.ec_eq.grid(row=5, column=1)

        self.button_edit_1 = tk.Button(self.frame, text="Edit", command=lambda: self.ec_edit())
        self.button_edit_1.grid(row=5, column=2)
        self.button_edit_1.grid_forget()

        # ///////////// End Elliptic Curve /////////////

        blank2 = tk.Label(self.frame, text='       ')
        blank2.grid(row=6, column=0)

        # ///////////// Begin Generator Point /////////////
        self.g_point = tk.Label(self.frame, text="Step 2: choose generator point to be used by both Bob and Alice", state='disabled')
        self.g_point.grid(row=7, column=0)

        self.g_frame = tk.Frame(self.frame)

        g_x_label = tk.Label(self.g_frame, text="x =")
        g_x_label.pack(side=tk.LEFT)
        self.g_x = tk.Entry(self.g_frame, width=5, state='disabled')
        self.g_x.pack(side=tk.LEFT)

        g_y_label = tk.Label(self.g_frame, text="y =")
        g_y_label.pack(side=tk.LEFT)
        self.g_y = tk.Entry(self.g_frame, width=5, state='disabled')
        self.g_y.pack(side=tk.LEFT)

        self.g_frame.grid(row=8, column=0)
        self.g_button = tk.Button(self.frame, text="Done", state='disabled', command=lambda: self.g_ready())
        self.g_button.grid(row=9, column=0)

        self.g_text = tk.StringVar()
        self.g_label = tk.Label(self.frame, textvariable=self.g_text)
        self.g_label.grid(row=9, column=1)

        # ///////////// End Generator Point /////////////

        blank3 = tk.Label(self.frame, text='       ')
        blank3.grid(row=11, column=0)

        # ///////////// Begin Bob /////////////
        self.bob = ec.User()

        self.step3_label = tk.Label(self.frame, text="Step 3: generate private and public keys for Bob and Alice",
                             state='disabled')
        self.step3_label.grid(row=12, column=0)

        self.bob_title = tk.Label(self.frame, text="Bob:", state='disabled')
        self.bob_title.grid(row=13, column=0)

        self.bob_label_priv = tk.Label(self.frame, text="Private Key:", state='disabled')
        self.bob_label_priv.grid(row=14, column=0)

        self.bob_entry_priv = tk.Entry(self.frame, state='disabled')
        self.bob_entry_priv.grid(row=14, column=1)

        self.bob_label_pub = tk.Label(self.frame, text="Public Key:", state='disabled')
        self.bob_label_pub.grid(row=15, column=0)

        self.bob_pub_text = tk.StringVar()
        self.bob_label = tk.Label(self.frame, textvariable=self.bob_pub_text, state='disabled')
        self.bob_label.grid(row=15, column=1)

        # ///////////// End Bob /////////////

        blank4 = tk.Label(self.frame, text='       ')
        blank4.grid(row=16, column=0)

        # ///////////// Begin Alice /////////////
        self.alice = ec.User()

        self.alice_title = tk.Label(self.frame, text="Alice:", state='disabled')
        self.alice_title.grid(row=17, column=0)

        self.alice_label_priv = tk.Label(self.frame, text="Private Key:", state='disabled')
        self.alice_label_priv.grid(row=18, column=0)

        self.alice_entry_priv = tk.Entry(self.frame, state='disabled')
        self.alice_entry_priv.grid(row=18, column=1)

        self.alice_label_pub = tk.Label(self.frame, text="Public Key:", state='disabled')
        self.alice_label_pub.grid(row=19, column=0)

        self.alice_pub_text = tk.StringVar()
        self.alice_pub_label = tk.Label(self.frame, textvariable=self.alice_pub_text, state='disabled')
        self.alice_pub_label.grid(row=19, column=1)

        self.bob_alice_button = tk.Button(self.frame, text="Done", command=lambda: self.bob_alice_ready(), state='disabled')
        self.bob_alice_button.grid(row=20, column=0)

        self.bob_alice_text = tk.StringVar()
        self.bob_alice_label = tk.Label(self.frame, textvariable=self.bob_alice_text, state='disabled')
        self.bob_alice_label.grid(row=20, column=3)

        # ///////////// End Alice /////////////

        blank5 = tk.Label(self.frame, text='       ')
        blank5.grid(row=21, column=0)

        # ///////////// Begin Shared Calculations /////////////
        self.step4_label = tk.Label(self.frame, text="Step 4: generate same shared key by Bob and Alice separately",
                                    state='disabled')
        self.step4_label.grid(row=22, column=0)

        self.shared_bob = tk.Label(self.frame, text="Shared key calculated by Bob: ", state='disabled')
        self.shared_bob.grid(row=23, column=0)
        self.shared_bob_text = tk.StringVar()
        self.shared_label_bob = tk.Label(self.frame, textvariable=self.shared_bob_text)
        self.shared_label_bob.grid(row=23, column=1)

        self.shared_alice = tk.Label(self.frame, text="Shared key calculated by Alice: ", state='disabled')
        self.shared_alice.grid(row=24, column=0)
        self.shared_alice_text = tk.StringVar()
        self.shared_label_alice = tk.Label(self.frame, textvariable=self.shared_alice_text, state='disabled')
        self.shared_label_alice.grid(row=24, column=1)


        # ///////////// End Shared Calculations /////////////

    def ec_ready(self):
        try:
            a_str = self.ec_a.get()
            b_str = self.ec_b.get()

            if a_str == '' or b_str == '':
                text = "a or b are empty"
                self.ec_eq_text.set(text)
                raise ValueError("Empty input")

            if not a_str.lstrip('-').isnumeric() or not b_str.lstrip('-').isnumeric():
                text = "a and b must be numbers"
                self.ec_eq_text.set(text)
                raise ValueError("Input must be numeric")

            a = int(a_str)
            b = int(b_str)
            self.elliptic_curve = ec.EllipticCurve(a, b)
            if not self.elliptic_curve.isNonSingular():
                text = "elliptic-curve is singular"
                self.ec_eq_text.set(text)
                raise ValueError("elliptic-curve is singular")

        except TypeError:
            text = "Invalid input"
            self.ec_eq_text.set(text)
            raise ValueError("invalid input")

        self.ec_eq_text.set(self.elliptic_curve.print())
        self.g_point.config(state='normal')
        self.g_x.config(state='normal')
        self.g_y.config(state='normal')
        self.g_button.config(state='normal')
        self.button_edit_1.grid(row=5, column=2)

    def ec_edit(self):
        self.elliptic_curve = None
        self.ec_eq_text.set("")
        self.g_point.config(state='disabled')
        self.g_x.config(state='disabled')
        self.g_y.config(state='disabled')
        self.g_button.config(state='disabled')
        self.button_edit_1.grid_forget()
        self.button_ready_1.grid(row=5, column=0)

    def g_ready(self):
        x_str = self.g_x.get()
        y_str = self.g_y.get()
        try:

            if x_str == '' or y_str == '':
                text = "x or y are empty"
                self.g_text.set(text)
                raise ValueError("Empty input")

            if not x_str.lstrip('-').isnumeric() or not y_str.lstrip('-').isnumeric():
                text = "x and b must be numbers"
                self.g_text.set(text)
                raise ValueError("Input must be numeric")

            self.g.set_x(int(x_str))
            self.g.set_y(int(y_str))
            if not self.elliptic_curve.belongsToCurve(self.g):
                text = "Point does not belong to curve"
                self.g_text.set(text)
                raise ValueError("Point does not belong to curve")

        except TypeError:
            text = "Invalid input"
            self.g_text.set(text)
            raise ValueError("invalid input")

        text = "G = "+self.g.print()
        self.g_text.set(text)

        self.step3_label.config(state="normal")
        self.bob_title.config(state="normal")
        self.bob_label_priv.config(state="normal")
        self.bob_entry_priv.config(state="normal")
        self.bob_label_pub.config(state="normal")
        self.bob_label.config(state="normal")

        self.alice_title.config(state="normal")
        self.alice_label_priv.config(state="normal")
        self.alice_entry_priv.config(state="normal")
        self.alice_label_priv.config(state="normal")
        self.alice_pub_label.config(state="normal")
        self.alice_label_pub.config(state="normal")

        self.bob_alice_button.config(state="normal")

    def bob_alice_ready(self):
        bob_priv_str = self.bob_entry_priv.get()
        bob_priv = int(bob_priv_str)
        alice_priv_str = self.alice_entry_priv.get()
        alice_priv = int(alice_priv_str)

        self.bob.setPrivKey(bob_priv)
        self.bob.setPubKey(self.elliptic_curve.point_mult(self.g, self.bob.getPrivKey()))
        self.bob_pub_text.set(self.bob.getPubKey().print())

        self.alice.setPrivKey(alice_priv)
        self.alice.setPubKey(self.elliptic_curve.point_mult(self.g, self.alice.getPrivKey()))
        self.alice_pub_text.set(self.alice.getPubKey().print())

        self.shared_bob_text.set(self.elliptic_curve.point_mult(self.alice.getPubKey(), self.bob.getPrivKey()).print())
        self.shared_alice_text.set(self.elliptic_curve.point_mult(self.bob.getPubKey(), self.alice.getPrivKey()).print())

        self.step4_label.config(state="normal")
        self.shared_label_alice.config(state="normal")
        self.shared_alice.config(state="normal")
        self.shared_label_bob.config(state="normal")
        self.shared_bob.config(state="normal")


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
