#variables
num1 = 2
num2 = 2
#Ol
#AND
print(num1 == num2 and num1 <= num2) # 1 1 - V
print(num1 == num2 and num1 > num2) # 1 0 - F
print(num1 < num2 and num1 > num2) # 0 0 - F
print(num1 < num2 and num1 >= num2) # 0 1 F

# ejemplo 1 
#usuario = input("Digite el usuario: ")
#contraseña = input( "Digite la contraseña: ")
#AND
#print(usuario == "pepitoelpro123" and contraseña == "elmasprosito")

print(num1 == num2 or num1 <= num2) # 1 1 - V
print(num1 <= num2 or num1 > num2) # 1 0 - V
print(num1 > num2 or num1 > num2) # 0 0 - F
print(num1 < num2 or num1 <= num2) # 0 1 - F

#NOT
print( not True) 
print(not False)