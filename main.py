"""Main"""
import time
from colorama import Fore
from visuales import Camion, limpiar_terminal, dibujar_pista
from logica import juego_iniciado

def solicitar_nombre():
    """Solicita y valida el nombre para cada camión"""
    while True:
        nombre = input("Nombre: ")
        if not nombre:
            print("Error: El valor no puede estar vacío.")
        elif len(nombre) > 15:
            print("Error: Debe ingresar un nombre menor a 15 caracteres.")
        else:
            return nombre

def solicitar_color():
    """Solicita y valida el color de cada camión"""
    colores = {
        "1": (Fore.RED, "Rojo"),
        "2": (Fore.BLUE, "Azul"),
        "3": (Fore.GREEN, "Verde"),
        "4": (Fore.YELLOW, "Amarillo"),
        "5": (Fore.MAGENTA, "Rosa"),
        "6": (Fore.CYAN, "Turquesa")
        }

    # recorre el diccionario colores para mostrar las opciones
    for clave, (_, nombre_color) in colores.items():
        print(f"{clave}. {nombre_color}")

    # solicita el ingreso del usuario del color elegido
    while True:
        opcion = input("Color (1-6): ").strip()
        if opcion not in colores:
            print("Error: Debe ingresar una opción válida entre 1 y 6.")
        else:
            return colores[opcion][0]

def configurar_camion(numero, ancho_pista):
    """Une las funciones anteriores para construir un camión limpio."""
    print(f"\nCONFIGURACIÓN CAMIÓN N°{numero}.\n"
          "\n"
            f"Nombre del camión N°{numero}.\n"
            "Longitud máxima: 15 caracteres.")
    nombre = solicitar_nombre()
    print(f"\nColor del camión N°{numero}.\n"
          "Opciones: ")
    color = solicitar_color()
    return Camion(nombre=nombre, color=color, ancho_pista=ancho_pista)

def cambiar_ancho_pista():
    """Determina el tamaño de la pista"""
    print("\nSelección del tamaño de pista.\n"
          "Tamaño recomendado: 125-160 caracteres.")
    while True:
        caracteres = input("Tamaño de la pista: ")
        if caracteres == "":
            caracteres = 125
            return caracteres
        if caracteres.isdigit():
            return int(caracteres)
        print("Error: Debe ingresar un número entero.")

def solicitar_eleccion(camion_uno, camion_dos):
    """Solicita al usuario su favorito antes de comenzar a jugar"""
    while True:
        print(
            "\n¡Elegí tu camión favorito!\n"
            f"1. {camion_uno.nombre}\n"
            f"2. {camion_dos.nombre}\n"
            "3. Cancelar selección."
        )
        choice = input("Elegí tu camión favorito: ")
        if choice != "":
            if choice.isdigit():
                choice = int(choice)
                if choice in (1, 2):
                    return choice
                if choice == 3:
                    break
            else:
                print("Error: Debe ingresar un número válido.")
        else:
            print("Error: Debe ingresar un valor.")


def game():
    """Conecta los archivos y ejecuta el juego"""
    limpiar_terminal()
    # inicio del menú de opciones
    print( 
        "¡Bienvenido al juego CARRERA DE CAMIONES!\n"
        "Para poder comenzar, necesitamos recopilar la siguiente información:\n"
        " • El tamaño de la pista.\n"
        " • Nombre de los camiones.\n"
        " • Color de los camiones.")

    # ejecuta la creación de los objetos
    ancho_elegido = cambiar_ancho_pista()
    camion_uno = configurar_camion(1, ancho_elegido)
    camion_dos = configurar_camion(2, ancho_elegido)
    usr_selection = solicitar_eleccion(camion_uno, camion_dos)

    # muestra los cambios y comienza el juego
    limpiar_terminal()
    dibujar_pista(camion_uno, camion_dos, usr_selection)
    print()
    for i in range(5):
        print(f"{5 - i}...")
        time.sleep(1)

    # corre el funcionamiento del juego desde lógica
    juego_iniciado(camion_uno, camion_dos, usr_selection)

# protege que solo se ejecute en esta ventana
if __name__ == "__main__":
    game()
