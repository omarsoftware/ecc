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

        title = tk.Label(self.frame, text='Elliptic-curve Diffie-Hellman')
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
        self.ec_ready_button = tk.Button(self.frame)
        self.ec_eq_text = tk.StringVar()
        self.ec_eq = tk.Label(self.frame)
        self.ec_button_edit = tk.Button(self.frame)

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

        self.g_set()

        # ///////////// End Generator Point /////////////

        blank3 = tk.Label(self.frame, text='       ')
        blank3.grid(row=11, column=0)

        # ///////////// Begin Bob /////////////
        self.bob = ec.User()

        self.step3_label = tk.Label(self.frame, text="Step 3: generate private and public keys for Bob and Alice",
                             state='disabled')
        self.step3_label.grid(row=12, column=0)

        self.bob_title = tk.Label(self.frame, text="Bob:", state="disabled")
        self.bob_title.grid(row=13, column=0)

        self.bob_label_priv = tk.Label(self.frame, text="Private Key:", state="disabled")
        self.bob_label_priv.grid(row=14, column=0)

        self.bob_entry_priv = tk.Entry(self.frame, state="disabled")
        self.bob_entry_priv.grid(row=14, column=1)

        self.bob_label_pub = tk.Label(self.frame, text="Public Key:", state="disabled")
        self.bob_label_pub.grid(row=15, column=0)

        self.bob_pub_text = tk.StringVar()
        self.bob_label = tk.Label(self.frame, textvariable=self.bob_pub_text, state="disabled")
        self.bob_label.grid(row=15, column=1)

        # ///////////// End Bob /////////////

        blank4 = tk.Label(self.frame, text='       ')
        blank4.grid(row=16, column=0)

        # ///////////// Begin Alice /////////////
        self.alice = ec.User()

        self.alice_title = tk.Label(self.frame, text="Alice:", state="disabled")
        self.alice_title.grid(row=17, column=0)

        self.alice_label_priv = tk.Label(self.frame, text="Private Key:", state="disabled")
        self.alice_label_priv.grid(row=18, column=0)

        self.alice_entry_priv = tk.Entry(self.frame, state="disabled")
        self.alice_entry_priv.grid(row=18, column=1)

        self.alice_label_pub = tk.Label(self.frame, text="Public Key:", state="disabled")
        self.alice_label_pub.grid(row=19, column=0)

        self.alice_pub_text = tk.StringVar()
        self.alice_pub_label = tk.Label(self.frame, textvariable=self.alice_pub_text, state="disabled")
        self.alice_pub_label.grid(row=19, column=1)

        self.bob_alice_button = tk.Button(self.frame, text="Done", command=lambda: self.bob_alice_ready(), state="disabled")
        self.bob_alice_button.grid(row=20, column=0)

        self.bob_alice_text = tk.StringVar()
        self.bob_alice_label = tk.Label(self.frame, textvariable=self.bob_alice_text, state="disabled")
        self.bob_alice_label.grid(row=20, column=3)

        # ///////////// End Alice /////////////

        blank5 = tk.Label(self.frame, text='       ')
        blank5.grid(row=21, column=0)

        # ///////////// Begin Shared Calculations /////////////
        self.step4_label = tk.Label(self.frame, text="Step 4: generate same shared key by Bob and Alice separately",
                                    state="disabled")
        self.step4_label.grid(row=22, column=0)

        self.shared_bob = tk.Label(self.frame, text="Shared key calculated by Bob: ", state="disabled")
        self.shared_bob.grid(row=23, column=0)
        self.shared_bob_text = tk.StringVar()
        self.shared_label_bob = tk.Label(self.frame, textvariable=self.shared_bob_text)
        self.shared_label_bob.grid(row=23, column=1)

        self.shared_alice = tk.Label(self.frame, text="Shared key calculated by Alice: ", state="disabled")
        self.shared_alice.grid(row=24, column=0)
        self.shared_alice_text = tk.StringVar()
        self.shared_label_alice = tk.Label(self.frame, textvariable=self.shared_alice_text, state="disabled")
        self.shared_label_alice.grid(row=24, column=1)


        # ///////////// End Shared Calculations /////////////

    def ec_set(self):
        self.ec_title.config(text='Step 1: choose the elliptic curve to be used by both Bob and Alice')
        self.ec_title.grid(row=2, column=0, sticky="W")

        self.ec_gen_eq.set("y\u00B2 = x\u00B3 + ax + b")
        self.ec_gen_eq_label.config(textvariable=self.ec_gen_eq)
        self.ec_gen_eq_label.grid(row=3, column=0)

        self.ec_a_label.config(text="a =")
        self.ec_a_label.pack(side=tk.LEFT)
        self.ec_a_entry.config(width=5)
        self.ec_a_entry.pack(side=tk.LEFT)

        self.ec_b_label.config(text="b =")
        self.ec_b_label.pack(side=tk.LEFT)
        self.ec_b_entry.pack(side=tk.LEFT)
        self.ec_b_entry.config(width=5)

        self.ec_frame.grid(row=4, column=0)

        self.ec_ready_button.config(text="Done", command=lambda: self.ec_ready())
        self.ec_ready_button.grid(row=5, column=0)

        self.ec_eq.grid(row=5, column=1)

        self.ec_eq.config(textvariable=self.ec_eq_text)

        self.ec_button_edit.config(text="Edit", command=lambda: self.ec_clear())
        self.ec_button_edit.grid_forget()

    def ec_ready(self):
        try:
            a_str = self.ec_a_entry.get()
            b_str = self.ec_b_entry.get()

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
        self.ec_a_entry.config(state="disabled")
        self.ec_b_entry.config(state="disabled")
        self.ec_ready_button.grid_forget()
        self.ec_button_edit.grid(row=5, column=0)

        self.g_title.config(state='normal')
        self.g_x_label.config(state='normal')
        self.g_y_label.config(state='normal')
        self.g_x_entry.config(state='normal')
        self.g_y_entry.config(state='normal')
        self.g_ready_button.config(state='normal')


    def ec_clear(self):
        self.ec_a_entry.delete(0, 'end')
        self.ec_a_entry.config(state="normal")
        self.ec_b_entry.delete(0, 'end')
        self.ec_b_entry.config(state="normal")
        self.ec_title.grid(row=2, column=0, sticky="W")
        self.ec_eq_text.set("")
        self.ec_ready_button.grid(row=5, column=0)
        self.ec_eq.grid(row=5, column=1)
        self.ec_button_edit.grid_forget()

        self.g_clear()

    def g_set(self):
        self.g_title.config(text="Step 2: choose generator point to be used by both Bob and Alice", state="disabled")
        self.g_title.grid(row=7, column=0)

        self.g_x_label.config(text="x =")
        self.g_x_label.pack(side="left")
        self.g_x_entry.config(width=5, state="disabled")
        self.g_x_entry.pack(side="left")

        self.g_y_label.config(text="y =")
        self.g_y_label.pack(side="left")
        self.g_y_entry.config(width=5, state="disabled")
        self.g_y_entry.pack(side="left")

        self.g_frame.grid(row=8, column=0)

        self.g_ready_button.config(text="Done", state="disabled", command=lambda: self.g_ready())
        self.g_ready_button.grid(row=9, column=0)

        self.g_label.config(textvariable=self.g_text)
        self.g_label.grid(row=9, column=1)

    def g_ready(self):
        x_str = self.g_x_entry.get()
        y_str = self.g_y_entry.get()
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

    def g_clear(self):
        self.g_title.config(state="disabled")
        self.g_x_label.config(state="disabled")
        self.g_x_entry.delete(0, "end")
        self.g_x_entry.config(state="disabled")
        self.g_y_label.config(state="disabled")
        self.g_y_entry.delete(0, "end")
        self.g_y_entry.config(state="disabled")
        self.g_ready_button.config(state="disabled")
        self.g_text.set("")
        self.g_label.grid_forget()


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
