'''
#configuracion inicial del sistema
saldo_inicial = 1000
pin = 1234
intentos_pin = 3
funcion_de_bienvenida()
autenticacion() # se debe incluir control de intentos 
menu_operaciones()  #consultar saldo , retirar dinero , depositar dinero , salir
consultar()
retirar()
depositar()
salir()
funcion_de_despedida()
'''

# Saldo Inicial Del Cajero
Saldo = 1000
pin = "1234"

# Autenticación
def Autenticacion():
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

Autenticacion()
