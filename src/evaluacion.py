from asignatura import *

'''
    En esta clase guardaremos cada tipos de evaluacion examen, seminarios, prácticas ejercicios de clase que tenga la asignatura

'''
class Evaluacion:

    ###Constructores###

    def __init__(self, name, mark, ponderation):
        self._name = name
        self._mark = mark
        self._ponderation = ponderation

    def __init__(self,name,ponderation):
        self._name = name
        self._ponderation = ponderation
        self._mark = -1 # ponemos -1 si no hay nota


    ### Setters
    def set_name(self,name):
        self._name = name

    def set_ponderation(self,ponderation):
        self._ponderation = ponderation

    def set_mark(self,mark):
        self._mark = mark
