import sys

try:
    numero1 = int(input("ingrese un numero: " "  " ))
    numero2 = int(input("ingrese otro numero: " " " ))

except ValueError:
    print("Error. valor no valido")
    sys.exit(1)
    
try:
     resultado = numero1 / numero2 
except ZeroDivisionError:
    print("ningun numero se puede dividir en cero")
    sys.exit(1)  
else :
    print("la divicion salio bien")    
    print(f"{numero1}, entre {numero2} es igual a: {resultado}")

