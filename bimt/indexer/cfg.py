import os
import configparser
import pathlib

current_dir = str(pathlib.Path(__file__).parent.absolute())

CFG_FILE_PATH = os.environ.get("GLI_CFG_FILE_PATH", current_dir + "/GLI.CFG")

# config = configparser.ConfigParser()
# config.read(CFG_FILE_PATH)

def mnual_parse_config(path):

    with open(path, "r") as f:
        lines = f.readlines()        

    config = {"DEFAULTS": {
        "LEIA": [],
        "ESCREVA": ""
    }}

    for l in lines:
        if "LEIA" in l:
            config["DEFAULTS"]["LEIA"].append(l.split("=")[1].strip("\n "))
        if "ESCREVA" in l:
            config["DEFAULTS"]["ESCREVA"] = l.split("=")[1].strip("\n ")

    return config

config = mnual_parse_config(CFG_FILE_PATH)  