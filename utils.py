from colores import *
import os
import time

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def menu_cajero():

    saldo_inicial = 1000

    while True:

        clear()
        color_pagina_principal("Página principal:")
        subtitulo_panel("Opción 1 → Consultar saldo")
        subtitulo_panel("Opción 2 → Retirar saldo")
        subtitulo_panel("Opción 3 → Depositar saldo")
        subtitulo_panel("Opción 4 → Cerrar sesión")

        try:
            color_opcion("Seleccione una opción: 1, 2, 3 o 4")
            opcion = int(input("→ "))

        except ValueError:
            mensaje_error("Debe ingresar un número válido, intente nuevamente")
            input("Presione Enter para continuar...")
            continue 

        if opcion == 1:
            clear()
            mensaje_exito(f"El monto actual es: {saldo_inicial}")
            input("Presione Enter para volver al menú...")

        elif opcion == 2:
            while True:
                clear()
                subtitulo_panel("¿Cuánto dinero desea retirar?")

                try:
                    monto = float(input("→ "))
                except ValueError:
                    mensaje_error("Debe ingresar un número válido, intente nuevamente")
                    input("Presione Enter para reintentar...")
                    continue

                if monto > saldo_inicial:
                    mensaje_error("No puede retirar más de su saldo actual")
                    input("Presione Enter para reintentar...")
                    continue

                elif monto <= 0:
                    mensaje_error("Monto inválido")
                    input("Presione Enter para reintentar...")
                    continue

                else:
                    saldo_inicial -= monto
                    mensaje_exito(f"Saldo restante: {saldo_inicial}")
                    input("Presione Enter para continuar...")
                    break

        elif opcion == 3:
            while True:
                clear()
                subtitulo_panel("¿Cuánto dinero desea depositar?")

                try:
                    monto = float(input("→ "))
                except ValueError:
                    mensaje_error("Debe ingresar un número válido")
                    input("Presione Enter para reintentar...")
                    continue

                if monto <= 0:
                    mensaje_error("Monto inválido")
                    input("Presione Enter para reintentar...")
                    continue
                else:
                    saldo_inicial += monto
                    mensaje_exito(f"Saldo restante: {saldo_inicial}")
                    input("Presione Enter para continuar...")
                    break

        elif opcion == 4:
            clear()
            mensaje_exito("Gracias por usar el cajero Tech Bank Riwi")
            time.sleep(3)
            break

        else:
            mensaje_error("Opción inválida")
            input("Presione Enter para reintentar...")


def authentication(pin, intentos_pin):

    while intentos_pin > 0:

        clear()
        subtitulo_panel("Ingrese su PIN: ")
        pin_usuario = input("→ ")

        if not pin_usuario.isdigit():
            mensaje_error("Error: el PIN solo debe tener números.")
            intentos_pin -= 1
            color_pagina_principal(f"Intentos restantes: {intentos_pin}")
            input("Presione Enter para reintentar...")
            continue

        if len(pin_usuario) != 4:
            mensaje_error("Error: el PIN debe tener 4 dígitos.")
            intentos_pin -= 1
            color_pagina_principal(f"Intentos restantes: {intentos_pin}")
            input("Presione Enter para reintentar...")
            continue

        if pin_usuario == pin:
            clear()
            mensaje_exito("Iniciaste sesión correctamente")
            time.sleep(2)
            break

        else:
            intentos_pin -= 1
            mensaje_error("PIN incorrecto")
            color_pagina_principal(f"Intentos restantes: {intentos_pin}")
            input("Presione Enter para reintentar...")

    if intentos_pin == 0:
        clear()
        mensaje_error("Cuenta bloqueada")
        exit()