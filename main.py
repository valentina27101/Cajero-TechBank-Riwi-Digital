from utils import *
import os
import time 

def clear():
    os.system("cls" if os.name == "nt" else "clear")


Saldo = 1000


clear()
color_pagina_principal("Bienvenid@ al cajero TechBank de Riwi")


authentication(pin="1234", intentos_pin=3)


clear()


time.sleep(1)  

saldo_inicial = 1000


menu_cajero()