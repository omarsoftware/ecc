import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from tkinter import *
from ecmath import *
from start import *

root = Tk()
app = Start(root)
app.start()

'''
#Hide all frames
def hide_all_frames():
    point_operations_frame.pack_forget()
    ecdh_frame.pack_forget()
    ecdsa_frame.pack_forget()
'''
root.mainloop()