from VATTUBOY.application import Application
import configparser

def get_config_parser():
    config_string = ""
    with open("vattuboy.config", "r") as config_file:
        config_string = config_file.read()
        config_file.close()
    
    config_parser = configparser.ConfigParser()
    config_parser.read_string(config_string)
    return config_parser

def launcer():
    new_application = Application(get_config_parser())
    new_application.initialize()
    new_application.run()


if __name__ == "__main__":
    launcer()