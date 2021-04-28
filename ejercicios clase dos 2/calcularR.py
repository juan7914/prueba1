import math
radio_circulo = float(input("ingrese numero del radio  "))
if (radio_circulo < 0):
    print("el numero que ingresaste es negativo, el numero debe ser positivo")
else:
    AreaCirculo = math.pi * radio_circulo**2
    print("el area de este circulo es: ",round(AreaCirculo,2))


