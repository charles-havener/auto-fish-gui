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

        # Vars from config
        self.configCount = int(config.config['VARIABLES']['Count'])


        # Creating Layout
        self.pack()
        self.create_widgets()


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

        self.totalCount = ttk.Label(self, text=f"{self.configCount}")
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
        self.startButton['command'] = lambda: self.change_run_state(True)

        self.stopButton = ttk.Button(self, text="Stop", width=15)
        self.stopButton.grid(row=row, column=3, columnspan=2, sticky=NSEW, pady=pady)
        self.stopButton["state"] = DISABLED
        self.stopButton['command'] = lambda: self.change_run_state(False)

        # ------------ Row 4 ------------
        row+=1
        self.progressBar = ttk.Progressbar(self, orient=HORIZONTAL, mode="indeterminate")
        self.progressBar.grid(row=row,column=1, columnspan=4, sticky=NSEW)

        # ------------ Row 5 ------------
        row+=1
        self.statusLabel = ttk.Label(self, text="Status: Not Running")
        self.statusLabel.grid(row = row, column=1, columnspan=4)


    def change_run_state(self, run):
        if not run:
            self.progressBar.stop()
            self.statusLabel['text'] = "Status: Stopped"
            self.after_cancel(self.checking)
            self.checking = None
            self.startButton['state'] = 'enabled'
            self.stopButton['state'] = 'disabled'
            return
        
        self.startButton['state'] = 'disabled'
        self.stopButton['state'] = 'enabled'
        self.progressBar.start()
        self.statusLabel['text'] = "Status: Running"

        self.checking = self.after(1000, self.check_status)

    
    def check_status(self):
        self.configCount += 1
        self.totalCount['text'] = str(int(self.totalCount['text']) + 1)
        self.sessionCount['text'] = str(int(self.sessionCount['text'])+1)
        self.checking = self.after(1000, self.check_status)
