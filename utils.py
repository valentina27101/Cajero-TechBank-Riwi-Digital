def autenticacion():
    intentos_pin = 3 

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
