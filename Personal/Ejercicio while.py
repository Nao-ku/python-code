#estructura de repeticion
Opcion = input("Digite la opcion del menu: ")
resultado = 1+2
while Opcion != "salir":
    if Opcion == "1": 
        print(f"suma = (resultado)")
    elif Opcion == "2" :
        print (f"resta = ", 3-4)
    elif Opcion == "3":
        print (f"multiplicacion =" , 3*4)
    elif Opcion == "4":
        print ("div=", 3/4)
    elif Opcion == "5":
        print ("potenciacion", 3**4)
    