import tkinter as tk

# Classes from other files
from resources.application import Application
from resources.config import ConfigFile


def main():
    cfg = ConfigFile()

    root = tk.Tk()
    app = Application(config=cfg, master=root)
    app.mainloop()


    # Update config file with new total count on GUI close
    cfg.update_config("VARIABLES", "count", str(app.configCount))


    #TODO Create some logs just for funzies
    # everytime something happens in app
    # [date:time] - What happened

if __name__ == "__main__":
    main()