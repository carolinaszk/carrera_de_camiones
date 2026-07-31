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

def resultado_final(camion1, camion2):
    """Establece el camión ganador y comparte los resultados"""
    if camion1.pos_derecha < camion2.pos_derecha:
        print(f"\n¡El ganador es {camion1.nombre.upper()}!!!\n")
    elif camion1.pos_derecha > camion2.pos_derecha:
        print(f"\n¡El ganador es {camion2.nombre.upper()}!!!\n")
    elif camion1.pos_derecha == camion2.pos_derecha:
        print("¡Los camiones EMPATARON!!!\n")

def juego_iniciado(camion1, camion2):
    """Se llama a esta función en main para comenzar el bucle del juego"""
    while True:
        # avance aleatorio entre 0 y 5 posiciones
        avance_uno = random.randint(0, 5)
        avance_dos = random.randint(0, 5)
        # se llama a la función que ejecuta el avance
        avanzar(camion1, avance_uno)
        avanzar(camion2, avance_dos)

        # limpia el resultado anterior y actualiza la posición de los camiones
        limpiar_terminal()
        dibujar_pista(camion1, camion2)

        # resultado parcial
        if camion1.pos_derecha < camion2.pos_derecha:
            print(f"\n¡El camión de {camion1.nombre} tiene la delantera!")
        elif camion1.pos_derecha > camion2.pos_derecha:
            print(f"\n¡El camión de {camion2.nombre} tiene la delantera!")
        elif camion1.pos_derecha == camion2.pos_derecha:
            print("\n¡Los camiones están empatando!")

        # condición que debe cumplirse para que el juego finalice
        if camion1.pos_derecha == 0 or camion2.pos_derecha == 0:
            break

        time.sleep(0.3)

    # una vez que termina el loop y hay un ganador, lo comunica
    resultado_final(camion1, camion2)
