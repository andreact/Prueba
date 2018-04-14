class EstadoAP:
    def __init__(self, nombre, inicial, aceptador):
        self.nombre= nombre
        self.esInicial= inicial
        self.esAceptador= aceptador
        self.transiciones = {}
        ''' la clave es un string que contiene simbolo de la cadena y el simbolo de la pila (leido) separados por coma, el valor es una lista de
        listas que tiene el estado destino(objeto) y el simbolo que se escribe en la pila. Es una lista de listas por si se trata
        de un automata a pila no determinista'''

    def agregarTransicion(self, comp1,comp2):#comp1=simbolo cadena,simbolo pila, comp2= [nuevo estado, simbolo a escribir en pila]
        if comp1 not in self.transiciones:
            self.transiciones[comp1]=[comp2]

        else:
            self.transiciones[comp1].append(comp2)


