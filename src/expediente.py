### CLASE EXPEDIENTE ###
from asignatura import *


class Expediente:
    def __init__(self,name):
        self._name = name
        self._asignaturas = [] #Array de assignaturas


    def set_name(self,name):
        self._name = name