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
        config['COORDINATES'] = {
            'bar': '(0,0)',
            'icon': '(0,0)',
        }
        config['COLORS'] = {
            'brown_bar': '(0,0,0)',
            'blue_bar': '(0,0,0)',
            'green_bar': '(0,0,0)',
            'face_color': '(0,0,0)',
        }
        # TODO: store x,y coordinates
        # TODO: store colors #should be the same for all (from addon)
            # only need face color since every icon has a different bar color except for brown
            # if brown check if also face, if not than catch, if so then cast

        with open(self.filepath, 'w') as configfile:
            config.write(configfile)

    # Update an item in the config file
    def update_config(self, section, key, value):
        self.config.set(section, key, value)
        with open(self.filepath, 'w+') as configfile:
            self.config.write(configfile)

