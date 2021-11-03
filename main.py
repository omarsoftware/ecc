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

        self.frame.pack()
        tk.Label(self.frame, text='Main page').pack()
        tk.Button(self.frame, text='Go to Page 1',
                  command=self.make_page_1).pack()
        self.page_1 = Page_1(master=self.root, app=self)

    def main_page(self):
        self.frame.pack()

    def make_page_1(self):
        self.frame.pack_forget()
        self.page_1.start_page()


class Page_1:
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master)
        tk.Label(self.frame, text='Page 1').pack()
        tk.Button(self.frame, text='Go back', command=self.go_back).pack()

    def start_page(self):
        self.frame.pack()

    def go_back(self):
        self.frame.pack_forget()
        self.app.main_page()


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
