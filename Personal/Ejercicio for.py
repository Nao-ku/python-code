#Estructura de repeticion FOR 
for i in range (2): #Comienza desde 0
    print(f"su dato es {i}")

    #Estructura de repeticion FOR 
for i in range (20,101): #Comienza inicio, fin -1
    print(f"su dato es {i}")

        #Estructura de repeticion FOR 
for i in range (1,10,2): #Comienza inicio, fin -1,  incremento 
    print(f"su dato es {i}")

    #Estructura de repeticion FOR 
    for letra in "Python":
        print(letra)

 #ejemplo 1
cadena = "Programacion"
for letra in cadena:
        if letra == "r":
         print("se encontro una  r")
         break
else:
         print("Letra no encontrada")
print("esta fuera del ciclo for")

#Ejemplo
mul = int(input("Digite la tabla de multiplicar que desea:"))
for i in range (1,12):
     print  (f"2 X {i} = {i*2}")

