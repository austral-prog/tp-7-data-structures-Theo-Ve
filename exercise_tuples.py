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
    """
    Recorre una tupla de números y retorna la suma total.
    Si la tupla está vacía, retorna 0.

    No se permite usar la función built-in sum(). Implementar la suma
    recorriendo la tupla con un for (o while).

    Args:
        numeros: Tupla de números (enteros o flotantes)

    Returns:
        La suma de todos los elementos de la tupla

    Ejemplo:
        sum_tuple((1, 2, 3, 4, 5)) -> 15
        sum_tuple(()) -> 0
    """

    if len(numeros) == 0:
        return 0
    else:
        total = 0
        for numero in numeros:
            total += numero
        return total


def count_occurrences(tupla, elemento):
    """
    Recorre la tupla y cuenta cuántas veces aparece el elemento.

    No se permite usar el método .count(). Implementar el conteo
    recorriendo la tupla con un for (o while).

    Args:
        tupla: Tupla con elementos de cualquier tipo
        elemento: El elemento a contar

    Returns:
        La cantidad de veces que aparece el elemento (int)

    Ejemplo:
        count_occurrences((1, 2, 2, 3, 2), 2) -> 3
        count_occurrences(('a', 'b', 'a'), 'c') -> 0
    """

    contador = 0
    for item in tupla:
        if item == elemento:
            contador += 1
    return contador

def find_index(tupla, elemento):
    for indice, item in enumerate(tupla):
        if item == elemento:
            return indice
    return 0


def filter_positives(numeros):
    positivos = ()
    for numero in numeros:
        if numero > 0:
            positivos += (numero,)
    return positivos