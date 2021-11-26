import tkinter as tk
import constants as cons
import ecmath as ec
from ecdh import Ecdh
from ecdsa import Ecdsa
from pointops import PointOperations


class App:
    def __init__(self, root=None):
        self.root = root
        self.root.geometry(cons.screen_size)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.frame = tk.Frame(self.root)

        self.main_menu = tk.Menu(self.root)
        self.root.config(menu=self.main_menu)

        # Creating exit
        file_menu = tk.Menu(self.main_menu)
        self.main_menu.add_cascade(label="Archivo", menu=file_menu)
        file_menu.add_command(label="Salir", command=self.root.quit)

        # Creating Analysis menu
        analysis_menu = tk.Menu(self.main_menu)
        self.main_menu.add_cascade(label="Análisis", menu=analysis_menu)
        analysis_menu.add_command(label="Operaciones de Puntos", command=self.make_point_operations)

        # Creating Encrypt menu
        encrypt_menu = tk.Menu(self.main_menu)
        self.main_menu.add_cascade(label="Cifrado", menu=encrypt_menu)
        encrypt_menu.add_command(label="Diffie-Hellman con curva elíptica (ECDH)",
                                 command=self.make_ecdh)
        encrypt_menu.add_command(label="Firma Digital con curva elíptica (ECDSA)",
                                 command=self.make_ecdsa)

        self.frame.grid()

        tk.Label(self.frame, text='Página Principal').grid()

        self.point_operations = PointOperations(master=self.root, app=self)
        self.ecdh = Ecdh(master=self.root, app=self)
        self.ecdsa = Ecdsa(master=self.root, app=self)

        self.pages = [self.point_operations, self.ecdh, self.ecdsa]

        # /////////////

        curve = ec.EllipticCurve(10, 15, 23)
        point_p = ec.Point(3, 7)
        # point_q = ec.Point(3, 7)
        point_r = curve.point_mult(point_p, 19)
        print(point_r.print())

        # da (22, 2)
        # ////////////


    def main_page(self):
        self.frame.grid()

    def make_ecdh(self):
        self.frame.grid_forget()
        self.hide_all_frames()
        self.ecdh.start_page()

    def make_ecdsa(self):
        self.frame.grid_forget()
        self.hide_all_frames()
        self.ecdsa.start_page()

    def make_point_operations(self):
        self.frame.grid_forget()
        self.hide_all_frames()
        self.point_operations.start_page()

    def hide_all_frames(self):
        for page in self.pages:
            page.get_frame().grid_forget()


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
