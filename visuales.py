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

def dibujar_pista(camion1, camion2):
    """Armado de la pista"""
    print("¡Carrera de CAMIONES!\n"
        "Elegí tu favorito:\n"
        f"{camion1.color_ascii} • {camion1.nombre}\n"
        f"{camion2.color_ascii} • {camion2.nombre}\n")
    for lap in range(8):
        if lap <= 3:
            print(camion1.START[lap] + camion1.espacio_izquierda + camion1.dibujo_ascii[lap] + camion1.espacio_derecha + camion1.FINISH[lap])
        else:
            lap_camion = lap-4
            print(camion2.START[lap] + camion2.espacio_izquierda + camion2.dibujo_ascii[lap_camion] + camion2.espacio_derecha + camion2.FINISH[lap])

def limpiar_terminal():
    """Vaciar todo el contenido de debugging pasado de la consola"""
    os.system('cls' if os.name == 'nt' else 'clear')
