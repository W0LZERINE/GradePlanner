### CLASE ASSIGNATURA ###

'''
Estructura clase Assignatura guardaremos el nombre, los creditos, y un objeto que sea avaluación, dónde iran las notas  

name
ects

Evaluacion : objeto que guarda notas

Aqui no editaremos las notas, las notas las añadiremos desde otra funcion en el main que ya crearemos

'''
from evaluacion import *

class Assignatura:

    # CONSTRUCTOR
    def __init__(self,name,ects,evaluation):
        self._name = name
        self._ects = ects
        self._evaluation = []
        
########################################################
    

    ###Setters###
    def set_name(self,name):
        self._name = name

    def set_ects(self,ects):
        self._ects = ects

########################################################

### METODOS ###

    def add_evaluation(self,evaluation):
        self._evaluation.append(evaluation)

    def remove_evaluation(self,name):
            try:
                self._evaluation.remove(name)
            except ValueError:
                print("Error: no existe un elemento con ese nombre.\n")

## Debe de haber dos edit uno para arrays y otro para objetos solos