"""2) Módulo masa.py: Este módulo debe contener funciones para convertir entre diferentes unidades de masa, como kilogramos, libras y onzas.(0.5 puntos) """

def Kilogramos_a_Gramos(kg):
    g = kg * 1000
    return g

def Kilogramos_a_Toneladas(kg):
    t = kg / 1000
    return t

def Gramos_a_Kilogramos(g):
    kg = g / 1000
    return kg

def Gramos_a_Toneladas(g):
    t = g / 1000000
    return t

def Toneladas_a_Kilogramos(t):
    kg = t * 1000
    return kg

def Toneladas_a_Gramos(t):
    g = t * 1000000
    return g