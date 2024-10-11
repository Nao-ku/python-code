# Programa para clasificar la edad de una persona

def clasificar_edad(edad):
    # Clasificación basada en la edad
    if edad <= 0:
        print("Edad no válida")
    elif edad <= 5:
        print("Infante")
    elif edad <= 12:
        print("Pre-adolescente")
    elif edad <= 18:
        print("Adulto joven")
    elif edad <= 64:
        print("Adulto")
    else:
        print("Adulto mayor")