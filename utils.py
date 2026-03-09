import datetime
from colores import *
import os
import time
from datetime import datetime


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def menu_cajero():
    
    saldo_inicial = 1000
    historial = []
    
    

    while True:

        clear()
        color_pagina_principal("Página principal:")
        subtitulo_panel("Opción 1 → Consultar saldo")
        subtitulo_panel("Opción 2 → Retirar saldo")
        subtitulo_panel("Opción 3 → Depositar saldo")
        subtitulo_panel("Opción 4 → Ver historial de transacciones")
        subtitulo_panel("Opción 5 → Cerrar sesión")

        try:
            color_opcion("Seleccione una opción: 1, 2, 3, 4 o 5")
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
                    nuevo_saldo = saldo_inicial - monto
                    mensaje_exito(f"Saldo restante: {nuevo_saldo}")
                    input("Presione Enter para continuar...")
                    historial_transacciones(saldo_inicial, monto, nuevo_saldo, historial, "retiro")
                    saldo_inicial = nuevo_saldo
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
                    nuevo_saldo = saldo_inicial + monto
                    mensaje_exito(f"Saldo restante: {nuevo_saldo}")
                    input("Presione Enter para continuar...")
                    historial_transacciones(saldo_inicial, monto, nuevo_saldo, historial, "deposito")
                    saldo_inicial = nuevo_saldo
                    break

        
        
        elif opcion == 4:
            clear()
            clear()
            print("Historial de transacciones:\n")

            if not historial:
                print("No hay transacciones registradas.")
            else:
                for i, transaccion in enumerate(historial, 1):
                    print(f"Transacción #{i}")
                    print("-" * 30)

                    for clave, valor in transaccion.items():
                        print(f"{clave.capitalize():20}: {valor}")

                    print("-" * 30)

            input("Presione Enter para continuar...")
                   
            
            

        elif opcion == 5:
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



def historial_transacciones(saldo_inicial, monto, nuevo_saldo, historial, tipo):
        registro = {
            "saldo inicial": saldo_inicial,
            f"monto de {tipo}": monto,
            f"hora del {tipo}": datetime.now().strftime("%H:%M:%S"),
            "saldo final": nuevo_saldo,                
                        }
        historial.append(registro)
                    

