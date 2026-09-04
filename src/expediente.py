### CLASE EXPEDIENTE ###
from expediente import *

class Expediente:
    def __init__(self,name):
        self._name = name
        self._asignaturas = [] #Array de assignaturas
        