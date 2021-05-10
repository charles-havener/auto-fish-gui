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
        config['VARIABLES'] = {'Count': '100'}

        with open(self.filepath, 'w') as configfile:
            config.write(configfile)


    # Update an item in the config file
    def update_config(self, section, key, value):
        self.config.set(section, key, value)

