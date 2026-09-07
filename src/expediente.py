### CLASE EXPEDIENTE ###
from asignatura import *


class Expediente:
    def __init__(self,name):
        self._name = name
        self._asignaturas = [] #Array de assignaturas


    def set_name(self,name):
        self._name = name

    def añadir_asignatura(self,asignatura):
        self._asignaturas.append(asignatura)

    def eliminar_asignatura(self,input):
        try:
            self._asignaturas.remove(input)
        except ValueError:
            print("Error: no se ha podido eliminar esa asignatura, no existe.\n")

    