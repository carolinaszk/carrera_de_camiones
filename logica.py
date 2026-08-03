"""Archivo de lógica matemática del funcionamiento del juego"""
import random
import time
from visuales import limpiar_terminal, dibujar_pista

def avanzar(camion, steps):
    """Capacidad de avanzar posiciones"""
    # si el avance excede el limite de pista setea al maximo posible
    if camion.pos_derecha - steps < 0:
        camion.pos_derecha = 0
        camion.pos_izquierda = camion.ancho_pista
    else: # si no excede suma el avance
        camion.pos_izquierda += steps
        camion.pos_derecha -= steps
    # actualiza la posición
    camion.espacio_derecha = " " * camion.pos_derecha
    camion.espacio_izquierda = " " * camion.pos_izquierda

def resultado_final(camion_uno, camion_dos, usr_selection):
    """Establece el camión ganador y comparte los resultados"""
    camion_ganador = ""
    if camion_uno.pos_derecha < camion_dos.pos_derecha:
        print(f"\n¡El ganador es {camion_uno.nombre.upper()}!!!\n")
        camion_ganador = [1]
    elif camion_uno.pos_derecha > camion_dos.pos_derecha:
        print(f"\n¡El ganador es {camion_dos.nombre.upper()}!!!\n")
        camion_ganador = [2]
    elif camion_uno.pos_derecha == camion_dos.pos_derecha:
        print("¡Los camiones EMPATARON!!!\n")
        camion_ganador = [1, 2]

    if usr_selection is not None:
        if usr_selection in camion_ganador:
            print("¡Ganaste!!!\n")
        else:
            print("Perdiste :(\n")

def juego_iniciado(camion_uno, camion_dos, usr_selection=None):
    """Se llama a esta función en main para comenzar el bucle del juego"""
    while True:
        # avance aleatorio entre 0 y 5 posiciones
        avance_uno = random.randint(0, 5)
        avance_dos = random.randint(0, 5)
        # se llama a la función que ejecuta el avance
        avanzar(camion_uno, avance_uno)
        avanzar(camion_dos, avance_dos)

        # limpia el resultado anterior y actualiza la posición de los camiones
        limpiar_terminal()
        dibujar_pista(camion_uno, camion_dos, usr_selection)

        # resultado parcial
        if camion_uno.pos_derecha < camion_dos.pos_derecha:
            print(f"\n¡El camión de {camion_uno.nombre} tiene la delantera!")
        elif camion_uno.pos_derecha > camion_dos.pos_derecha:
            print(f"\n¡El camión de {camion_dos.nombre} tiene la delantera!")
        elif camion_uno.pos_derecha == camion_dos.pos_derecha:
            print("\n¡Los camiones están empatando!")

        # condición que debe cumplirse para que el juego finalice
        if camion_uno.pos_derecha == 0 or camion_dos.pos_derecha == 0:
            break

        time.sleep(0.3)

    # una vez que termina el loop y hay un ganador, lo comunica
    resultado_final(camion_uno, camion_dos, usr_selection)
