import tkinter as tk
import constants as cons


class App:
    def __init__(self, root=None):
        self.root = root
        self.root.geometry(cons.screen_size)
        self.frame = tk.Frame(self.root)

        self.main_menu = tk.Menu(self.root)
        self.root.config(menu=self.main_menu)

        # Creating exit
        file_menu = tk.Menu(self.main_menu)
        self.main_menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Exit", command=self.root.quit)

        # Creating Analysis menu
        analysis_menu = tk.Menu(self.main_menu)
        self.main_menu.add_cascade(label="Analysis", menu=analysis_menu)
        analysis_menu.add_command(label="Point Operations", command=self.make_point_operations)

        # Creating Encrypt menu
        encrypt_menu = tk.Menu(self.main_menu)
        self.main_menu.add_cascade(label="Encrypt", menu=encrypt_menu)
        encrypt_menu.add_command(label="Elliptic-Curve Diffie-Hellman (ECDH)",
                                 command=self.make_ecdh)
        encrypt_menu.add_command(label="Elliptic-Curve Digital Signature Algorithm (ECDSA)",
                                 command=self.make_ecdsa)


        self.frame.pack()

        tk.Label(self.frame, text='Main page').pack()

        self.point_operations = PointOperations(master=self.root, app=self)
        self.ecdh = Ecdh(master=self.root, app=self)
        self.ecdsa = Ecdsa(master=self.root, app=self)

        self.classes = [self.point_operations, self.ecdh, self.ecdsa]

    def main_page(self):
        self.frame.pack()

    def make_ecdh(self):
        self.frame.pack_forget()
        self.hide_all_frames()
        self.ecdh.start_page()

    def make_ecdsa(self):
        self.frame.pack_forget()
        self.hide_all_frames()
        self.ecdsa.start_page()

    def make_point_operations(self):
        self.frame.pack_forget()
        self.hide_all_frames()
        self.point_operations.start_page()

    def hide_all_frames(self):
        for i in self.classes:
            i.get_frame().pack_forget()


class Ecdh:
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master)
        tk.Label(self.frame, text='ECDH Page!!!').pack()
        tk.Entry(self.frame).pack()
        # tk.Button(self.frame, text='Go back', command=self.go_back).pack()

    def start_page(self):
        self.frame.pack()

    def go_back(self):
        self.frame.pack_forget()
        self.app.main_page()

    def get_frame(self):
        return self.frame


class Ecdsa:
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master)
        tk.Label(self.frame, text='ECDSA Page!!!').pack()
        # tk.Button(self.frame, text='Go back', command=self.go_back).pack()

    def start_page(self):
        self.frame.pack()

    def go_back(self):
        self.frame.pack_forget()
        self.app.main_page()

    def get_frame(self):
        return self.frame


class PointOperations:
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master)
        tk.Label(self.frame, text='Point Operations Page!!!').pack()
        # tk.Button(self.frame, text='Go back', command=self.go_back).pack()

    def start_page(self):
        self.frame.pack()

    def go_back(self):
        self.frame.pack_forget()
        self.app.main_page()

    def get_frame(self):
        return self.frame


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
