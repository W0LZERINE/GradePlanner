### MAIN ###

from expediente import *
from menus import *

while True:
    menu_base()

    opcion = input_with_control()

    match opcion :
        case 0:
            pass