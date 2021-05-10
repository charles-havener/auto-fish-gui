import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

class Application(tk.Frame):
    def __init__(self, config, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.totalCount = config.config['VARIABLES']['Count']


    def create_widgets(self):
        #TODO: figure out how to place pieces at (x,y) locations with set width and height
        #TODO: rather than deal with the grid. Also set main window width/height
        self.header = ttk.Label(self, text="Ayyy")
        self.header.grid(row=1, column=1)

    '''
    --Example of running the same thing over and over without freezing the GUI--

    def check_status(self):
        self.count['text'] = f"Counting: {str(int(self.count['text'].split(': ')[1]) + 1)}"
        self.checking = self.after(1000, self.check_status)
    '''
