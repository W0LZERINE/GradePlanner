from asignatura import *

'''
    En esta clase guardaremos cada tipos de evaluacion examen, seminarios, prácticas ejercicios de clase que tenga la asignatura

'''
class Evaluacion:

    ###Constructores###

    def __init__(self, name, ponderation, mark):
        self._name = name
        self._ponderation = ponderation
        if mark == None:
            self._mark = -1
        else:
            self._mark = mark



    ### Setters
    def set_name(self,name):
        self._name = name

    def set_ponderation(self,ponderation):
        self._ponderation = ponderation

    def set_mark(self,mark):
        self._mark = mark
