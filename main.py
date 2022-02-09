import tkinter as tk
import constants as cons
from interfaces.ecdh import Ecdh
from interfaces.commutativity import Commutativity
from interfaces.point_addition import PointAddition
from interfaces.point_multiplication import PointMultiplication


class App:
    def __init__(self, root=None):
        self.root = root
        self.root.title(cons.title)
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

        # Creating Operations menu
        analysis_menu = tk.Menu(self.main_menu)
        self.main_menu.add_cascade(label="Operaciones", menu=analysis_menu)
        analysis_menu.add_command(label="Suma", command=self.make_point_addition)
        analysis_menu.add_command(label="Multiplicación", command=self.make_double_and_addiplication)

        # Creating Properties menu
        properties_menu = tk.Menu(self.main_menu)
        self.main_menu.add_cascade(label="Propiedades", menu=properties_menu)
        properties_menu.add_command(label="Conmutatividad", command=self.make_commutativity)

        # Creating Algorithms menu
        encrypt_menu = tk.Menu(self.main_menu)
        self.main_menu.add_cascade(label="Algoritmos", menu=encrypt_menu)
        encrypt_menu.add_command(label="Diffie-Hellman con curva elíptica (ECDH)",
                                 command=self.make_ecdh)

        self.frame.grid()

        tk.Label(self.frame, text='Página Principal').grid()

        # self.addition = Addition(master=self.root, app=self)
        # self.addition = Multiplication(master=self.root, app=self)
        self.point_addition = PointAddition(master=self.root, app=self)
        self.double_and_addiplication = PointMultiplication(master=self.root, app=self)
        self.commutativity = Commutativity(master=self.root, app=self)
        self.ecdh = Ecdh(master=self.root, app=self)

        self.pages = [self.point_addition, self.double_and_addiplication, self.commutativity, self.ecdh]

    def main_page(self):
        self.frame.grid()

    def make_ecdh(self):
        self.frame.grid_forget()
        self.hide_all_frames()
        self.ecdh.start_page()

    def make_point_addition(self):
        self.frame.grid_forget()
        self.hide_all_frames()
        self.point_addition.start_page()

    def make_double_and_addiplication(self):
        self.frame.grid_forget()
        self.hide_all_frames()
        self.double_and_addiplication.start_page()

    def make_point_operations(self):
        self.frame.grid_forget()
        self.hide_all_frames()
        self.point_operations.start_page()

    def make_commutativity(self):
        self.frame.grid_forget()
        self.hide_all_frames()
        self.commutativity.start_page()

    def hide_all_frames(self):
        for page in self.pages:
            page.get_frame().grid_forget()


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
