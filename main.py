from utils import *
import os
import time 

def clear():
    os.system("cls" if os.name == "nt" else "clear")

clear()
color_pagina_principal("Bienvenid@ al cajero TechBank de Riwi")
time.sleep(2)  

authentication(pin="1234", intentos_pin=3)
clear()
time.sleep(1)  

menu_cajero()
