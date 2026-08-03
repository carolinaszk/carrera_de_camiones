"""Archivo de código visual ASCII"""
import os
from colorama import Fore, Style, Back, init

class Camion:
    """Seteo del comportamiento de los camiones"""
    # estética fija start y finish
    FORE_WHITE = Style.BRIGHT + Fore.WHITE
    BACK_WHITE = Style.BRIGHT + Back.WHITE
    BACK_BLACK = Style.BRIGHT + Back.BLACK
    init(autoreset=True)

    START = [
        (FORE_WHITE + "|" + " " + " " + " " +  "|"),
        (FORE_WHITE + "|" + " " + "S" + " " +  "|"),
        (FORE_WHITE + "|" + " " + "T" + " " +  "|"),
        (FORE_WHITE + "|" + " " + "A" + " " +  "|"),
        (FORE_WHITE + "|" + " " + "R" + " " +  "|"),
        (FORE_WHITE + "|" + " " + "T" + " " +  "|"),
        (FORE_WHITE + "|" + " " + " " + " " +  "|"),
        (FORE_WHITE + "|" + " " + " " + " " +  "|")
        ]

    FINISH = [
        (BACK_WHITE + "  " + BACK_BLACK + "  " + BACK_WHITE + "  "),
        (BACK_BLACK + "  " + BACK_WHITE + "  " + BACK_BLACK + "  "),
        (BACK_WHITE + "  " + BACK_BLACK + "  " + BACK_WHITE + "  "),
        (BACK_BLACK + "  " + BACK_WHITE + "  " + BACK_BLACK + "  "),
        (BACK_WHITE + "  " + BACK_BLACK + "  " + BACK_WHITE + "  "),
        (BACK_BLACK + "  " + BACK_WHITE + "  " + BACK_BLACK + "  "),
        (BACK_WHITE + "  " + BACK_BLACK + "  " + BACK_WHITE + "  "),
        (BACK_BLACK + "  " + BACK_WHITE + "  " + BACK_BLACK + "  ")
        ]

    # constructor
    def __init__(self, nombre, color, ancho_pista=125):
        self.nombre = nombre
        self.color_ascii = Style.BRIGHT + color
        reset = Style.RESET_ALL

        # ancho total disponible para el movimiento de los camiones
        self.ancho_pista = ancho_pista

        # centrado del nombre del camion
        espacios_camion = (21 - len(self.nombre)) / 2
        if espacios_camion % 2 == 0:
            self.espacios_left = int(espacios_camion)
            self.espacios_right = int(espacios_camion)
        else:
            self.espacios_left = int(espacios_camion)
            self.espacios_right = 21 - len(self.nombre) - int(espacios_camion)

        # armado del dibujo ASCII
        camion_uno = " ______________         "
        camion_dos = "|__|__|__|__|__|______  "
        camion_tres = "|" + (" " * self.espacios_left) + reset + self.nombre.upper() + self.color_ascii + (" " * self.espacios_right) + "|)"
        camion_cuatro = "'~~~~" + reset + "@" + self.color_ascii + ("~" * 11) + reset + "@" + self.color_ascii + "~~~~' "

        self.dibujo_ascii = [
            (self.color_ascii + camion_uno),
            (self.color_ascii + camion_dos),
            (self.color_ascii + camion_tres),
            (self.color_ascii + camion_cuatro)
            ]

        # ubicación del camión dentro de la pista
        self.pos_izquierda = 0
        self.espacio_izquierda = " " * self.pos_izquierda
        self.pos_derecha = self.ancho_pista
        self.espacio_derecha = " " * self.pos_derecha

def dibujar_pista(camion_uno, camion_dos, usr_selection):
    """Armado de la pista"""
    print("¡Carrera de CAMIONES!\n"
        "Elegí tu favorito:\n"
        f"{camion_uno.color_ascii} • {camion_uno.nombre}\n"
        f"{camion_dos.color_ascii} • {camion_dos.nombre}\n")

    if usr_selection == 1:
        print(f"Favorito: {camion_uno.color_ascii + camion_uno.nombre}\n")
    if usr_selection == 2:
        print(f"Favorito: {camion_dos.color_ascii + camion_dos.nombre}\n")

    for lap in range(8):
        if lap <= 3:
            print(camion_uno.START[lap] + camion_uno.espacio_izquierda + camion_uno.dibujo_ascii[lap] + camion_uno.espacio_derecha + camion_uno.FINISH[lap])
        else:
            lap_camion = lap-4
            print(camion_dos.START[lap] + camion_dos.espacio_izquierda + camion_dos.dibujo_ascii[lap_camion] + camion_dos.espacio_derecha + camion_dos.FINISH[lap])

def limpiar_terminal():
    """Vaciar todo el contenido de debugging pasado de la consola"""
    os.system('cls' if os.name == 'nt' else 'clear')