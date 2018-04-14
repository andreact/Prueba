from Modelo.clsVariable import Variable
from Modelo.clsAutomata import Automata
from Modelo.clsEstado import Estado

class Gramatica:
    def __init__(self):
        self.variables={}#clave: nombre variable y valor: objeto variable
        self.terminales=[]#Strings
        self.valInicial=''#variable inicial (String)

    def agregarVariable(self, nombre):
        if nombre not in self.variables:
            variable_nuv= Variable(nombre, False)
            self.variables[variable_nuv.nombre]=variable_nuv

    def gramaticaDeAutomata(self,automata,tipo, contador):#tipo se refiere a derecha o izquierda
        #Se renombra el automata
        if contador<=1:
            automata.renombrarEstados()

        for estado in automata.estados.values():
            self.agregarVariable(estado.nombre)
            if estado.esInicial:
                self.variables[estado.nombre].esInicial=True
                self.valInicial=estado.nombre
            #Transiciones
            for k,v in estado.transiciones.items():
                if k not in self.terminales:
                    self.terminales.append(k)
                produccion=[]
                for destino in v:
                    if tipo=='derecha':
                        produccion=[k,destino.nombre]
                    elif tipo=='izquierda':
                        produccion=[destino.nombre,k]
                    else:
                        produccion=[]
                    self.variables[estado.nombre].agregarProduccion(produccion)

            if estado.esAceptador:
                self.variables[estado.nombre].agregarProduccion(['λ'])#si la variable corresponde a un estado aceptador, se agrega la produccion lambda