import tkinter as tk
import constants as cons
import ecmath as ec
import random as rand
from PIL import Image, ImageTk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)


class PointAddition:
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master)

        self.title = tk.Label(self.frame, text='Suma de Puntos', font='Helvetica 16 bold')
        self.title.pack(fill="x")

        # button that displays the plot
        plot_button = tk.Button(master=self.frame,
                                command=self.plot,
                                height=2,
                                width=10,
                                text="Plot")

        # place the button
        # in main window
        plot_button.pack()

    # plot function is created for
    # plotting the graph in
    # tkinter window
    def plot(self):
        # the figure that will contain the plot
        fig = Figure(figsize=(5, 5),
                     dpi=100)

        # list of squares
        y = [i ** 2 for i in range(101)]

        # adding the subplot
        plot1 = fig.add_subplot(111)

        # plotting the graph
        plot1.plot(y)

        # creating the Tkinter canvas
        # containing the Matplotlib figure
        canvas = FigureCanvasTkAgg(fig,
                                   master=self.frame)
        canvas.draw()

        # placing the canvas on the Tkinter window
        canvas.get_tk_widget().pack()

        # creating the Matplotlib toolbar
        toolbar = NavigationToolbar2Tk(canvas,
                                       self.frame)
        toolbar.update()

        # placing the toolbar on the Tkinter window
        canvas.get_tk_widget().pack()

    def start_page(self):
        self.frame.grid(column=0, row=0, sticky="NWES")

    def go_back(self):
        self.frame.pack_forget()
        self.app.main_page()

    def get_frame(self):
        return self.frame
