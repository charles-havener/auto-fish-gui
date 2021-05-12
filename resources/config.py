from pathlib import Path
import configparser
import os

class ConfigFile():
    def __init__(self, filepath="resources/config.ini"):
        self.filepath = filepath

        # Check for config file and create one if it doesn't exist.
        config_file = Path(self.filepath)
        if not config_file.is_file():
            self.__create_config()

        # Set the config file
        self.config = configparser.ConfigParser()
        self.config.read(self.filepath)


    # Create a new config file
    def __create_config(self):
        print(f"Creating config file: {self.filepath}")

        # set up the config_file
        config = configparser.ConfigParser()
        config['VARIABLES'] = {
            'count': '100'
        }
        config['KEYBINDS'] = {
            'cast_key': 'y',
            'catch_key': 'y',
        }
        # check comment on bottom for how to get coordinates/colors
        config['COORDINATES'] = {
            'bar': '(2761,1009)',
            'icon': '(2787,1068)',
        }
        config['COLORS'] = {
            'brown_bar': '(101,69,0)',
            'blue_bar': '(75,156,213)',
            'green_bar': '(0,204,0)',
            'face_color': '(255,204,77)',
            'bag_color': '(253,216,137)',
        }
        
        with open(self.filepath, 'w') as configfile:
            config.write(configfile)

    # Update an item in the config file
    def update_config(self, section, key, value):
        self.config.set(section, key, value)
        with open(self.filepath, 'w+') as configfile:
            self.config.write(configfile)

"""
To get (x,y) locaitons and (R,G,B) values:

in cmd with venv that has pyautogui
$ python
>> import pyautogui
>> pyautogui.displayMousePosition()

will print out the informaiton as the cursor moves on screen.

"""