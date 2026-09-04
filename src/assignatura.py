### CLASE ASSIGNATURA ###

class Assignatura:

    # CONSTRUCTOR
    def __init__(self,name,ects):
        self._nombre = name
        self._ects = ects
        self._ponderaciones = {}

    ### METODOS ###

    def set_name(self):
        pass
    def set_ects(self):
        pass

    
    # Los métodos: add_pond y remove_pond metodos privados de la clase para el método edit_pond
    
    def _add_pond(self,key,val):
        pass
    def _remove_pond(self,key):
        pass

    '''
        edit_pond permite añadir o eliminar o editar el atributo pond para los diferentes métodos de avaluación
    '''
    def edit_pond(self):
        pass