import configparser


def get_config(file_name:str)-> configparser.ConfigParser:
    config = configparser.ConfigParser()

    ini_file_path = "./resources/"+ file_name + ".ini"
    config.read(ini_file_path)
    return config

