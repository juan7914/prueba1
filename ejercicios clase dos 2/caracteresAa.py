print("programa que calcula la longitud de la cadena de texto y las veces que aparece la letra a")
cadena = input("ingresa tu cadena de texto o frace " )
largoCadena = len(cadena)
contarA= cadena.upper().count("A")
print("la longitud de tu cadena de texto es {}, y aparece la letra A en tu cadena {} veces.".format(largoCadena,contarA))
