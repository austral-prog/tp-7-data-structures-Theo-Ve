# Ejercicios de diccionarios: sistema de inventario


def create_inventory(items):
    inventario = {}
    for item in items:
        if item in inventario:
            inventario[item] += 1
        else:
            inventario[item] = 1
    return inventario


def add_items(inventario, items):
    for item in items:
        if item in inventario:
            inventario[item] += 1
        else:
            inventario[item] = 1
    return inventario

def decrement_items(inventario, items):
    for item in items:
        if item in inventario:
            inventario[item] = max(0, inventario[item] - 1)
    return inventario

def remove_item(inventario, item):
    if item in inventario:
        del inventario[item]
    return inventario

def list_inventory(inventario):
    disponibles = []
    for item in inventario:
        if inventario[item] > 0:
            disponibles.append((item, inventario[item]))
    return disponibles


def find_max_value(diccionario):
    if not diccionario:
        return ""
    mejor_nombre = ""
    mejor_puntaje = -1
    for nombre in diccionario:
        if diccionario[nombre] > mejor_puntaje:
            mejor_puntaje = diccionario[nombre]
            mejor_nombre = nombre
    return mejor_nombre


def reverse_dict(diccionario):
        invertido = {}
        for clave in diccionario:
            valor = diccionario[clave]
            if valor in invertido:
                invertido[valor] += clave
            else:
                invertido[valor] = clave
        return invertido


def word_frequency(palabras):
    """
    Cuenta cuántas veces aparece cada palabra en la lista y lo retorna
    como un diccionario {palabra: cantidad}.

    Args:
        palabras: Lista de palabras (strings). También debe soportar
                  un string vacío retornando un diccionario vacío.

    Returns:
        Diccionario con la frecuencia de cada palabra

    Ejemplo:
        word_frequency(["apple", "banana", "apple", "orange", "banana", "apple"])
        -> {'apple': 3, 'banana': 2, 'orange': 1}
    """
    if not palabras:
        return {}
    lista = {}
    for palabra in palabras:
        if palabra in lista:
            lista[palabra] += 1
        else:
            lista[palabra] = 1
    return lista


def find_biggest_expense(gastos):
    if not gastos:
        return ""
    mejor_categoria = ""
    mejor_promedio = -1
    for categoria in gastos:
        lista = gastos[categoria]
        total = 0
        for gasto in lista:
            total += gasto
        promedio = total / len(lista)
        if promedio > mejor_promedio:
            mejor_promedio = promedio
            mejor_categoria = categoria
    return mejor_categoria


def sum_expenses(gastos):
    if not gastos:
        return {}
    suma = {}
    for categoria in gastos:
        lista = gastos[categoria]
        total = 0
        for gasto in lista:
            total += gasto
        suma[categoria] = total
    return suma



def sum_expenses_by_type(gastos):
    totales = {}
    for categoria in gastos:
        for tipo, monto in gastos[categoria]:
            if tipo in totales:
                totales[tipo] += monto
            else:
                totales[tipo] = monto
    return totales
