## Cajero-TechBank-Riwi-Digital
## Descripción
Este proyecto tiene como proposito crear un simulador de cajero automático en consola utilizando Python.
El programa permite que el usuario ingrese un PIN para autenticarse y, una vez dentro del sistema, pueda realizar diferentes operaciones básicas como consultar su saldo, retirar dinero, depositar dinero o ver el historial de movimientos.

## Objetivo

El objetivo del proyecto es aplicar conceptos básicos de programación en Python, como el uso de funciones, estructuras condicionales, ciclos y validación de datos.
Además, busca fomentar el trabajo en equipo y el uso de herramientas de control de versiones para el desarrollo colaborativo.

## Funciones
El sistema del cajero incluye las siguientes funciones principales:
- authentication(): se encarga de verificar el PIN del usuario antes de permitir el acceso al sistema.
- menu_cajero(): muestra el menú principal y permite al usuario seleccionar las operaciones disponibles.
-Funciones de formato del módulo colores: se utilizan para mostrar mensajes organizados en la consola (títulos, errores, opciones y mensajes de éxito).

## Reglas del sistema
El cajero sigue algunas reglas para garantizar su correcto funcionamiento:
- El usuario debe ingresar un PIN de 4 dígitos para acceder al sistema.
- El PIN solo puede contener números.
- El usuario tiene un número limitado de intentos para ingresar el PIN.
- No se puede retirar una cantidad mayor al saldo disponible.
- No se permiten montos negativos o iguales a cero en depósitos o retiros.
- El sistema valida que los datos ingresados sean números válidos.

## Flujo del cajero
El funcionamiento general del programa sigue el siguiente flujo:

1. El sistema solicita al usuario ingresar su PIN.

2. Si el PIN es correcto, el sistema muestra un mensaje de bienvenida.

3. Se presenta el menú principal del cajero.

4. El usuario puede elegir entre:

 - Consultar saldo.
 - Retirar dinero.
 - Depositar dinero.
 - Historial de movimientos.
 - Cerrar sesión.

5. El sistema valida cada operación antes de ejecutarla.

6. Cuando el usuario selecciona cerrar sesión, el programa finaliza.

## Estructura del proyecto

main.py → archivo principal que ejecuta el programa  
utils.py → contiene funciones como authentication() y menu_cajero()  
colores.py → contiene funciones para mostrar mensajes con formato en consola

## Cómo ejecutar el proyecto

1. Clonar el repositorio.
2. Abrir el proyecto en Visual Studio Code.
3. Ejecutar el archivo principal con Python.

## Tecnologías utilizadas

- Python
- Git
- Github

## Integrantes

- Mateo Hernandez
- Guillermo Leaño
- Valentina Pacheco


