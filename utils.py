#aqui van todas las funciones
funcion_de_despedida():
    from rich.console import Console
    from rich.panel import Panel

    console = Console()

    mensaje = "💳 Gracias por usar el cajero automático\n¡Vuelva pronto!"

    console.print(Panel(mensaje, style="yellow", title="Banco"))
