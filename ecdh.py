import tkinter as tk
import constants as cons
import ecmath as ec

class Ecdh:
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master)

        # ///////////// Begin Elliptic Curve /////////////

        self.elliptic_curve = None

        title = tk.Label(self.frame, text='Elliptic-curve Diffie-Hellman')
        title.grid(row=0, column=0, sticky="W")

        blank = tk.Label(self.frame, text='       ')
        blank.grid(row=1, column=0)

        shared_label = tk.Label(self.frame, text='Step 1: choose the elliptic curve to be used by both Bob and Alice')
        shared_label.grid(row=2, column=0, sticky="W")

        self.ec_frame = tk.Frame(self.frame)
        ec_label_1 = tk.Label(self.ec_frame, text="a =")
        ec_label_1.pack(side=tk.LEFT)
        self.ec_a = tk.Entry(self.ec_frame, width=5)
        self.ec_a.pack(side=tk.LEFT)
        ec_label_2 = tk.Label(self.ec_frame, text="b =")
        ec_label_2.pack(side=tk.LEFT)
        self.ec_b = tk.Entry(self.ec_frame, width=5)
        self.ec_b.pack(side=tk.LEFT)
        self.ec_frame.grid(row=3, column=0)

        button = tk.Button(self.frame, text="Listo", command=lambda: self.ec_ready())
        button.grid(row=5, column=0)

        self.ec_eq_text = tk.StringVar()
        self.ec_eq = tk.Label(self.frame, textvariable=self.ec_eq_text)
        self.ec_eq.grid(row=5, column=1)

        # ///////////// End Elliptic Curve /////////////

        blank2 = tk.Label(self.frame, text='       ')
        blank2.grid(row=6, column=0)

        # ///////////// Begin Generator Point /////////////
        self.g = None

        g_point = tk.Label(self.frame, text="Step 2: choose generator point to be used by both Bob and Alice")
        g_point.grid(row=7, column=0)

        g_x_label = tk.Label(self.frame, text="X =")
        g_x_label.grid(row=8, column=0)
        self.g_x = tk.Entry(self.frame, width=5, state='disabled')
        self.g_x.grid(row=8, column=1)

        g_y_label = tk.Label(self.frame, text="Y =")
        g_y_label.grid(row=9, column=0)
        self.g_y = tk.Entry(self.frame, width=5, state='disabled')
        self.g_y.grid(row=9, column=1)

        g_button = tk.Button(self.frame, text="Listo", state='disabled', command=lambda: self.g_ready())
        g_button.grid(row=10, column=0)

        self.g_text = tk.StringVar()
        self.g_label = tk.Label(self.frame, textvariable=self.g_text)
        self.g_label.grid(row=10, column=3)

        # ///////////// End Generator Point /////////////

        blank3 = tk.Label(self.frame, text='       ')
        blank3.grid(row=11, column=0)

        # ///////////// Begin Bob /////////////
        self.bob = ec.User()

        bob_label = tk.Label(self.frame, text="Bob:")
        bob_label.grid(row=12, column=0)

        bob_label_priv = tk.Label(self.frame, text="Private Key:")
        bob_label_priv.grid(row=13, column=0)

        self.bob_entry_priv = tk.Entry(self.frame)
        self.bob_entry_priv.grid(row=13, column=1)

        bob_label_pub = tk.Label(self.frame, text="Public Key:")
        bob_label_pub.grid(row=14, column=0)

        self.bob_pub_text = tk.StringVar()
        self.bob_label = tk.Label(self.frame, textvariable=self.bob_pub_text)
        self.bob_label.grid(row=14, column=1)

        # ///////////// End Bob /////////////

        blank4 = tk.Label(self.frame, text='       ')
        blank4.grid(row=15, column=0)

        # ///////////// Begin Alice /////////////
        self.alice = ec.User()

        alice_label = tk.Label(self.frame, text="Alice:")
        alice_label.grid(row=16, column=0)

        alice_label_priv = tk.Label(self.frame, text="Private Key:")
        alice_label_priv.grid(row=17, column=0)

        self.alice_entry_priv = tk.Entry(self.frame)
        self.alice_entry_priv.grid(row=17, column=1)

        alice_label_pub = tk.Label(self.frame, text="Public Key:")
        alice_label_pub.grid(row=18, column=0)

        self.alice_pub_text = tk.StringVar()
        self.alice_pub_label = tk.Label(self.frame, textvariable=self.alice_pub_text)
        self.alice_pub_label.grid(row=18, column=1)

        bob_alice_button = tk.Button(self.frame, text="Listo", command=lambda: self.bob_alice_ready())
        bob_alice_button.grid(row=19, column=0)

        self.bob_alice_text = tk.StringVar()
        self.bob_alice_label = tk.Label(self.frame, textvariable=self.bob_alice_text)
        self.bob_alice_label.grid(row=19, column=3)

        # ///////////// End Alice /////////////

        # ///////////// Begin Shared Calculations /////////////
        shared_bob = tk.Label(self.frame, text="Shared key calculated by Bob: ")
        shared_bob.grid(row=20, column=0)
        self.shared_bob_text = tk.StringVar()
        shared_label_bob = tk.Label(self.frame, textvariable=self.shared_bob_text)
        shared_label_bob.grid(row=20, column=1)

        shared_alice = tk.Label(self.frame, text="Shared key calculated by Alice: ")
        shared_alice.grid(row=21, column=0)
        self.shared_alice_text = tk.StringVar()
        shared_label_alice = tk.Label(self.frame, textvariable=self.shared_alice_text)
        shared_label_alice.grid(row=21, column=1)


        # ///////////// End Shared Calculations /////////////

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


        '''
        print("Clave COMPARTIDA calculada por ALICE:")
        print(curve.point_mult(bob.getPubKey(), alice.getPrivKey()).print())
        print("-------")

        print("Clave COMPARTIDA calculada por BOB:")
        print(curve.point_mult(alice.getPubKey(), bob.getPrivKey()).print())
        print("-------")
        '''



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
            a_str = str(a)
            b = int(b_str)
            b_str = str(b)
        except TypeError:
            text = "Invalid input"
            self.ec_eq_text.set(text)
            raise ValueError("invalid input")

        self.elliptic_curve = ec.EllipticCurve(a, b)

        if not self.elliptic_curve.isNonSingular():
            text = "elliptic-curve is singular"
            self.ec_eq_text.set(text)
            raise ValueError("elliptic-curve is singular")

        text = ("y\u00B2 = x\u00B3 + "+a_str) if a > 0 else ("y\u00B2 = x\u00B3 "+a_str)
        text += (("x + " + b_str) if b > 0 else ("x "+b_str))

        self.ec_eq_text.set(text)
        self.g_x.config(state='normal')
        self.g_y.config(state='normal')

    def g_ready(self):
        x_str = self.g_x.get()
        x = int(x_str)
        y_str = self.g_y.get()
        y = int(y_str)

        self.g = ec.Point(x, y)

        text = "G("+x_str+", "+y_str+")"

        self.g_text.set(text)

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
