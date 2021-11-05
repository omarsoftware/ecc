import tkinter as tk
import constants as cons

class Ecdh:
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master)

        title = tk.Label(self.frame, text='ECDH Page!!!').grid(row=0, column=3)

        blank = tk.Label(self.frame, text='       ')
        blank.grid(row=1, column=0)

        shared_label = tk.Label(self.frame, text='Shared data:').grid(row=2, column=0)

        ec_label_1 = tk.Label(self.frame, text="A = ").grid(row=3, column=0)
        self.ec_a = tk.Entry(self.frame, width=5)
        self.ec_a.grid(row=3, column=1)

        ec_label_2 = tk.Label(self.frame, text="B = ").grid(row=4, column=0)
        self.ec_b = tk.Entry(self.frame, width=5)
        self.ec_b.grid(row=4, column=1)

        button = tk.Button(self.frame, text="Listo", command=lambda: self.listo())
        button.grid(row=5, column=0)

        self.ec_eq_text = tk.StringVar()
        self.ec_eq = tk.Label(self.frame, textvariable=self.ec_eq_text)
        self.ec_eq.grid(row=6, column=0)


        '''
        ec_label_1 = tk.Label(self.frame, text="y\u00B2 = x\u00B3 +").grid(row=3, column=1)
        ec_a = tk.Entry(self.frame, width=3).grid(row=3, column=2, padx=3)
        
        shared_ec = tk.Label(self.frame, text="Chosen Elliptic Curve:").grid(row=3, column=0)
        
        ec_label_2 = tk.Label(self.frame, text="x +").grid(row=3, column=3, padx=3)
        ec_b = tk.Entry(self.frame, width=3).grid(row=3, column=4)
        
        
        blank = tk.Label(self.frame, text='       ')
        blank.grid(row=4, column=0)
        '''
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

    def listo(self):
        a_str = self.ec_a.get()
        a = int(self.ec_a.get())
        b_str = self.ec_b.get()
        b = int(self.ec_b.get())
        text = ""
        if a > 0:
            text = ("y\u00B2 = x\u00B3 + "+a_str)
        else:
            text = ("y\u00B2 = x\u00B3 "+a_str)
        if b > 0:
            text = (text + "x + " + b_str)
        else:
            text = (text+"x "+b_str)

        self.ec_eq_text.set(text)

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
