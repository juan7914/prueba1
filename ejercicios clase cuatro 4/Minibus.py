class vehiculo ():
    Categoria = "transporte"
    def __init__(self , capacidad):
        self.capacidad = capacidad
        self.pasajeros = []
    def agregar_pasajero(self, nombre):
        if not self.asientos_libres():
            return print("el pasajero no pudo ingresar no quedan asientos disponibles")
        self.pasajeros.append(nombre)  
        return print("el pasajero abordo satisfactoriamente")  
    def asientos_libres(self):
        return self.capacidad - len(self.pasajeros)

Minibus=vehiculo(5) 
lista_pasajeros=["Maria", "Juan", "Octavio", "Felipe",  "Camilo", "Roberto", "Jose"] 

n=1
for pasajero in lista_pasajeros:
    print(f"ingreso pasajero numero{n}")
    print(Minibus.agregar_pasajero(pasajero))
    n=n+1

print(f"ingresaron al minibus los pasajeros{Minibus.pasajeros}")    


         
