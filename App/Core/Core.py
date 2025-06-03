import logging.config
from Core.Components.Initializer import Initializer
from kivy.logger import Logger

class Core:
    def __init__(self):
        self.initializer = Initializer(self)
        Logger.debug("Core initialized")