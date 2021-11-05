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

        title = tk.Label(self.frame, text='Elliptic Curve:').grid(row=0, column=0, sticky="W")

        blank = tk.Label(self.frame, text='       ')
        blank.grid(row=1, column=0)

        shared_label = tk.Label(self.frame, text='Shared data:')
        shared_label.grid(row=2, column=0, sticky="W")

        ec_label_1 = tk.Label(self.frame, text="A =").grid(row=3, column=0)
        self.ec_a = tk.Entry(self.frame, width=5)
        self.ec_a.grid(row=3, column=1)

        ec_label_2 = tk.Label(self.frame, text="B =").grid(row=4, column=0)
        self.ec_b = tk.Entry(self.frame, width=5)
        self.ec_b.grid(row=4, column=1)

        button = tk.Button(self.frame, text="Listo", command=lambda: self.ec_ready())
        button.grid(row=5, column=0)

        self.ec_eq_text = tk.StringVar()
        self.ec_eq = tk.Label(self.frame, textvariable=self.ec_eq_text)
        self.ec_eq.grid(row=5, column=3)

        # ///////////// End Elliptic Curve /////////////

        blank2 = tk.Label(self.frame, text='       ')
        blank2.grid(row=6, column=0)

        # ///////////// Begin Generator Point /////////////
        g_point = tk.Label(self.frame, text="Generator Point:")
        g_point.grid(row=7, column=0)

        g_x_label = tk.Label(self.frame, text="X =")
        g_x_label.grid(row=8, column=0)
        self.g_x = tk.Entry(self.frame, width=5)
        self.g_x.grid(row=8, column=1)

        g_y_label = tk.Label(self.frame, text="Y =")
        g_y_label.grid(row=9, column=0)
        self.g_y = tk.Entry(self.frame, width=5)
        self.g_y.grid(row=9, column=1)

        g_button = tk.Button(self.frame, text="Listo", command=lambda: self.g_ready())
        g_button.grid(row=10, column=0)

        self.g_text = tk.StringVar()
        self.g_label = tk.Label(self.frame, textvariable=self.g_text)
        self.g_label.grid(row=10, column=3)

        # ///////////// End Generator Point /////////////

        '''
        bob_label = tk.Label(self.frame, text='Bob').grid(row=2, column=0)
        bob_label_priv = tk.Label(self.frame, text="Private Key:").grid(row=3, column=0)
        bob_priv = tk.Entry(self.frame).grid(row=3, column=1)
        bob_label_pub = tk.Label(self.frame, text="Public Key:").grid(row=4, column=0)
        bob_pub = tk.Entry(self.frame).grid(row=4, column=1)

        alice_label = tk.Label(self.frame, text='Alice').grid(row=2, column=4)
        alice_label_priv = tk.Label(self.frame, text="Private Key:").grid(row=3, column=4)
        alice_priv = tk.Entry(self.frame).grid(row=3, column=5)
        alice_label_pub = tk.Label(self.frame, text="Public Key:").grid(row=4, column=4)
        alice_pub = tk.Entry(self.frame).grid(row=4, column=5)
        '''

    def ec_ready(self):
        a_str = self.ec_a.get()
        a = int(a_str)
        b_str = self.ec_b.get()
        b = int(b_str)

        self.elliptic_curve = ec.EllipticCurve(a, b)

        text = ("y\u00B2 = x\u00B3 + "+a_str) if a > 0 else ("y\u00B2 = x\u00B3 "+a_str)
        text += (("x + " + b_str) if b > 0 else ("x "+b_str))

        self.ec_eq_text.set(text)

    def g_ready(self):
        x_str = self.g_x.get()
        x = int(x_str)
        y_str = self.g_y.get()
        y = int(y_str)

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
