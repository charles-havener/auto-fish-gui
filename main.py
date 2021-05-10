import tkinter as tk

# Classes from other files
from resources.application import Application
from resources.config import ConfigFile


def main():
    cfg = ConfigFile()

    root = tk.Tk()
    app = Application(config=cfg, master=root)
    app.mainloop()




    #TODO Create some logs just for funzies
    # everytime something happens in app
    # [date:time] - What happened



    #TODO: on gui close update total count in .ini
    #TODO: should be this -> cfg.update_config("VAIRIABLES", "Count", app.totalCount)


if __name__ == "__main__":
    main()