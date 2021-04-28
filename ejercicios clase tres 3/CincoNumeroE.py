print("ingrese 5 numeros que sean enteros:")
try :
    numero1 = int(input("ingrese primer numero entero "))
    numero2 = int(input("ingrese segundo numero entero "))
    numero3 = int(input("ingrese tercero numero entero "))
    numero4 = int(input("ingrese cuarto numero entero "))
    numero5 = int(input("ingrese quinto numero entero "))
except : 
    print("numero no es entero")
lista = [numero1, numero2, numero3, numero4, numero5]
print(lista)