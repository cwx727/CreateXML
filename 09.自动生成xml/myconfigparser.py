import configparser

class MyConfigParser(configparser.ConfigParser):
    def __init__(self, defaults=None):
        configparser.ConfigParser.__init__(self, defaults=defaults,allow_no_value=True)

    def optionxform(self, optionstr):
        return optionstr