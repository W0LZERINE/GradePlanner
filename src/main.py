### MAIN ###
from expediente import *
from menus import *
from evaluacion import *


##Aqui irá la carga del fichero:
evaluation = Evaluacion("Examen", 1, 10)
#Cómo no hay fichero de momento hacemos que asignaturas esté vació
a = Asignatura("Mates", 6, evaluation)

asignaturas = [a]


while True:


    menu_base()
    
    opcion = input_with_control()

    match opcion :
        case 0: #En esta opcion pondremos que imprima la asignatura con la nota media que lleva de momento
            menu_mostrar_asigntauras(asignaturas)
            if  asignaturas:
                print("Selecciona la asignatura que quieras ver sus evaluaciones o escribe -1 para volver")
                select = input_with_control()
                if select == -1:
                    break
                else:
                    mostrar_menu_evaluaciones(asignaturas[select])
            
            print("para salir introduzca una tecla")
            input("")# esto es para esperar a que toque una
            
        case 1:
            pass

        case 2:
            pass

        case 3:
            break

        case _:
            print("Opción no válida, introduzca una opción del 0 - 3\n")
