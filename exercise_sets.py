# Ejercicios de sets: catering del club de cocina

ALCOHOLS = {
    "whiskey", "whisky", "white rum", "dark rum", "bourbon", "rye", "scotch",
    "vodka", "tequila", "gin", "dry vermouth", "sweet vermouth", "prosecco",
    "aperol", "brandy", "mezcal", "triple sec", "coffee liqueur",
    "almond liqueur", "champagne", "orange curacao", "rum"
}


def clean_ingredients(nombre_plato, ingredientes):
    conjunto = set(ingredientes)
    return (nombre_plato, conjunto)

def check_drinks(nombre_bebida, ingredientes):
    for ingredient in ingredientes:
        if ingredient in ALCOHOLS:
            return f"{nombre_bebida} Cocktail"
    return f"{nombre_bebida} Mocktail"


def unique_chars(texto):
    conjunto = set()
    for letra in texto:
        conjunto.add(letra)
    return conjunto

def sum_set(numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma

def common_elements(set_a, set_b):
    comunes = set()
    for elemento in set_a:
        if elemento in set_b:
            comunes.add(elemento)
    return comunes

print(common_elements({1, 2}, {3, 4}))
