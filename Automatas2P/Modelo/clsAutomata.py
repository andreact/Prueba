from Modelo.clsEstado import Estado

class Automata:
    def __init__(self):
        self.estados = {}  # {nombreEstado(clave),estado}
        self.alfabeto = []
        self.estadoIni = ""  # nombre
        self.estAceptadores = []  # nombre


    def agregarEstado(self, posX, posY):  # se agrega un estado generado graficamente
        cantidad = len(self.estados)
        nuevoEstado = Estado('q' + str(cantidad), posX, posY, False,False)  # Por defecto se coloca falso a los atributos de si es inicial o aceptador, pero luego se cambiara de acuerdo a lo que indique el usuario

        self.estados[nuevoEstado.nombre] = nuevoEstado
        return nuevoEstado

    
    def renombrarEstados(self):
	hola = ""
        nuevoDic = {}
        abecedario=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','T','U','V','W','X','Y','Z']
        for i in range(0,len(self.estados)):
            if self.estados["q"+str(i)].esInicial:
                self.estados["q"+str(i)].nombre="S" #Se le cambia el nombre al estado inicial
                self.estadoIni="S"

                if self.estados["q"+str(i)].esAceptador:
                    pos = self.estAceptadores.index("q" + str(i))
                    self.estAceptadores[pos] = "S"
                # Se agrega al nuevo diccionario
                nuevoDic["S"] = self.estados["q"+str(i)]
            else:
                if self.estados["q"+str(i)].esAceptador: #Se revisa si es aceptador
                    pos = self.estAceptadores.index("q"+str(i))
                    self.estAceptadores[pos] = abecedario[0]

                self.estados["q"+str(i)].nombre=abecedario[0]
                # Se agrega al nuevo diccionario
                nuevoDic[abecedario[0]] = self.estados["q"+str(i)]
                del(abecedario[0])

        self.estados=nuevoDic


























































