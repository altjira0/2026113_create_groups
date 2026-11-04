# FORMACIÓN ALEATORIA DE EQUIPOS
# Este programa solicita el número y nombres de los participantes y los distribuye aleatoriamente en equipos del tamaño indicado.
# No acepta nombres vacíos y, si sobran participantes, forma un último equipo con menos miembros.

import random

# 1. Pedir el número de participantes
numero_participantes = int(input("Número de participantes: "))

while numero_participantes <= 0:
    print("El número debe ser mayor que cero.")
    numero_participantes = int(input("Número de participantes: "))

# Crear una lista con una posición para cada participante
participantes = [""] * numero_participantes

# 2. Pedir los nombres
contador = 0

while contador < numero_participantes:
    nombre = input("Nombre del participante " + str(contador + 1) + ": ")
    

    if nombre == "":
        print("No has escrito un nombre. Este participante no cuenta.")
    else:
        participantes[contador] = nombre
        contador = contador + 1

# 3. Pedir el tamaño de los equipos
miembros_equipo = int(input("Número de personas por equipo: "))

while miembros_equipo <= 0:
    print("El tamaño del equipo debe ser mayor que cero.")
    miembros_equipo = int(input("Número de personas por equipo: "))

#Mostramos por pantalla la lista de participantes antes de mezclarla
print("\nLista de participantes antes de realizar equipos:")
print("Tal cual los has introducido, sin mezclar:")
print ("\n")
print(participantes)
print ("\n")
print("\nMezclando aleatoriamente...")



# Mezclar los nombres aleatoriamente
random.shuffle(participantes)
print(participantes)
print("\nEsta lista muestra los nombres en un orden aleatorio tal cual se van a distribuir en equipos")

# 4. Mostrar los equipos
posicion = 0
numero_equipo = 1

print("\nEQUIPOS FORMADOS")

while posicion < numero_participantes:
    print("\nEquipo", numero_equipo)
    miembros = 0

    while miembros < miembros_equipo and posicion < numero_participantes:
        print("-", participantes[posicion])
        posicion = posicion + 1
        miembros = miembros + 1

    numero_equipo = numero_equipo + 1