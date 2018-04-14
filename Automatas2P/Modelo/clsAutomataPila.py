from Modelo.clsAutomata import Automata
from Modelo.clsEstadoAP import EstadoAP

class AutomataPila(Automata):
    def __init__(self):
        Automata.__init__(self)
        self.alfabetoPila=[]
        self.simboloIniPila=""#simbolo inicial de la pila

    def agregarEstadoAP(self):
        cantidad = len(self.estados)
        nuevoEstado = EstadoAP('q' + str(cantidad), False, False)

        self.estados[nuevoEstado.nombre] = nuevoEstado
        return nuevoEstado