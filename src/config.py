import os

class ClfJobConfig:
    def __init__(self, token, zone, freq, record_type, domain):
        self.__token = token
        self.__zone = zone
        self.__freq = freq
        self.__record_type = record_type
        self.__domain = domain

    def __init__(self):
        self.__token = os.getenv("TOKEN")
        self.__zone = os.getenv("ZONE")
        self.__freq = int(os.getenv("FREQ"))
        self.__record_type = os.getenv("TYPE")
        self.__domain = os.getenv("DOMAIN")

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