### MAIN ###

from expediente import *
from menus import *

##Aqui irá la carga del fichero:

#Cómo no hay fichero de momento hacemos que asignaturas esté vació

asignaturas = []


while True:


    menu_base()
    
    opcion = input_with_control()

    match opcion :
        case 0: #En esta opcion pondremos que imprima la asignatura con la nota media que lleva de momento
            menu_mostrar_asigntauras(asignaturas)
            print("para salir introduzca una tecla")
            p = input()

        case 1:
            pass

        case 2:
            pass

        case 3:
            break

        case _:
            print("Opción no válida, introduzca una opción del 0 - 3\n")
