# Cajero-TechBank-Riwi-Digital 🏦

Este proyecto es una simulación de un cajero automático desarrollado en Python. Permite a los usuarios realizar operaciones bancarias básicas de manera segura, aplicando validaciones de datos y reglas de negocio financieras.

## 📋 Contexto del Proyecto
Desarrollado para **TechBank Riwi Digital**, este sistema busca simular la interacción real de un cliente con un cajero, gestionando la autenticación, saldos y movimientos de dinero (depósitos y retiros) a través de una interfaz de consola mejorada.

## 🛠️ Estructura del Código

El proyecto se divide en tres módulos principales para garantizar una arquitectura limpia y modular:

### 1. `main.py` (Punto de Entrada)
Es el archivo principal que orquesta la ejecución del programa.
* Define el saldo inicial de **$1000**.
* Llama a la función de **autenticación** con un PIN predefinido (`1234`) y un límite de 3 intentos.
* Inicia el `menu_cajero()` una vez que el usuario accede exitosamente.

### 2. `utils.py` (Lógica de Negocio)
Contiene las funciones core que hacen que el cajero funcione:
* **`authentication(pin, intentos_pin)`**: 
    * Valida que el PIN ingresado sea numérico y tenga exactamente 4 dígitos.
    * Controla el contador de intentos restantes.
    * Bloquea la cuenta si se agotan los intentos.
* **`menu_cajero()`**: 
    * Contiene el bucle principal con las opciones de: *Consultar saldo*, *Retirar*, *Depositar* y *Salir*.
    * **Validaciones:** Controla que no se retiren montos superiores al saldo disponible ni se ingresen valores negativos o no numéricos.

### 3. `colores.py` (Interfaz Visual)
Este módulo se encarga de la estética del programa utilizando la librería `rich`.
* **Paneles:** Organiza la información en cuadros visuales.
* **Estilos:** Define colores específicos para cada situación:
    * `mensaje_error`: Rojo (para entradas inválidas o fondos insuficientes).
    * `mensaje_exito`: Verde (para operaciones exitosas).
    * `color_opcion`: Amarillo (para guiar al usuario en la selección).

---

## ⚙️ Requisitos e Instalación

Para ejecutar este proyecto, necesitas tener instalado Python y la librería `rich` para los efectos visuales.

1. **Instalar la dependencia:**
   ```bash
   pip install rich
2. **Ejecutar:**
   ```python
   python main.py
