def menu_cajero():
    from colores import subtitulo_panel
    from colores import mensaje_error, mensaje_exito, mensaje_info
    from colores import color_pagina_principal
    from colores import color_opcion

    saldo_inicial = 1000

    while True:

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
            continue 

        if opcion == 1:
            mensaje_exito(f"El monto actual es: {saldo_inicial}")

        elif opcion == 2:
            while True:
                subtitulo_panel("¿Cuánto dinero desea retirar?")

                try:
                    monto = float(input("→ "))
                except ValueError:
                    mensaje_error("Debe ingresar un número válido, intente nuevamente")
                    continue

                if monto > saldo_inicial:
                    mensaje_error("No puede retirar más de su saldo actual, intente nuevamente")
                    continue

                elif monto <= 0:
                    mensaje_error("Monto inválido, intente nuevamente")
                    continue

                else:
                    saldo_inicial -= monto
                    mensaje_exito(f"Saldo restante: {saldo_inicial}")
                    break

        elif opcion == 3:
            while True:
                subtitulo_panel("¿Cuánto dinero desea depositar?")

                try:
                    monto = float(input("→ "))
                except ValueError:
                    mensaje_error("Debe ingresar un número válido, intente nuevamente")
                    continue

                if monto <= 0:
                    mensaje_error("Monto inválido, intente nuevamente")
                    continue
                else:
                    saldo_inicial += monto
                    mensaje_exito(f"Saldo restante: {saldo_inicial}")
                    break

        elif opcion == 4:
            mensaje_exito("Gracias por usar el cajero Tech Bank Riwi")
            break

        else:
            mensaje_error("Opción inválida")
def authentication(pin, intentos_pin):
    while intentos_pin > 0:
        
        pin_usuario = input("Ingrese su PIN: ")
    
        # Validar que solo tenga números
        if not pin_usuario.isdigit():
            print("Error: el PIN solo debe tener numeros.")
            intentos_pin -= 1
            print("Intentos restantes:", intentos_pin)
            continue

        # Validar que tenga 4 dígitos
        if len(pin_usuario) != 4:
            print("Error: el PIN debe tener 4 digitos.")
            intentos_pin -= 1
            print("Intentos restantes:", intentos_pin)
            continue
    
        if pin_usuario == pin:
            print("Acceso permitido")
            break
        else: 
            intentos_pin -= 1
            print("PIN incorrecto")
            print("Intentos restantes:", intentos_pin)

    if intentos_pin == 0:
        print("Cuenta bloqueada")
