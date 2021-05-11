import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

class Application(tk.Frame):
    def __init__(self, config, master=None):
        super().__init__(master)
        self.master = master

        # Window Size Options
        self.master.geometry("250x150")
        self.master.maxsize(250,150)
        self.master.minsize(250,150)

        # Force on top
        self.master.attributes('-topmost', True)

        # Creating Layout
        self.pack()
        self.create_widgets()

        # Additional Vars
        self.totalCount = config.config['VARIABLES']['Count']


    def create_widgets(self):
        # ---------- Title Bar ----------
        self.master.title("Title Bar")

        # ------------ Row 1 ------------
        row = 1
        self.header = ttk.Label(self, text="Title", font=("Arial", 20))
        self.header.grid(row=row, column=1, columnspan=4, pady=(10,3))

        # ------------ Row 2 ------------
        row+=1
        self.totalLabel = ttk.Label(self, text="Total: ")
        self.totalLabel.grid(row=row, column=1)

        self.totalCount = ttk.Label(self, text="0")
        self.totalCount.grid(row=row, column=2, sticky=W)

        self.sessionLabel = ttk.Label(self, text="Session: ")
        self.sessionLabel.grid(row=row, column=3)

        self.sessionCount = ttk.Label(self, text="0")
        self.sessionCount.grid(row=row, column=4, sticky=W)

        # ------------ Row 3 ------------
        row+=1
        pady=(15,0)
        self.startButton = ttk.Button(self, text="Start", width=15)
        self.startButton.grid(row=row, column=1, columnspan=2, sticky=NSEW, pady=pady)

        self.stopButton = ttk.Button(self, text="Stop", width=15)
        self.stopButton.grid(row=row, column=3, columnspan=2, sticky=NSEW, pady=pady)
        self.stopButton["state"] = DISABLED

        # ------------ Row 4 ------------
        row+=1
        self.progressBar = ttk.Progressbar(self, orient=HORIZONTAL, mode="indeterminate")
        self.progressBar.grid(row=row,column=1, columnspan=4, sticky=NSEW)

        # ------------ Row 5 ------------
        row+=1
        self.statusLabel = ttk.Label(self, text="Status: Not Running")
        self.statusLabel.grid(row = row, column=1, columnspan=4)

    '''
    --Example of running the same thing over and over without freezing the GUI--

    def check_status(self):
        self.count['text'] = f"Counting: {str(int(self.count['text'].split(': ')[1]) + 1)}"
        self.checking = self.after(1000, self.check_status)
    '''
