class Rectangulo(object):
    def __init__(self, alto, ancho):
        self.alto = alto
        self.ancho = ancho
    def area(self):
        area = self.alto * self.ancho
        return area
    def Perimetro(self):
        Perimetro = (self.alto *2) + (self.ancho *2)
        return Perimetro 


r1=Rectangulo(5 , 7) 
area = r1.area()
perimetro = r1.Perimetro() 

print(" el area del rectangulo es: ", area)
print("el perimetro del rectangulo es ", perimetro)




