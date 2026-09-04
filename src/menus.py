
def menu_base():
    print("--- GRADE PLANNER ---")
    print("0. Ver asignaturas")
    print("1. Editar asignaturas")
    print("2. Añadir/Eliminar asignaturas")
    print("3. Salir\n")


def menu_mostrar_asigntauras(asignaturas):
    
    print("--- ASIGNATURAS ---")
    if not asignaturas:
        print("No hay asignaturas registradas.")
    else:
        for i, asignatura in enumerate(asignaturas):
            print(f"{i}. {asignatura}")
        print(f"{len(asignaturas)}. Volver al menú principal\n")


def menu_editar_asignatura():
    print("--- EDITAR ASIGNATURA ---")
    print("0. Editar Nombre")
    print("1. Editar Evaluaciones")
    print("2. Volver al menú principal\n")

# ESTE SERVIRA PARA CUANDO RECIVAMOS UN ARRAY DE EVALUACIONES
def mostrar_menu_evaluaciones(evaluaciones):
    print("--- EVALUACIONES ---")

    if not evaluaciones:
        print("No hay evaluaciones registradas.")
    else:
        for i, evaluacion in enumerate(evaluaciones):
            print(f"{i}. {evaluacion}")
        print(f"{len(evaluaciones)}. Volver al menú principal\n")

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
    try:
        opcion = int(input("Selecciona una opción válida: "))
    except ValueError:
        print("Error no has seleccionado una opción válida")
    else:
        return opcion