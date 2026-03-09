from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich import box


console = Console()


def mensaje_reintentar(texto):
    console.print(
        Panel(
            Align.center(texto),
            border_style="yellow",
            style="bold yellow",
            padding=(0,1),
            width=50
        )
    )

def subtitulo_panel(texto):
    console.print(
        Panel(
            Align.left(f"[#a6d1ff]ℹ️  {texto}"),  #color azul claro 
            border_style="#30363d",  # Gris oscuro de lineas
            style="on #0d1117",      # fondo azul marino profundo
            box=box.ROUNDED,         # Bordes redondeados para diferenciar de la bienvenida
            width=50,
            padding=(0, 1)
        )
    )

def mensaje_error(texto):
    console.print(
        Panel(
            Align.center(f"[#ff7b72]🔴  {texto}"), #color rojo letra
            border_style="#30363d",  # Gris oscuro de lineas
            style="on #0d1117",      # fondo azul marino profundo
            box=box.ROUNDED,         # Bordes redondeados para diferenciar de la bienvenida
            width=50,
            padding=(0, 1)
        )
    )

def mensaje_exito(texto):
    console.print(
        Panel(
            Align.left(f"[bold #7ee787]✅  {texto}"), #color verde letra
            border_style="#30363d",  # Gris oscuro para no competir con el título principal
            style="on #0d1117",      # Mantenemos el fondo azul marino profundo
            box=box.ROUNDED,         # Bordes redondeados para diferenciar de la bienvenida
            width=50,
            padding=(0, 1)
        )
    )

def mensaje_info(texto):
    console.print(
        Panel(
            Align.center(f"[#a6d1ff]ℹ️  {texto}[/]", vertical="middle"), 
            border_style="#30363d",  # Gris oscuro 
            style="on #0d1117",      # Mantenemos el fondo azul
            box=box.ROUNDED,         # Bordes redondeados
            width=60,
            padding=(0, 1)
        )
    )

def color_pagina_principal(texto):
    # Usamos f-strings con etiquetas de Rich directamente para reducir líneas
    mensaje = f"\n[bold yellow]✨[/] [bold grey93]{texto.upper()}[/] [bold yellow]✨[/]\n"
    
    panel = Panel(
        Align.center(mensaje),
        title="[bold #58a6ff] 💎 TECHBANK RIWI 💎 [/]",
        border_style="#30363d",
        box=box.DOUBLE_EDGE,
        width=50,
        style="on #0d1117"
    )

    # Imprimimos todo en un solo bloque limpio
    console.print("\n" * 2, Align.left(panel), sep="")
    

def color_opcion(texto):
    console.print(
        Panel(
            Align.center(f"[bold #9d7cd8]🟣  {texto}"),
            border_style="#30363d",  # Gris oscuro 
            style="on #0d1117",      # Mantenemos el fondo azul 
            box=box.ROUNDED,         # Bordes redondeados 
            width=50,
            padding=(0, 1)
        )
    )
