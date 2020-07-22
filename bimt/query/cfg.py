import os
import configparser
import pathlib

current_dir = str(pathlib.Path(__file__).parent.absolute())

CFG_FILE_PATH = os.environ.get("PC_CFG_FILE_PATH", current_dir + "/PC.CFG")

config = configparser.ConfigParser()
config.read(CFG_FILE_PATH)