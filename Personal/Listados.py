#Crear una lista
lista = [90, "a", "Sunday",True,4.5]
print(f"Los datos de la lista son: {lista}")
#Datos en una lista
print(lista[2])
print(lista[4])
print(lista[-4])
print(lista[-3])
print(lista[-2])
print(lista[-1:])
#Recorrer una lista
numeros = [1,5]
numeros.append(100)
numeros.append("kevincandela124@unisangil.edu.co")
print(numeros)
#Tamaño llista
longitud = numeros.__len__()
print(f"El tamaño de la lista es {longitud}")
#Insert
numeros.insert(2, "Kevin")
print(numeros)
numeros.insert(1,"r")
print(numeros)
numeros.insert(5, "1053326735")
print(numeros)
numeros.insert(3, "cumpleaños:11")
print(numeros)
numeros.insert(5, "Naciminento: 07")
print(numeros)
#Reemplaar datos de una lista
numeros[-1] = "Kevadriespgmail.com"
print(numeros)
numeros[-3] = 80
print (numeros)
numeros[-5] = "Kevin Adrian"
print(numeros)
numeros[-6] = "12"
print(numeros)
#Eliminar datos
numeros.remove(80)
print(numeros)
numeros.pop()
print(numeros)
numeros[2:8] = []
print(numeros)
#Recorrer lista
for i in lista:
    print(f"Datos lista: {i}")
    #Invertir lista
lista.reverse()
print(lista)
#Ordenar datos de una lista
lista_2 = [10, 2, 4, 5, 7 , 8, 3,]
print(sorted(lista_2))
print(lista_2.sort(reverse= True))
print(lista_2)
lista_2[:]

promedio = 37/7
print(promedio)