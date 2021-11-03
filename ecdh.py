import tkinter as tk
import constants as cons

class Ecdh:
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master)

        title = tk.Label(self.frame, text='ECDH Page!!!').grid(row=0, column=0)

        blank = tk.Label(self.frame, text='       ')
        blank.grid(row=1, column=0)

        bob_label = tk.Label(self.frame, text='Bob:').grid(row=2, column=0)
        bob_priv = tk.Entry(self.frame).grid(row=3, column=0)
        bob_pub = tk.Entry(self.frame).grid(row=4, column=0)

        alice_label = tk.Label(self.frame, text='Alice:').grid(row=5, column=0)
        alice_priv = tk.Entry(self.frame).grid(row=6, column=0)
        alice_pub = tk.Entry(self.frame).grid(row=7, column=0)

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
