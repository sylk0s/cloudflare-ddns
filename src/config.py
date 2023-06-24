# reads the config from the 
class ConfigReader:

    # reads the file
    def read(path):
        pass

class ClfJobConfig:
    def __init__(self, token, zone, freq, record_type, domain):
        self.__token = token
        self.__zone = zone
        self.__freq = freq
        self.__record_type = record_type
        self.__domain = domain

    @property
    def token(self):
        return self.__token

    @property
    def zone(self):
        return self.__zone

    @property
    def freq(self):
        return self.__freq

    @property
    def record_type(self):
        return self.__record_type

    @property
    def domain(self):
        return self.__domain

class AppConfig:
    
    def __init__(self, tasks):
        self.tasks = tasks