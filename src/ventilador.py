from gpiozero import OutputDevice
from config.settings import *

class Ventilador():

    def __init__(self, pin: int):
        
        self.pin = pin
        self.fan = OutputDevice(pin)

    def on(self):
        self.fan.value = 1

    def off(self):
        self.fan.value = 0