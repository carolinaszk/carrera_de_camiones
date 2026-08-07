"""Archivo de lógica matemática del funcionamiento del juego"""
import random
import time
import csv
import os
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

def guardar_resultados(favoritos, ganadores):
    """Carga el csv y lo actualiza"""
    elecciones = favoritos
    jugadores_ganadores = ganadores
    jugadores_score = []

    resultados_file = "resultados.csv"
    file_exists = os.path.exists(resultados_file)

    # si el csv existe, lo abre y lo lee, y a los ganadores que existen los actualiza
    if not file_exists:
        pass
    else:
        with open("resultados.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            jugadores_score = list(reader)
            if jugadores_score and jugadores_ganadores:
                for player in jugadores_score:
                    if player["username"] in jugadores_ganadores:
                        player["cantidad_wins"] = int(player["cantidad_wins"]) + 1

    # si hay elecciones para guardar que no esten ya los suma al csv recuperado
    if elecciones:
        for player in elecciones:
            usuarios_logueados = [player["username"] for player in jugadores_score]
            if player["username"] not in usuarios_logueados:
                if player["username"] in jugadores_ganadores:
                    jugador_agregar = {
                        "username": player["username"], 
                        "nombre": player["nombre"], 
                        "cantidad_wins": 1
                        }
                    jugadores_score.append(jugador_agregar)
                else:
                    jugador_agregar = {
                        "username": player["username"], 
                        "nombre": player["nombre"], 
                        "cantidad_wins": 0
                        }
                    jugadores_score.append(jugador_agregar)

    # sobreescribe el csv pasado con el resultado nuevo
    with open(resultados_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["username", "nombre", "cantidad_wins"])
        if jugadores_score:
            for player in jugadores_score:
                jugador_add = [player["username"], player["nombre"], player["cantidad_wins"]]
                writer.writerow(jugador_add)

    # ordena el total por mayor cantidad de wins
    jugadores_ordenados = []
    if jugadores_score:
        jugadores_ordenados = sorted(
            jugadores_score,
            key=lambda jugador: int(jugador["cantidad_wins"]), 
            reverse=True)

    # recupera los primeros 3 y los imprime por pantalla
    if jugadores_ordenados:
        top_tres = jugadores_ordenados[:3]
        print("TOP SCORES:")
        for player in top_tres:
            print(f"{player["nombre"]} ({player["username"]}): {player["cantidad_wins"]} wins")

def resultado_final(camion_uno, camion_dos, favoritos=None):
    """Establece el camión ganador y comparte los resultados"""
    camion_ganador = []
    if camion_uno.pos_derecha < camion_dos.pos_derecha:
        print(f"\n¡El ganador es {camion_uno.nombre.upper()}!!!\n")
        camion_ganador.append(1)
    elif camion_uno.pos_derecha > camion_dos.pos_derecha:
        print(f"\n¡El ganador es {camion_dos.nombre.upper()}!!!\n")
        camion_ganador.append(2)
    elif camion_uno.pos_derecha == camion_dos.pos_derecha:
        print("¡Los camiones EMPATARON!!!\n")
        camion_ganador.append(1,2)

    jugadores_ganadores = []
    jugadores_ganadores_print = []
    elecciones = favoritos

    # si hay jugadores separa los ganadores
    if elecciones:
        for player in elecciones:
            if player["opcion"] in camion_ganador:
                jugadores_ganadores.append(player["username"])
                jugadores_ganadores_print.append(player["nombre"])

    if jugadores_ganadores_print:
        print(f"Ganadores: {', '.join(jugadores_ganadores_print)}!!!\n")

    guardar_resultados(elecciones, jugadores_ganadores)

def juego_iniciado(camion_uno, camion_dos, favoritos):
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
        dibujar_pista(camion_uno, camion_dos, favoritos)

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
    resultado_final(camion_uno, camion_dos, favoritos)
