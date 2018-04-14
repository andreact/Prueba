class Variable:
    def __init__(self, nombre, esInicial):
        self.nombre= nombre
        self.producciones={}#clave:numero, valor:lista donde se guarda cada elemento de una produccion
        self.esInicial=esInicial #Booleano

    def agregarProduccion(self, produccion):#la produccion debe ser una lista
        cantidad=len(self.producciones)

        if produccion not in self.producciones.values():
            self.producciones[cantidad+1]=produccion