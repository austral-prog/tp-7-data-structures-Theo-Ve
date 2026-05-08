# Ejercicios de tuplas: búsqueda del tesoro pirata


def get_coordinate(registro):
    return registro [1]

def convert_coordinate(coordenada):
    primera = coordenada [:-1]
    segunda = coordenada [-1]
    return (primera, segunda)

def create_record(registro_azara, registro_rui):
    tesoro, coord_azara = registro_azara
    ubicacion, coord_rui, cuadrante = registro_rui

    if coord_azara == coord_rui[0] + coord_rui[1]:
        return (tesoro, coord_azara, ubicacion, coord_rui, cuadrante)

    return "not a match"

def sum_tuple(numeros):
    if len(numeros) == 0:
        return 0
    else:
        total = 0
        for numero in numeros:
            total += numero
        return total


def count_occurrences(tupla, elemento):
    contador = 0
    for item in tupla:
        if item == elemento:
            contador += 1
    return contador

def find_index(tupla, elemento):
    for indice, item in enumerate(tupla):
        if item == elemento:
            return indice
    return -1


def filter_positives(numeros):
    positivos = ()
    for numero in numeros:
        if numero > 0:
            positivos += (numero,)
    return positivos