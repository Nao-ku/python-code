# Función para calcular el promedio de las notas
def calcular_promedio():
    # Mensaje de bienvenida
    print("Bienvenido a la calculadora de promedio de notas.")

    # Pedir al usuario cuántas notas quiere ingresar
    cantidad_notas = int(input("¿Cuántas notas deseas ingresar?: "))

    # Lista para almacenar las notas
    notas = []

    # Bucle para ingresar las notas una por una
    for i in range(cantidad_notas):
        while True:
            try:
                # Pedir al usuario que ingrese cada nota
                nota = float(input(f"Ingrese la nota {i+1}: "))
                # Validar que la nota esté entre 0 y 5
                if nota < 0 or nota > 5:
                    print("La nota debe estar entre 0 y 5. Inténtalo de nuevo.")
                else:
                    # Agregar la nota a la lista
                    notas.append(nota)
                    break
            except ValueError:
                print("Por favor, ingresa un número válido.")

    # Calcular el promedio
    promedio = sum(notas) / cantidad_notas

    # Mostrar el promedio
    print(f"El promedio de las notas ingresadas es: {promedio:.2f}")

# Ejecutar la función
calcular_promedio()