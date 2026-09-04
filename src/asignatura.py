### CLASE ASSIGNATURA ###

'''
Estructura clase Assignatura guardaremos el nombre, los creditos, y los criterios es decir sus ponderaciones: 

name
ects

diccionario = {nombre de la prueba : {ponderacion : nota} }

Aqui no editaremos las notas, las notas las añadiremos desde otra funcion en el main que ya crearemos

'''


class Assignatura:

    # CONSTRUCTOR
    def __init__(self,name,ects):
        self._name = name
        self._ects = ects
        self._ponderation = {}  # El formato del diccionarios será prueba -> ponderación -> nota

    ### METODOS ###

    #Setters
    def set_name(self,name):
        self._name = name

    def set_ects(self,ects):
        self._ects = ects

    
    # Los métodos: add_pond y remove_pond metodos privados de la clase para el método edit_pond
    
    def add_ponderetion(self,name, ponderation, grade = None):
        self._ponderation[name] = { ponderation: grade}

    def remove_ponderation(self,name):
        del self._ponderation[name]


    ##################################################################################################################
    ### Funciones para el edit_ponderation ###
    
    # Muestra todas las ponderaciones
    def _show_pond(self):
            for name, ponderation in self._ponderation.items():
                for ponderation_value in ponderation.keys():
                    print(f"Type : ({name}), ponderation: ({ponderation_value})")
    
    # Funcion que devuelve un -1 si hay un valueerror en el input y devuelve el input si no
    def value_error_control():
        try: 
            num = int(input("Selecciona una opción: "))
        except ValueError:
            print("Error: no has introducido un valor de tipo int vuelve a intentar.\n")
            num = -1
        finally:
            return num

    #Editar el key
    def pond_option_one(): 
        pass
    #Editar el valor de la ponderación
    def pond_option_two():
        pass

    ##################################################################################################################
        
    def edit_pond(self):
        #comprobamos que no esté vacío el diccionario
        if not self._ponderations:
            print("No hay ninguna ponderación assignada")
            return 
        
        else:
            #Mostramos menú
            print("EDITAR PONDERACION\n")
            print("\n\n---------------------\n")
            print("1.Cambiar tipo de prueba\n2.Cambiar ponderacion de una prueba")
            print("---------------------\n")

            num = -1
            while num != (1 or 2):
                num = self.value_error_control()

            self._show_pond()

            # Cambiar la key del diccionario        
            if num == 1:
                pass
            elif num == 2: 
                pass
                
        