class Estado:
    def __init__(self,nombre,posX,posY,esIncial,esAceptador):
        self.nombre=nombre
        self.posX=posX #posicion grafica
        self.posY=posY
        self.claveGraficos=None#clave para acceder al circulo grafico
        self.transiciones={}#{valor(clave),lista[estados]} #se guardan los estados, no los nombres
        self.esInicial=esIncial#booleano
        self.esAceptador=esAceptador #booleano

    def agregarTransicion(self,valor,estDestino):
        if valor in self.transiciones:
            self.transiciones[valor].append(estDestino)

        else:
            self.transiciones[valor]=[]
            self.transiciones[valor].append(estDestino)
