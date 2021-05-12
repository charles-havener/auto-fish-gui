import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import pyautogui
import numpy as np
import time

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
        self.configCount = int(config.config['VARIABLES']['count'])
        self.barLocation = eval(config.config['COORDINATES']['bar'])
        self.iconLocation = eval(config.config['COORDINATES']['icon'])
        self.brownColor = eval(config.config['COLORS']['brown_bar'])
        self.blueColor = eval(config.config['COLORS']['blue_bar'])
        self.greenColor = eval(config.config['COLORS']['green_bar'])
        self.faceColor = eval(config.config['COLORS']['face_color'])
        self.bagColor = eval(config.config['COLORS']['bag_color'])
        self.castKey = config.config['KEYBINDS']['cast_key']
        self.catchKey = config.config['KEYBINDS']['catch_key']

        # Additional vars
        self.stdWaitTime = 200

        # Creating Layout
        self.pack()
        self.create_widgets()


    def create_widgets(self):
        # ---------- Title Bar ----------
        self.master.title("auto_fish.exe")

        # ------------ Row 1 ------------
        row = 1
        self.header = ttk.Label(self, text="ESO Auto Fish", font=("Arial", 20))
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


    def waitToRun(self):
        self.checking = self.after(10, self.check_status())

    def change_run_state(self, run):
        if not run:
            self.progressBar.stop()
            self.statusLabel['text'] = "Status: Stopped"
            self.after_cancel(self.checking)
            self.after_cancel(self.pressing)
            self.checking = None
            self.pressing = None
            self.startButton['state'] = 'enabled'
            self.stopButton['state'] = 'disabled'
            return
        
        self.startButton['state'] = 'disabled'
        self.stopButton['state'] = 'enabled'
        self.progressBar.start()
        self.statusLabel['text'] = "Status: Starting in 3 sec"

        # 3 sec wait before starting to get to game window
        self.pressing = self.after(3000, self.waitToRun)


    def keyPress(self, key, release_deleay):
        pyautogui.keyDown(key)
        time.sleep(release_deleay)
        pyautogui.keyUp(key)


    def check_status(self):
        barColor = pyautogui.pixel(self.barLocation[0], self.barLocation[1])
        iconColor = pyautogui.pixel(self.iconLocation[0], self.iconLocation[1])

        # Able to cast
        if barColor == self.brownColor and iconColor == self.faceColor:
            self.statusLabel['text'] = "Status: Attempting cast"
            startDelay = np.random.uniform(0.2,0.7)
            releaseDelay = np.random.uniform(0.031,0.11)
            self.pressing = self.after(int(startDelay*1000), lambda: self.keyPress(self.castKey, releaseDelay))
            self.checking = self.after(int(self.stdWaitTime*3+(startDelay+releaseDelay)*1000), self.check_status)

        # Waiting for bite
        elif barColor == self.blueColor:
            self.statusLabel['text'] = "Status: Waiting for bite"
            self.checking = self.after(self.stdWaitTime, self.check_status)

        # Ready to catch
        elif barColor == self.greenColor:
            self.statusLabel['text'] = "Status: Attempting to catch"
            startDelay = np.random.uniform(0.68,1.68)
            releaseDelay = np.random.uniform(0.028,0.98)
            self.pressing = self.after(int(startDelay*1000), lambda: self.keyPress(self.catchKey, releaseDelay))
            self.checking = self.after(int(self.stdWaitTime+(startDelay+releaseDelay)*1000), self.check_status)

        # Baggin it
        elif iconColor == self.bagColor:
            self.statusLabel['text'] = "Status: Collecting Loot"
            self.configCount += 1
            self.totalCount['text'] = str(int(self.totalCount['text']) + 1)
            self.sessionCount['text'] = str(int(self.sessionCount['text'])+1)
            self.checking = self.after(int(np.random.uniform(4.0,4.25)*1000), self.check_status)

        # Not able to cast
        else:
            self.statusLabel['text'] = "Status: Waiting for valid cast location"
            self.checking = self.after(self.stdWaitTime, self.check_status)