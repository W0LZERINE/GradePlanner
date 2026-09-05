

def menu_base():
    print("--- GRADE PLANNER ---")
    print("0. Ver asignaturas y notas")
    print("1. Editar asignaturas")
    print("2. Añadir/Eliminar asignaturas")
    print("3. Salir\n")


def menu_mostrar_asigntauras(asignaturas):
    
    print("--- ASIGNATURAS ---")
    if asignaturas:
        for i, asignatura in enumerate(asignaturas):
                print(f"{i}. {asignatura._name.upper()}")
                print(f"{len(asignaturas)}. Volver al menú principal\n")
        
    else:
        print("No hay asignaturas registradas.\nIntroduce cualquier tecla para volver")
        input()


def menu_editar_asignatura():
    print("--- EDITAR ASIGNATURA ---")
    print("0. Editar Nombre")
    print("1. Editar Evaluaciones")
    print("2. Volver al menú principal\n")

# ESTE SERVIRA PARA CUANDO RECIVAMOS UN ARRAY DE EVALUACIONES
def mostrar_menu_evaluaciones(asignatura):
    print(f"--- EVALUACIONES de la asignatura {(asignatura._name).upper()}---")

    if not asignatura._evaluation:
        print(f"No hay evaluaciones registradas para la asignatura {asignatura._name.upper()}.\nIntroduce cualquier tecla para volver")
        input()
    else:
        for i, evaluacion in enumerate(asignatura._evaluation):
            print(f"{i}. {evaluacion._name} cuenta un {int(evaluacion._ponderation*100) }")
        print(f"{len(asignatura._evaluation)}. Volver al menú principal\n")

def menu_editar_evaluacion():
    print("--- EDITAR DETALLES DE EVALUACIÓN ---")
    print("0. Cambiar nombre")
    print("1. Cambiar nota")
    print("2. Cambiar ponderación")
    print("3. Volver\n")

def menu_añadir_eliminar():
    print("--- AÑADIR / ELIMINAR ASIGNATURAS ---")
    print("0. Añadir asignatura")
    print("1. Eliminar asignatura")
    print("2. Volver al menú principal\n")




def exit():
    print("Saliendo...")




def input_with_control():
    while True:
        try:
            opcion = int(input("Selecciona una opción válida: "))
        except ValueError:
            print("Error has seleccionado una opción NO válida")
        else:
            return opcion