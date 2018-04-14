#Parte Grafica
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QGraphicsView,QMessageBox,QGraphicsEllipseItem,QGraphicsTextItem,QGraphicsScene,QGraphicsLineItem,QTableWidget,QTableWidgetItem,QFileDialog
from PyQt5.QtCore import QPointF, Qt,QRectF
from PyQt5.QtGui import QPen,QBrush,QColor,QFont, QPainterPath

#Modelo
from Modelo.clsEstado import Estado
from Modelo.clsAutomata import Automata
from Modelo.clsGramatica import Gramatica
from Modelo.clsVariable import Variable
from Modelo.clsAutomataPila import AutomataPila
from Modelo.clsEstadoAP import EstadoAP

#Otros
import random
import pickle

class VentanaP(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.retranslateUi(self)
        self.crearEscenas()
        self.automata = Automata()  # Automata actual
        self.automataP= AutomataPila()
        self.estadosTotales = 0  # contador de todos los estados que se crean en el editor, el cual sera la clave para acceder a ellos graficamente
        self.elemGraficos = {}  # diccionario donde se guardan todos los elementos graficos de los ESTADOS
        self.gramatica1=Gramatica()
        self.gramatica2 = Gramatica()
        self.gramatica3 = Gramatica()

        self.contador=0 #cantidad de veces que se llama al método automataGramatica

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(857, 721)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pestanas = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pestanas.sizePolicy().hasHeightForWidth())
        self.pestanas.setSizePolicy(sizePolicy)
        self.pestanas.setObjectName("pestanas")

        #Regex
        self.regex = QtWidgets.QWidget()
        self.regex.setObjectName("regex")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.regex)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.expRegular1Txt = QtWidgets.QLineEdit(self.regex)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.expRegular1Txt.sizePolicy().hasHeightForWidth())
        self.expRegular1Txt.setSizePolicy(sizePolicy)
        self.expRegular1Txt.setObjectName("expRegular1Txt")
        self.gridLayout_4.addWidget(self.expRegular1Txt, 1, 3, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.regex)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_11.setFont(font)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 1, 2, 1, 1)
        self.ok1Btn = QtWidgets.QPushButton(self.regex)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ok1Btn.sizePolicy().hasHeightForWidth())
        self.ok1Btn.setSizePolicy(sizePolicy)
        self.ok1Btn.setObjectName("ok1Btn")
        self.gridLayout_4.addWidget(self.ok1Btn, 2, 3, 1, 1)
        self.limpiar1Btn = QtWidgets.QPushButton(self.regex)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.limpiar1Btn.sizePolicy().hasHeightForWidth())
        self.limpiar1Btn.setSizePolicy(sizePolicy)
        self.limpiar1Btn.setObjectName("limpiar1Btn")
        self.gridLayout_4.addWidget(self.limpiar1Btn, 2, 4, 1, 1)
        self.campoTexto1 = QtWidgets.QTextEdit(self.regex)
        self.campoTexto1.setObjectName("campoTexto1")
        self.gridLayout_4.addWidget(self.campoTexto1, 1, 0, 3, 2)
        self.pestanas.addTab(self.regex, "")


        #Gramatica de autómata
        self.gramatica = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gramatica.sizePolicy().hasHeightForWidth())
        self.gramatica.setSizePolicy(sizePolicy)
        self.gramatica.setObjectName("gramatica")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gramatica)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.estInicialLbl = QtWidgets.QLabel(self.gramatica)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.estInicialLbl.sizePolicy().hasHeightForWidth())
        self.estInicialLbl.setSizePolicy(sizePolicy)
        self.estInicialLbl.setObjectName("estInicialLbl")
        self.gridLayout_2.addWidget(self.estInicialLbl, 4, 11, 1, 1)
        self.alfabetoLbl = QtWidgets.QLabel(self.gramatica)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.alfabetoLbl.sizePolicy().hasHeightForWidth())
        self.alfabetoLbl.setSizePolicy(sizePolicy)
        self.alfabetoLbl.setObjectName("alfabetoLbl")
        self.gridLayout_2.addWidget(self.alfabetoLbl, 3, 11, 1, 1)
        self.estInicial2Txt = QtWidgets.QLineEdit(self.gramatica)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.estInicial2Txt.sizePolicy().hasHeightForWidth())
        self.estInicial2Txt.setSizePolicy(sizePolicy)
        self.estInicial2Txt.setObjectName("estInicial2Txt")
        self.gridLayout_2.addWidget(self.estInicial2Txt, 4, 12, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gramatica)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 2, 11, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gramatica)
        self.label_4.setMinimumSize(QtCore.QSize(110, 29))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 22, 0, 1, 1)
        self.checkBoxDerecha2 = QtWidgets.QCheckBox(self.gramatica)
        font = QtGui.QFont()
        font.setItalic(True)
        self.checkBoxDerecha2.setFont(font)
        self.checkBoxDerecha2.setObjectName("checkBoxDerecha2")
        self.gridLayout_2.addWidget(self.checkBoxDerecha2, 18, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gramatica)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 24, 8, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gramatica)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 24, 0, 1, 1)
        self.alfabeto2Txt = QtWidgets.QLineEdit(self.gramatica)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.alfabeto2Txt.sizePolicy().hasHeightForWidth())
        self.alfabeto2Txt.setSizePolicy(sizePolicy)
        self.alfabeto2Txt.setObjectName("alfabeto2Txt")
        self.gridLayout_2.addWidget(self.alfabeto2Txt, 3, 12, 1, 1)
        self.aplicar2Btn = QtWidgets.QPushButton(self.gramatica)
        self.aplicar2Btn.setObjectName("aplicar2Btn")
        self.gridLayout_2.addWidget(self.aplicar2Btn, 6, 12, 1, 1)
        self.estAceptadoresLbl = QtWidgets.QLabel(self.gramatica)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.estAceptadoresLbl.sizePolicy().hasHeightForWidth())
        self.estAceptadoresLbl.setSizePolicy(sizePolicy)
        self.estAceptadoresLbl.setObjectName("estAceptadoresLbl")
        self.gridLayout_2.addWidget(self.estAceptadoresLbl, 5, 11, 1, 1)
        self.estAceptadores2Txt = QtWidgets.QLineEdit(self.gramatica)
        self.estAceptadores2Txt.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.estAceptadores2Txt.sizePolicy().hasHeightForWidth())
        self.estAceptadores2Txt.setSizePolicy(sizePolicy)
        self.estAceptadores2Txt.setObjectName("estAceptadores2Txt")
        self.gridLayout_2.addWidget(self.estAceptadores2Txt, 5, 12, 1, 1)
        self.label = QtWidgets.QLabel(self.gramatica)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 7, 11, 1, 1)
        self.origenLbl = QtWidgets.QLabel(self.gramatica)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.origenLbl.sizePolicy().hasHeightForWidth())
        self.origenLbl.setSizePolicy(sizePolicy)
        self.origenLbl.setObjectName("origenLbl")
        self.gridLayout_2.addWidget(self.origenLbl, 8, 11, 1, 1)
        self.destinoLbl = QtWidgets.QLabel(self.gramatica)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.destinoLbl.sizePolicy().hasHeightForWidth())
        self.destinoLbl.setSizePolicy(sizePolicy)
        self.destinoLbl.setObjectName("destinoLbl")
        self.gridLayout_2.addWidget(self.destinoLbl, 9, 11, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.gramatica)
        self.label_23.setObjectName("label_23")
        self.gridLayout_2.addWidget(self.label_23, 24, 3, 1, 1)
        self.origen2Txt = QtWidgets.QLineEdit(self.gramatica)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.origen2Txt.sizePolicy().hasHeightForWidth())
        self.origen2Txt.setSizePolicy(sizePolicy)
        self.origen2Txt.setObjectName("origen2Txt_4")
        self.gridLayout_2.addWidget(self.origen2Txt, 8, 12, 1, 1)
        self.destino2Txt = QtWidgets.QLineEdit(self.gramatica)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.destino2Txt.sizePolicy().hasHeightForWidth())
        self.destino2Txt.setSizePolicy(sizePolicy)
        self.destino2Txt.setObjectName("destino2Txt_2")
        self.gridLayout_2.addWidget(self.destino2Txt, 9, 12, 1, 1)
        self.guardarAut2 = QtWidgets.QPushButton(self.gramatica)
        self.guardarAut2.setObjectName("guardarAut2")
        self.gridLayout_2.addWidget(self.guardarAut2, 13, 12, 1, 1)
        self.valorLbl = QtWidgets.QLabel(self.gramatica)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.valorLbl.sizePolicy().hasHeightForWidth())
        self.valorLbl.setSizePolicy(sizePolicy)
        self.valorLbl.setObjectName("valorLbl")
        self.gridLayout_2.addWidget(self.valorLbl, 10, 11, 1, 1)
        self.valor2Txt = QtWidgets.QLineEdit(self.gramatica)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.valor2Txt.sizePolicy().hasHeightForWidth())
        self.valor2Txt.setSizePolicy(sizePolicy)
        self.valor2Txt.setObjectName("valor2Txt")
        self.gridLayout_2.addWidget(self.valor2Txt, 10, 12, 1, 1)
        self.aplicarTransiBtn = QtWidgets.QPushButton(self.gramatica)
        self.aplicarTransiBtn.setObjectName("aplicarTransiBtn")
        self.gridLayout_2.addWidget(self.aplicarTransiBtn, 11, 12, 1, 1)

        self.guardar_gram2 = QtWidgets.QPushButton(self.gramatica)
        self.guardar_gram2.setObjectName("guardar_gram2")
        self.gridLayout_2.addWidget(self.guardar_gram2, 14, 12, 1, 1)
        self.checkBoxIzquierda2 = QtWidgets.QCheckBox(self.gramatica)
        font = QtGui.QFont()
        font.setItalic(True)
        self.checkBoxIzquierda2.setFont(font)
        self.checkBoxIzquierda2.setObjectName("checkBoxIzquierda2")
        self.gridLayout_2.addWidget(self.checkBoxIzquierda2, 18, 11, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gramatica)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 16, 0, 1, 8)
        self.label_24 = QtWidgets.QLabel(self.gramatica)
        self.label_24.setObjectName("label_24")
        self.gridLayout_2.addWidget(self.label_24, 24, 12, 1, 1)
        self.comboBoxProducc2 = QtWidgets.QComboBox(self.gramatica)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxProducc2.sizePolicy().hasHeightForWidth())
        self.comboBoxProducc2.setSizePolicy(sizePolicy)
        self.comboBoxProducc2.setObjectName("comboBoxProducc2")
        self.gridLayout_2.addWidget(self.comboBoxProducc2, 24, 11, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gramatica)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 22, 8, 1, 1)
        self.vInicialTxt = QtWidgets.QLineEdit(self.gramatica)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vInicialTxt.sizePolicy().hasHeightForWidth())
        self.vInicialTxt.setSizePolicy(sizePolicy)
        self.vInicialTxt.setObjectName("vInicialTxt")
        self.gridLayout_2.addWidget(self.vInicialTxt, 22, 11, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.gramatica)
        self.label_22.setObjectName("label_22")
        self.gridLayout_2.addWidget(self.label_22, 22, 3, 1, 1)
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.gramatica)
        self.graphicsView_2.setObjectName("graphicsView_4")
        self.gridLayout_2.addWidget(self.graphicsView_2, 2, 0, 14, 9)
        self.combovariables2 = QtWidgets.QComboBox(self.gramatica)
        self.combovariables2.setObjectName("combovariables2")
        self.gridLayout_2.addWidget(self.combovariables2, 22, 1, 1, 2)
        self.comboBoxTermin2 = QtWidgets.QComboBox(self.gramatica)
        self.comboBoxTermin2.setObjectName("comboBoxTermin2")
        self.gridLayout_2.addWidget(self.comboBoxTermin2, 24, 1, 1, 2)
        self.limpiar2Btn = QtWidgets.QPushButton(self.gramatica)
        self.limpiar2Btn.setObjectName("limpiar2_1Btn")
        self.gridLayout_2.addWidget(self.limpiar2Btn, 15, 12, 1, 1)
        self.generarG2Btn = QtWidgets.QPushButton(self.gramatica)
        self.generarG2Btn.setObjectName("limpiar2_2Btn")
        self.gridLayout_2.addWidget(self.generarG2Btn, 23, 12, 1, 1)
        self.pestanas.addTab(self.gramatica, "")

        #Arbol derivacion
        self.arbolDerivacion = QtWidgets.QWidget()
        self.arbolDerivacion.setObjectName("arbolDerivacion")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.arbolDerivacion)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_15 = QtWidgets.QLabel(self.arbolDerivacion)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout_10.addWidget(self.label_15, 2, 3, 1, 1)
        self.guardar_gram3Btn = QtWidgets.QPushButton(self.arbolDerivacion)
        self.guardar_gram3Btn.setObjectName("guardar_gram3Btn")
        self.gridLayout_10.addWidget(self.guardar_gram3Btn, 5, 4, 1, 1)
        self.variables3Txt = QtWidgets.QLineEdit(self.arbolDerivacion)
        self.variables3Txt.setObjectName("variables3Txt")
        self.gridLayout_10.addWidget(self.variables3Txt, 2, 1, 1, 1)
        self.ok3_1Btn = QtWidgets.QPushButton(self.arbolDerivacion)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ok3_1Btn.sizePolicy().hasHeightForWidth())
        self.ok3_1Btn.setSizePolicy(sizePolicy)
        self.ok3_1Btn.setObjectName("ok3_1Btn")
        self.gridLayout_10.addWidget(self.ok3_1Btn, 2, 4, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.arbolDerivacion)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout_10.addWidget(self.label_13, 2, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.arbolDerivacion)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout_10.addWidget(self.label_12, 1, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.arbolDerivacion)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout_10.addWidget(self.label_14, 4, 0, 1, 1)
        self.vInicial3Txt = QtWidgets.QLineEdit(self.arbolDerivacion)
        self.vInicial3Txt.setObjectName("vInicial3Txt")
        self.gridLayout_10.addWidget(self.vInicial3Txt, 4, 1, 1, 1)
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.arbolDerivacion)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.gridLayout_10.addWidget(self.graphicsView_3, 11, 0, 1, 7)
        self.ok3_3Btn = QtWidgets.QPushButton(self.arbolDerivacion)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ok3_3Btn.sizePolicy().hasHeightForWidth())
        self.ok3_3Btn.setSizePolicy(sizePolicy)
        self.ok3_3Btn.setObjectName("ok3_3Btn")
        self.gridLayout_10.addWidget(self.ok3_3Btn, 4, 4, 1, 1)
        self.ok3_2Btn = QtWidgets.QPushButton(self.arbolDerivacion)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ok3_2Btn.sizePolicy().hasHeightForWidth())
        self.ok3_2Btn.setSizePolicy(sizePolicy)
        self.ok3_2Btn.setObjectName("ok3_2Btn")
        self.gridLayout_10.addWidget(self.ok3_2Btn, 2, 9, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.arbolDerivacion)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.gridLayout_10.addWidget(self.label_16, 2, 5, 1, 1)
        self.terminales3Txt = QtWidgets.QLineEdit(self.arbolDerivacion)
        self.terminales3Txt.setObjectName("terminales3Txt")
        self.gridLayout_10.addWidget(self.terminales3Txt, 2, 6, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.arbolDerivacion)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gridLayout_10.addWidget(self.label_17, 2, 7, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.arbolDerivacion)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.gridLayout_10.addWidget(self.label_18, 4, 5, 1, 1)
        self.comboBoxProducc3 = QtWidgets.QComboBox(self.arbolDerivacion)
        self.comboBoxProducc3.setObjectName("comboBoxProducc3")
        self.gridLayout_10.addWidget(self.comboBoxProducc3, 4, 6, 1, 1)
        self.agregarProd3Btn = QtWidgets.QPushButton(self.arbolDerivacion)
        self.agregarProd3Btn.setObjectName("agregarProd3Btn")
        self.gridLayout_10.addWidget(self.agregarProd3Btn, 4, 9, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.arbolDerivacion)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.gridLayout_10.addWidget(self.label_19, 4, 7, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.arbolDerivacion)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.gridLayout_10.addWidget(self.label_20, 7, 0, 1, 1)
        self.cadena3Txt = QtWidgets.QLineEdit(self.arbolDerivacion)
        self.cadena3Txt.setObjectName("cadena3Txt")
        self.gridLayout_10.addWidget(self.cadena3Txt, 7, 1, 1, 1)
        self.checkBoxDerecha3 = QtWidgets.QCheckBox(self.arbolDerivacion)
        font = QtGui.QFont()
        font.setItalic(True)
        self.checkBoxDerecha3.setFont(font)
        self.checkBoxDerecha3.setObjectName("checkBoxDerecha3")
        self.gridLayout_10.addWidget(self.checkBoxDerecha3, 7, 9, 1, 1)
        self.generar3Btn = QtWidgets.QPushButton(self.arbolDerivacion)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generar3Btn.sizePolicy().hasHeightForWidth())
        self.generar3Btn.setSizePolicy(sizePolicy)
        self.generar3Btn.setObjectName("generar3Btn")
        self.gridLayout_10.addWidget(self.generar3Btn, 11, 9, 1, 1)
        self.checkBoxIzquierda3 = QtWidgets.QCheckBox(self.arbolDerivacion)
        font = QtGui.QFont()
        font.setItalic(True)
        self.checkBoxIzquierda3.setFont(font)
        self.checkBoxIzquierda3.setObjectName("checkBoxIzquierda3")
        self.gridLayout_10.addWidget(self.checkBoxIzquierda3, 10, 9, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.arbolDerivacion)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.gridLayout_10.addWidget(self.label_21, 6, 9, 1, 1)
        self.limpiar3_1Btn = QtWidgets.QPushButton(self.arbolDerivacion)
        self.limpiar3_1Btn.setObjectName("limpiar3_1Btn")
        self.gridLayout_10.addWidget(self.limpiar3_1Btn, 6, 4, 1, 1)
        self.limpiar3_2Btn = QtWidgets.QPushButton(self.arbolDerivacion)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.limpiar3_2Btn.sizePolicy().hasHeightForWidth())
        self.limpiar3_2Btn.setSizePolicy(sizePolicy)
        self.limpiar3_2Btn.setObjectName("limpiar3_2Btn")
        self.gridLayout_10.addWidget(self.limpiar3_2Btn, 12, 9, 1, 1)
        self.pestanas.addTab(self.arbolDerivacion, "")

        #Automata a pila
        self.automataPila = QtWidgets.QWidget()
        self.automataPila.setObjectName("automataPila")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.automataPila)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame = QtWidgets.QFrame(self.automataPila)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.maquinaLbl = QtWidgets.QLabel(self.frame)
        self.maquinaLbl.setGeometry(QtCore.QRect(0, 180, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.maquinaLbl.setFont(font)
        self.maquinaLbl.setObjectName("maquinaLbl")
        self.cBoxEstados4 = QtWidgets.QComboBox(self.frame)
        self.cBoxEstados4.setGeometry(QtCore.QRect(50, 190, 91, 21))
        self.cBoxEstados4.setObjectName("cBoxEstados4")
        self.cBoxEstInicial4 = QtWidgets.QComboBox(self.frame)
        self.cBoxEstInicial4.setGeometry(QtCore.QRect(380, 190, 101, 21))
        self.cBoxEstInicial4.setObjectName("cBoxEstInicial4")
        self.cBoxTransiciones4_ = QtWidgets.QComboBox(self.frame)
        self.cBoxTransiciones4_.setGeometry(QtCore.QRect(240, 190, 131, 21))
        self.cBoxTransiciones4_.setObjectName("cBoxTransiciones4_")
        self.cBoxAlfabeto4_ = QtWidgets.QComboBox(self.frame)
        self.cBoxAlfabeto4_.setGeometry(QtCore.QRect(150, 190, 81, 21))
        self.cBoxAlfabeto4_.setObjectName("cBoxAlfabeto4_")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(830, 180, 16, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.QLbl = QtWidgets.QLabel(self.frame)
        self.QLbl.setGeometry(QtCore.QRect(90, 160, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.QLbl.setFont(font)
        self.QLbl.setObjectName("QLbl")
        self.inicial2Lbl = QtWidgets.QLabel(self.frame)
        self.inicial2Lbl.setGeometry(QtCore.QRect(410, 160, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.inicial2Lbl.setFont(font)
        self.inicial2Lbl.setObjectName("inicial2Lbl")
        self.aceptadores2Lbl = QtWidgets.QLabel(self.frame)
        self.aceptadores2Lbl.setGeometry(QtCore.QRect(520, 170, 31, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.aceptadores2Lbl.setFont(font)
        self.aceptadores2Lbl.setObjectName("aceptadores2Lbl")
        self.alfabeto2Lbl = QtWidgets.QLabel(self.frame)
        self.alfabeto2Lbl.setGeometry(QtCore.QRect(180, 160, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.alfabeto2Lbl.setFont(font)
        self.alfabeto2Lbl.setObjectName("alfabeto2Lbl")
        self.transiLbl = QtWidgets.QLabel(self.frame)
        self.transiLbl.setGeometry(QtCore.QRect(300, 160, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.transiLbl.setFont(font)
        self.transiLbl.setObjectName("transiLbl")
        self.checkBoxInicial4 = QtWidgets.QCheckBox(self.frame)
        self.checkBoxInicial4.setGeometry(QtCore.QRect(10, 50, 98, 21))
        self.checkBoxInicial4.setObjectName("checkBoxInicial4")
        self.checkBoxAceptador4 = QtWidgets.QCheckBox(self.frame)
        self.checkBoxAceptador4.setGeometry(QtCore.QRect(120, 50, 98, 21))
        self.checkBoxAceptador4.setObjectName("checkBoxAceptador4")
        self.anadirEstado4Btn = QtWidgets.QPushButton(self.frame)
        self.anadirEstado4Btn.setGeometry(QtCore.QRect(260, 50, 111, 29))
        self.anadirEstado4Btn.setObjectName("anadirEstado4Btn")
        self.origen4Txt = QtWidgets.QLineEdit(self.frame)
        self.origen4Txt.setGeometry(QtCore.QRect(10, 130, 71, 21))
        self.origen4Txt.setObjectName("origen4Txt")
        self.origenLbl_2 = QtWidgets.QLabel(self.frame)
        self.origenLbl_2.setGeometry(QtCore.QRect(20, 100, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.origenLbl_2.setFont(font)
        self.origenLbl_2.setObjectName("origenLbl_2")
        self.transi4Btn = QtWidgets.QPushButton(self.frame)
        self.transi4Btn.setGeometry(QtCore.QRect(580, 120, 141, 29))
        self.transi4Btn.setObjectName("transi4Btn")
        self.alfabeto2Lbl_2 = QtWidgets.QLabel(self.frame)
        self.alfabeto2Lbl_2.setGeometry(QtCore.QRect(10, 0, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.alfabeto2Lbl_2.setFont(font)
        self.alfabeto2Lbl_2.setObjectName("alfabeto2Lbl_2")
        self.alfabeto4 = QtWidgets.QLineEdit(self.frame)
        self.alfabeto4.setGeometry(QtCore.QRect(50, 10, 181, 21))
        self.alfabeto4.setObjectName("alfabeto4")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(240, 10, 16, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.alfabeto2Lbl_3 = QtWidgets.QLabel(self.frame)
        self.alfabeto2Lbl_3.setGeometry(QtCore.QRect(430, 0, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.alfabeto2Lbl_3.setFont(font)
        self.alfabeto2Lbl_3.setObjectName("alfabeto2Lbl_3")
        self.alfabetoPila4 = QtWidgets.QLineEdit(self.frame)
        self.alfabetoPila4.setGeometry(QtCore.QRect(470, 10, 181, 21))
        self.alfabetoPila4.setObjectName("alfabetoPila4")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(650, 10, 16, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.agregarAlfabeto4 = QtWidgets.QPushButton(self.frame)
        self.agregarAlfabeto4.setGeometry(QtCore.QRect(260, 0, 121, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.agregarAlfabeto4.setFont(font)
        self.agregarAlfabeto4.setObjectName("agregarAlfabeto4")
        self.agregarAPila4 = QtWidgets.QPushButton(self.frame)
        self.agregarAPila4.setGeometry(QtCore.QRect(670, 10, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.agregarAPila4.setFont(font)
        self.agregarAPila4.setObjectName("agregarAPila4")
        self.sEntrada4Txt = QtWidgets.QLineEdit(self.frame)
        self.sEntrada4Txt.setGeometry(QtCore.QRect(110, 130, 91, 21))
        self.sEntrada4Txt.setObjectName("sEntrada4Txt")
        self.origenLbl_3 = QtWidgets.QLabel(self.frame)
        self.origenLbl_3.setGeometry(QtCore.QRect(180, 80, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.origenLbl_3.setFont(font)
        self.origenLbl_3.setObjectName("origenLbl_3")
        self.origenLbl_4 = QtWidgets.QLabel(self.frame)
        self.origenLbl_4.setGeometry(QtCore.QRect(100, 100, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.origenLbl_4.setFont(font)
        self.origenLbl_4.setObjectName("origenLbl_4")
        self.sPila4Txt = QtWidgets.QLineEdit(self.frame)
        self.sPila4Txt.setGeometry(QtCore.QRect(210, 130, 91, 21))
        self.sPila4Txt.setObjectName("sPila4Txt")
        self.origenLbl_5 = QtWidgets.QLabel(self.frame)
        self.origenLbl_5.setGeometry(QtCore.QRect(220, 100, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.origenLbl_5.setFont(font)
        self.origenLbl_5.setObjectName("origenLbl_5")
        self.destino4Txt = QtWidgets.QLineEdit(self.frame)
        self.destino4Txt.setGeometry(QtCore.QRect(330, 130, 91, 21))
        self.destino4Txt.setObjectName("destino4Txt")
        self.origenLbl_6 = QtWidgets.QLabel(self.frame)
        self.origenLbl_6.setGeometry(QtCore.QRect(350, 100, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.origenLbl_6.setFont(font)
        self.origenLbl_6.setObjectName("origenLbl_6")
        self.simboloEscribirP4Txt = QtWidgets.QLineEdit(self.frame)
        self.simboloEscribirP4Txt.setGeometry(QtCore.QRect(450, 130, 91, 21))
        self.simboloEscribirP4Txt.setObjectName("simboloEscribirP4Txt")
        self.origenLbl_7 = QtWidgets.QLabel(self.frame)
        self.origenLbl_7.setGeometry(QtCore.QRect(420, 100, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.origenLbl_7.setFont(font)
        self.origenLbl_7.setObjectName("origenLbl_7")
        self.cBoxAceptadores4 = QtWidgets.QComboBox(self.frame)
        self.cBoxAceptadores4.setGeometry(QtCore.QRect(490, 190, 101, 21))
        self.cBoxAceptadores4.setObjectName("cBoxAceptadores4")
        self.cBoxSimbolosPila4 = QtWidgets.QComboBox(self.frame)
        self.cBoxSimbolosPila4.setGeometry(QtCore.QRect(600, 190, 101, 21))
        self.cBoxSimbolosPila4.setObjectName("cBoxSimbolosPila4")
        self.alfabeto2Lbl_4 = QtWidgets.QLabel(self.frame)
        self.alfabeto2Lbl_4.setGeometry(QtCore.QRect(640, 160, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.alfabeto2Lbl_4.setFont(font)
        self.alfabeto2Lbl_4.setObjectName("alfabeto2Lbl_4")
        self.cBoxSimboloIniP4 = QtWidgets.QComboBox(self.frame)
        self.cBoxSimboloIniP4.setGeometry(QtCore.QRect(710, 190, 81, 21))
        self.cBoxSimboloIniP4.setObjectName("cBoxSimboloIniP4")
        self.alfabeto2Lbl_5 = QtWidgets.QLabel(self.frame)
        self.alfabeto2Lbl_5.setGeometry(QtCore.QRect(750, 160, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.alfabeto2Lbl_5.setFont(font)
        self.alfabeto2Lbl_5.setObjectName("alfabeto2Lbl_5")
        self.maquinaLbl_2 = QtWidgets.QLabel(self.frame)
        self.maquinaLbl_2.setGeometry(QtCore.QRect(560, 360, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.maquinaLbl_2.setFont(font)
        self.maquinaLbl_2.setObjectName("maquinaLbl_2")
        self.cadena4Txt = QtWidgets.QLineEdit(self.frame)
        self.cadena4Txt.setGeometry(QtCore.QRect(630, 370, 181, 21))
        self.cadena4Txt.setObjectName("cadena4Txt")
        self.analizar4Btn = QtWidgets.QPushButton(self.frame)
        self.analizar4Btn.setGeometry(QtCore.QRect(660, 410, 101, 29))
        self.analizar4Btn.setObjectName("analizar4Btn")
        self.maquinaLbl_3 = QtWidgets.QLabel(self.frame)
        self.maquinaLbl_3.setGeometry(QtCore.QRect(560, 470, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.maquinaLbl_3.setFont(font)
        self.maquinaLbl_3.setObjectName("maquinaLbl_3")
        self.estActual4Txt = QtWidgets.QLineEdit(self.frame)
        self.estActual4Txt.setGeometry(QtCore.QRect(690, 480, 81, 21))
        self.estActual4Txt.setObjectName("estActual4Txt")
        self.guardarAut4Btn = QtWidgets.QPushButton(self.frame)
        self.guardarAut4Btn.setGeometry(QtCore.QRect(560, 290, 131, 29))
        self.guardarAut4Btn.setObjectName("guardarAut4Btn")
        self.limpiar4Btn = QtWidgets.QPushButton(self.frame)
        self.limpiar4Btn.setGeometry(QtCore.QRect(710, 290, 101, 29))
        self.limpiar4Btn.setObjectName("limpiar4Btn")
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setGeometry(QtCore.QRect(9, 259, 541, 341))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 539, 339))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents_6)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(-1, 0, 541, 341))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_6)
        self.sigpaso4Btn = QtWidgets.QPushButton(self.frame)
        self.sigpaso4Btn.setGeometry(QtCore.QRect(640, 540, 111, 29))
        self.sigpaso4Btn.setObjectName("sigpaso4Btn")
        self.maquinaLbl_4 = QtWidgets.QLabel(self.frame)
        self.maquinaLbl_4.setGeometry(QtCore.QRect(0, 220, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.maquinaLbl_4.setFont(font)
        self.maquinaLbl_4.setObjectName("maquinaLbl_4")
        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)
        self.pestanas.addTab(self.automataPila, "")

        #Formas Normales
        self.forNormales = QtWidgets.QWidget()
        self.forNormales.setObjectName("forNormales")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.forNormales)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.guardar_gram5Btn = QtWidgets.QPushButton(self.forNormales)
        self.guardar_gram5Btn.setObjectName("guardar_gram5Btn")
        self.gridLayout_5.addWidget(self.guardar_gram5Btn, 7, 2, 1, 1)
        self.chomsky5Btn = QtWidgets.QPushButton(self.forNormales)
        self.chomsky5Btn.setObjectName("chomsky5Btn")
        self.gridLayout_5.addWidget(self.chomsky5Btn, 6, 2, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.forNormales)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.gridLayout_5.addWidget(self.label_33, 6, 0, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.forNormales)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.gridLayout_5.addWidget(self.label_32, 2, 10, 1, 1)
        self.cBoxProducc5 = QtWidgets.QComboBox(self.forNormales)
        self.cBoxProducc5.setObjectName("cBoxProducc5")
        self.gridLayout_5.addWidget(self.cBoxProducc5, 2, 9, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.forNormales)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.gridLayout_5.addWidget(self.label_25, 0, 0, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.forNormales)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.gridLayout_5.addWidget(self.label_29, 2, 1, 1, 1)
        self.terminales5Txt = QtWidgets.QLineEdit(self.forNormales)
        self.terminales5Txt.setObjectName("terminales5Txt")
        self.gridLayout_5.addWidget(self.terminales5Txt, 2, 2, 1, 1)
        self.greibach5Btn = QtWidgets.QPushButton(self.forNormales)
        self.greibach5Btn.setObjectName("greibach5Btn")
        self.gridLayout_5.addWidget(self.greibach5Btn, 6, 1, 1, 1)
        self.limpiar5Btn = QtWidgets.QPushButton(self.forNormales)
        self.limpiar5Btn.setObjectName("limpiar5Btn")
        self.gridLayout_5.addWidget(self.limpiar5Btn, 7, 1, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.forNormales)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.gridLayout_5.addWidget(self.label_27, 0, 8, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.forNormales)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.gridLayout_5.addWidget(self.label_31, 2, 4, 1, 1)
        self.variables5Txt = QtWidgets.QLineEdit(self.forNormales)
        self.variables5Txt.setObjectName("variables5Txt")
        self.gridLayout_5.addWidget(self.variables5Txt, 0, 2, 1, 1)
        self.ok5_2Btn = QtWidgets.QPushButton(self.forNormales)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ok5_2Btn.sizePolicy().hasHeightForWidth())
        self.ok5_2Btn.setSizePolicy(sizePolicy)
        self.ok5_2Btn.setObjectName("ok5_2Btn")
        self.gridLayout_5.addWidget(self.ok5_2Btn, 0, 11, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.forNormales)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.gridLayout_5.addWidget(self.label_28, 0, 4, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.forNormales)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.gridLayout_5.addWidget(self.label_34, 7, 0, 1, 1)
        self.sInicial5Txt = QtWidgets.QLineEdit(self.forNormales)
        self.sInicial5Txt.setObjectName("sInicial5Txt")
        self.gridLayout_5.addWidget(self.sInicial5Txt, 0, 9, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.forNormales)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.gridLayout_5.addWidget(self.label_30, 2, 8, 1, 1)
        self.ok5_3Btn = QtWidgets.QPushButton(self.forNormales)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ok5_3Btn.sizePolicy().hasHeightForWidth())
        self.ok5_3Btn.setSizePolicy(sizePolicy)
        self.ok5_3Btn.setObjectName("ok5_3Btn")
        self.gridLayout_5.addWidget(self.ok5_3Btn, 2, 5, 1, 1)
        self.ok5_1Btn = QtWidgets.QPushButton(self.forNormales)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ok5_1Btn.sizePolicy().hasHeightForWidth())
        self.ok5_1Btn.setSizePolicy(sizePolicy)
        self.ok5_1Btn.setObjectName("ok5_1Btn")
        self.gridLayout_5.addWidget(self.ok5_1Btn, 0, 5, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.forNormales)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.gridLayout_5.addWidget(self.label_26, 0, 1, 1, 1)
        self.agregarProd5Btn = QtWidgets.QPushButton(self.forNormales)
        self.agregarProd5Btn.setObjectName("agregarProd5Btn")
        self.gridLayout_5.addWidget(self.agregarProd5Btn, 2, 11, 1, 1)
        self.pestanas.addTab(self.forNormales, "")

        #Menu
        self.gridLayout.addWidget(self.pestanas, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 857, 23))
        self.menubar.setObjectName("menubar")
        self.menuPrincipal = QtWidgets.QMenu(self.menubar)
        self.menuPrincipal.setObjectName("menuPrincipal")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCargarAut = QtWidgets.QAction(MainWindow)#cargar automata
        self.actionCargarAut.setObjectName("actionCargarAut")
        self.actionCargarAutP = QtWidgets.QAction(MainWindow)#cargar automata a pila
        self.actionCargarAutP.setObjectName("actionCargarAutP")
        self.actionCargarGram = QtWidgets.QAction(MainWindow)
        self.actionCargarGram.setObjectName("actionCargarGram")#cargar gramatica
        self.menuPrincipal.addAction(self.actionCargarAut)
        self.menuPrincipal.addAction(self.actionCargarAutP)
        self.menuPrincipal.addAction(self.actionCargarGram)
        self.menubar.addAction(self.menuPrincipal.menuAction())
        self.retranslateUi(MainWindow)
        self.pestanas.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Eventos
        #Botones
        #REGEX
        self.ok1Btn.clicked.connect(self.buscandoResaltando)
        self.limpiar1Btn.clicked.connect(self.limpiar1)
        #Gramatica
        self.aplicar2Btn.clicked.connect(self.aplicar1)
        self.aplicarTransiBtn.clicked.connect(self.aplicarTransicion)
        self.guardarAut2.clicked.connect(self.guardarAutomata)
        self.limpiar2Btn.clicked.connect(self.limpiar2_1)#organizar
        self.generarG2Btn.clicked.connect(self.automataGramatica)
        self.guardar_gram2.clicked.connect(self.guardarGramatica1)
        #Automata a pila
        self.agregarAlfabeto4.clicked.connect(self.agregarAlfabetoC)
        self.agregarAPila4.clicked.connect(self.agregarAlfabetoPila)
        self.anadirEstado4Btn.clicked.connect(self.agregarEstadoPila)
        self.transi4Btn.clicked.connect(self.agregarTransicionP)


        #Items del menu
        self.actionCargarAut.triggered.connect(self.cargarAutomata)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_11.setText(_translate("MainWindow", "Expresión Regular:"))
        self.ok1Btn.setText(_translate("MainWindow", "O.K"))
        self.limpiar1Btn.setText(_translate("MainWindow", "Limpiar"))
        self.pestanas.setTabText(self.pestanas.indexOf(self.regex), _translate("MainWindow", "Regex"))
        self.estInicialLbl.setText(_translate("MainWindow", "Estado Inicial:"))
        self.alfabetoLbl.setText(_translate("MainWindow", "Alfabeto Σ: "))
        self.label_8.setText(_translate("MainWindow", "Autómata:"))
        self.label_4.setText(_translate("MainWindow", "V = {"))
        self.checkBoxDerecha2.setText(_translate("MainWindow", "Por derecha"))
        self.label_7.setText(_translate("MainWindow", "P = {"))
        self.label_5.setText(_translate("MainWindow", "T= {"))
        self.aplicar2Btn.setText(_translate("MainWindow", "Aplicar"))
        self.estAceptadoresLbl.setText(_translate("MainWindow", "Estados aceptadores: "))
        self.label.setText(_translate("MainWindow", "Transiciones:"))
        self.origenLbl.setText(_translate("MainWindow", "Origen:"))
        self.destinoLbl.setText(_translate("MainWindow", "Destino:"))
        self.label_23.setText(_translate("MainWindow", "}"))
        self.guardarAut2.setText(_translate("MainWindow", "Guardar Autómata"))
        self.valorLbl.setText(_translate("MainWindow", "Valor:"))
        self.aplicarTransiBtn.setText(_translate("MainWindow", "Aplicar Transición"))
        self.guardar_gram2.setText(_translate("MainWindow", "Guardar Gramática"))
        self.checkBoxIzquierda2.setText(_translate("MainWindow", "Por izquierda"))
        self.label_2.setText(_translate("MainWindow", "   GRAMÁTICA"))
        self.label_24.setText(_translate("MainWindow", "}"))
        self.label_6.setText(_translate("MainWindow", "S ="))
        self.label_22.setText(_translate("MainWindow", "}"))
        self.limpiar2Btn.setText(_translate("MainWindow", "Limpiar"))
        self.generarG2Btn.setText(_translate("MainWindow", "Generar Gramática"))
        self.pestanas.setTabText(self.pestanas.indexOf(self.gramatica), _translate("MainWindow", "Gramática"))
        self.label_15.setText(_translate("MainWindow", "}"))
        self.guardar_gram3Btn.setText(_translate("MainWindow", "Guardar Grámatica"))
        self.ok3_1Btn.setText(_translate("MainWindow", "OK"))
        self.label_13.setText(_translate("MainWindow", "V = {"))
        self.label_12.setText(_translate("MainWindow", "Gramática:"))
        self.label_14.setText(_translate("MainWindow", "S="))
        self.ok3_3Btn.setText(_translate("MainWindow", "OK"))
        self.ok3_2Btn.setText(_translate("MainWindow", "OK"))
        self.label_16.setText(_translate("MainWindow", "T = {"))
        self.label_17.setText(_translate("MainWindow", "}"))
        self.label_18.setText(_translate("MainWindow", "P = {"))
        self.agregarProd3Btn.setText(_translate("MainWindow", "Agregar producción"))
        self.label_19.setText(_translate("MainWindow", "}"))
        self.label_20.setText(_translate("MainWindow", "Cadena:"))
        self.checkBoxDerecha3.setText(_translate("MainWindow", "Por derecha"))
        self.generar3Btn.setText(_translate("MainWindow", "Generar"))
        self.checkBoxIzquierda3.setText(_translate("MainWindow", "Por izquierda"))
        self.label_21.setText(_translate("MainWindow", "Árbol de Derivación:"))
        self.limpiar3_1Btn.setText(_translate("MainWindow", "Limpiar(Gramática)"))
        self.limpiar3_2Btn.setText(_translate("MainWindow", "Limpiar(Árbol)"))
        self.pestanas.setTabText(self.pestanas.indexOf(self.arbolDerivacion), _translate("MainWindow", "Árbol Derivación"))
        self.maquinaLbl.setText(_translate("MainWindow", "M =  {"))
        self.label_3.setText(_translate("MainWindow", "}"))
        self.QLbl.setText(_translate("MainWindow", "Q"))
        self.inicial2Lbl.setText(_translate("MainWindow", "q0"))
        self.aceptadores2Lbl.setText(_translate("MainWindow", "F"))
        self.alfabeto2Lbl.setText(_translate("MainWindow", "Σ"))
        self.transiLbl.setText(_translate("MainWindow", "δ"))
        self.checkBoxInicial4.setText(_translate("MainWindow", "Inicial"))
        self.checkBoxAceptador4.setText(_translate("MainWindow", "Aceptador"))
        self.anadirEstado4Btn.setText(_translate("MainWindow", "Añadir Estado"))
        self.origenLbl_2.setText(_translate("MainWindow", "Origen"))
        self.transi4Btn.setText(_translate("MainWindow", "Añadir Transición"))
        self.alfabeto2Lbl_2.setText(_translate("MainWindow", "Σ = {"))
        self.label_9.setText(_translate("MainWindow", "}"))
        self.alfabeto2Lbl_3.setText(_translate("MainWindow", "T= {"))
        self.label_10.setText(_translate("MainWindow", "}"))
        self.agregarAlfabeto4.setText(_translate("MainWindow", "Agregar alfabeto"))
        self.agregarAPila4.setText(_translate("MainWindow", "Agregar alfabeto(pila)"))
        self.origenLbl_3.setText(_translate("MainWindow", "VALOR"))
        self.origenLbl_4.setText(_translate("MainWindow", "Simbolo entrada"))
        self.origenLbl_5.setText(_translate("MainWindow", "Simbolo pila"))
        self.origenLbl_6.setText(_translate("MainWindow", "Destino"))
        self.origenLbl_7.setText(_translate("MainWindow", "Simbolo escribir en pila"))
        self.alfabeto2Lbl_4.setText(_translate("MainWindow", "T"))
        self.alfabeto2Lbl_5.setText(_translate("MainWindow", "Z0"))
        self.maquinaLbl_2.setText(_translate("MainWindow", "Cadena:"))
        self.analizar4Btn.setText(_translate("MainWindow", "Analizar"))
        self.maquinaLbl_3.setText(_translate("MainWindow", "Estado Actual:"))
        self.guardarAut4Btn.setText(_translate("MainWindow", "Guardar Autómata"))
        self.limpiar4Btn.setText(_translate("MainWindow", "Limpiar"))
        self.sigpaso4Btn.setText(_translate("MainWindow", "Siguiente paso"))
        self.maquinaLbl_4.setText(_translate("MainWindow", "Pila:"))
        self.pestanas.setTabText(self.pestanas.indexOf(self.automataPila), _translate("MainWindow", "Autómata a Pila"))
        self.guardar_gram5Btn.setText(_translate("MainWindow", "Guardar Gramática"))
        self.chomsky5Btn.setText(_translate("MainWindow", "Chomsky"))
        self.label_33.setText(_translate("MainWindow", "Formas Normales:"))
        self.label_32.setText(_translate("MainWindow", "}"))
        self.label_25.setText(_translate("MainWindow", "Gramática:"))
        self.label_29.setText(_translate("MainWindow", "T = {"))
        self.greibach5Btn.setText(_translate("MainWindow", "Greibach"))
        self.limpiar5Btn.setText(_translate("MainWindow", "Limpiar"))
        self.label_27.setText(_translate("MainWindow", "S ="))
        self.label_31.setText(_translate("MainWindow", "}"))
        self.ok5_2Btn.setText(_translate("MainWindow", "OK"))
        self.label_28.setText(_translate("MainWindow", "}"))
        self.label_34.setText(_translate("MainWindow", "Acciones:"))
        self.label_30.setText(_translate("MainWindow", "P = {"))
        self.ok5_3Btn.setText(_translate("MainWindow", "OK"))
        self.ok5_1Btn.setText(_translate("MainWindow", "OK"))
        self.label_26.setText(_translate("MainWindow", "V = {"))
        self.agregarProd5Btn.setText(_translate("MainWindow", "Agregar Producción"))
        self.pestanas.setTabText(self.pestanas.indexOf(self.forNormales), _translate("MainWindow", "Formas Normales"))

        self.menuPrincipal.setTitle(_translate("MainWindow", "Menu"))
        self.actionCargarAut.setText(_translate("MainWindow", "Cargar Autómata"))
        self.actionCargarAutP.setText(_translate("MainWindow", "Cargar Autómata a Pila"))
        self.actionCargarGram.setText(_translate("MainWindow", "Cargar Gramática"))

    #REGEX
    def buscandoResaltando(self):
        cursor= self.campoTexto1.textCursor()#se asigna a una variable el cursor del campo de texto

        #Se configura el formato para las coincidencias(resaltado)
        formato= QtGui.QTextCharFormat()#formato para cada caracter
        formato.setBackground(QtGui.QBrush(QtGui.QColor("yellow"))) #se define el color de resaltado

        try:
            # Lectura de la expresion regular
            patron= self.expRegular1Txt.text()
            regex=QtCore.QRegExp(patron)

            #Busqueda de coincidencias y resaltado
            pos=0
            index= regex.indexIn(self.campoTexto1.toPlainText(),pos)
            while( index != -1):
                #Se selecciona la coincidencia en el texto y se le aplica el formato
                cursor.setPosition(index)
                cursor.movePosition(QtGui.QTextCursor.EndOfWord,1)# lo que recibe el metodo es el modo de moverse y la cantidad de veces que se va a repetir
                cursor.mergeCharFormat(formato)# se aplica el formato a todos los caracteres de la seleccion del cursor

                #Nos movemos a la siguiente coincidencia
                pos= index + regex.matchedLength()# regex.matchedLength() retorna la longitud de la ultima coincidencia(string)
                index= regex.indexIn(self.campoTexto1.toPlainText(),pos)
                '''regex.indexIn retorna la posicion de la primera coincidencia, recibe el texto que se revisa y la posicion
                desde donde va a empezar a buscar, si retorna -1 es porque no encuentra coincidencias'''

        except IOError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Advertencia")
            msg.setText("Ingrese la expresión regular de forma correcta")
            msg.exec_()
            print(IOError)

    def limpiar1(self):
        self.campoTexto1.clear()
        self.expRegular1Txt.setText("")

    #GRAMATICA
    def crearEscenas(self):
        escena1 = QGraphicsScene()
        self.graphicsView_2.setScene(escena1)
        rcontent = self.graphicsView_2.contentsRect()
        self.graphicsView_2.setSceneRect(0, 0, rcontent.width() + 600, rcontent.height() + 600)

        escena2 = QGraphicsScene()
        self.graphicsView_3.setScene(escena2)
        rcontent = self.graphicsView_3.contentsRect()
        self.graphicsView_3.setSceneRect(0, 0, rcontent.width() + 1000, rcontent.height() + 1000)


    #Dibujando automata
    def dibujarEstados(self, posX, posY, graphicsView):  # Aqui tambien se agrega un estado logicamente, recibe un identificador del metodo que lo llama

        estado = QGraphicsEllipseItem(posX, posY, 44, 44)  # posX,posY,ancho,alto

        if self.colisionEstados(self.automata, estado, 1) is False:
            nuevoEst = self.automata.agregarEstado(posX, posY)  # se agrega el estado logicamente
            lapiz = QPen(Qt.black)
            lapiz.setWidth(2)
            estado.setPen(lapiz)
            self.estadosTotales = self.estadosTotales + 1
            self.elemGraficos[self.estadosTotales] = [estado]  # se agrega el estado grafico al diccionario (recoradar que aui se guardaran todos los elementos graficos relacionados con un estado)
            self.automata.estados[nuevoEst.nombre].claveGraficos = self.estadosTotales  # Se agrega la claveCirculo al nuevo estado creado logicamente
            graphicsView.scene().addItem(estado)

            texto = QGraphicsTextItem(nuevoEst.nombre, estado)  # texto, objeto sobre el que va el texto
            texto.setX(posX + 8)
            texto.setY(posY + 5)
            serifFont = QFont("Times", 12, QFont.Bold)
            texto.setFont(serifFont)
            texto.setDefaultTextColor(Qt.red)
            self.elemGraficos[self.estadosTotales].append(texto)  # se agrega el nombre grafico  al diccionario, en la lista del estado
            graphicsView.scene().addItem(texto)

    def dibujarEstLogicos(self,automata,graphicsView):

        for estado in automata.estados.values():
            estGrafico = QGraphicsEllipseItem(estado.posX, estado.posY, 44, 44)
            while self.colisionEstados(automata,estGrafico,2)==True:
                posX = []  # posiciones en x de todos los estados que ya tiene asignada posicion
                posY = []  # posiciones en y de todos los estados que ya tiene asignada posicion

                for esta in automata.estados.values():
                    if esta.posX != None and esta.posY != None:
                        posX.append(esta.posX)
                        posY.append(esta.posY)

                # Se le asigna posicion aleatoria
                estGrafico.setX(random.randrange(min(posX), max(posX) + 222))  # se sumas 198 para que quepan mas o menos 4 estados de mas a la derecha del estado con pos mayor en x
                estGrafico.setY(random.randrange(min(posY), max(posY) + 222))
                estado.posX=estGrafico.x()
                estado.posY=estGrafico.y()
                #Estar pendiente de la parte de arriba

            lapiz = QPen(Qt.black)
            lapiz.setWidth(2)
            estGrafico.setPen(lapiz)
            self.estadosTotales = self.estadosTotales + 1
            self.elemGraficos[self.estadosTotales] = [estGrafico]  # se agrega el estado grafico al diccionario (recoradar que aui se guardaran todos los elementos graficos relacionados con un estado)
            automata.estados[estado.nombre].claveGraficos = self.estadosTotales  # Se agrega la claveCirculo al nuevo estado creado logicamente
            graphicsView.scene().addItem(estGrafico)

            texto = QGraphicsTextItem(estado.nombre, estGrafico)  # texto, objeto sobre el que va el texto
            texto.setX(estado.posX + 8)
            texto.setY(estado.posY + 5)
            serifFont = QFont("Times", 12, QFont.Bold)
            texto.setFont(serifFont)
            texto.setDefaultTextColor(Qt.red)
            self.elemGraficos[self.estadosTotales].append(texto)  # se agrega el nombre grafico  al diccionario, en la lista del estado
            graphicsView.scene().addItem(texto)

            #Se pinta la flecha al estado inicial
            lapiz2 = QPen(Qt.darkMagenta)
            lapiz2.setWidth(4)
            if estado.esInicial:
                posX = estado.posX
                posY = estado.posY

                linea = QGraphicsLineItem(posX, posY, posX - 13, posY - 5, None)
                linea.setPen(lapiz2)
                graphicsView.scene().addItem(linea)
                self.dibujarFlecha(posX, posY, 6, graphicsView)
                self.elemGraficos[self.estadosTotales].append(linea)
            #Se pinta el identificador(circulo) a los estados aceptadores
            if estado.esAceptador:
                posX = estado.posX
                posY = estado.posY
                circulo = QGraphicsEllipseItem(posX - 4, posY - 4, 53, 53)
                circulo.setPen(lapiz2)
                graphicsView.scene().addItem(circulo)
                self.elemGraficos[self.estadosTotales].append(circulo)

    def colisionEstados(self,automata,estadoADibujar,metodoDibujo): #Verifica que un estado no quede dibujado sobre otro.metodoDibujo es un numero que identifica cual es el metodo de dibujo, para saber si saca el mensaje o no
        for estado in automata.estados.values():
            if estado.claveGraficos in self.elemGraficos:
                if estadoADibujar.rect().intersects(self.elemGraficos[estado.claveGraficos][0].rect()):#recordar que en la posicion 0 esta el circulo
                    if metodoDibujo==1:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Warning)
                        msg.setWindowTitle("Advertencia")
                        msg.setText("Acción inválida")
                        msg.exec_()
                    return True
        return False



    def dibujarTransicion(self, estOrigen,estDestino,valor,graphicsView):
        if estOrigen==estDestino:
            pInicial = QPainterPath(QPointF(estOrigen.posX + 40, estOrigen.posY+10))
            c1 = QPointF(estOrigen.posX + 40,estOrigen.posY - 33)  # como es hacia arriba la posicion en y debe estar por debajo(valor menor) a posY en punto inicial y final
            c2 = QPointF(estDestino.posX+8, estDestino.posY - 33)
            pFinal = QPointF(estDestino.posX +8, estDestino.posY+5)
            pInicial.cubicTo(c1, c2, pFinal)

            # Se agrega el valor de la transicion graficamente
            #pInicial.addText(estOrigen.posX + 20, estOrigen.posY -33, QFont("Times", 10), valor)
            texto = QGraphicsTextItem(valor, self.elemGraficos[estOrigen.claveGraficos][0])  # texto, objeto sobre el que va el texto
            texto.setX(estOrigen.posX + 20)
            texto.setY(estOrigen.posY -38)
            serifFont = QFont("Times", 10, QFont.Bold)
            texto.setFont(serifFont)
            texto.setDefaultTextColor(Qt.darkBlue)

            # Se agrega la arista al graphicsView
            graphicsView.scene().addPath(pInicial)
            graphicsView.scene().addItem(texto)
            self.dibujarFlecha(pFinal.x(), pFinal.y(), 5,graphicsView)


        else:
            #Linea a la derecha
            if estDestino.posX-estOrigen.posX >0 and estDestino.posX-estOrigen.posX > estDestino.posY-estOrigen.posY and estDestino.posX-estOrigen.posX > estOrigen.posY-estDestino.posY:
                pInicial=QPainterPath(QPointF(estOrigen.posX+44,estOrigen.posY+20))
                c1=QPointF(estOrigen.posX+44,estOrigen.posY-20)#como es hacia arriba la posicion en y debe estar por debajo(valor menor) a posY en punto inicial y final
                c2=QPointF(estDestino.posX,estDestino.posY-20)
                pFinal=QPointF(estDestino.posX,estDestino.posY+20)
                pInicial.cubicTo(c1,c2,pFinal)

                #Se agrega el valor de la transicion graficamente
                #pInicial.addText(estOrigen.posX+47,estOrigen.posY+20,QFont("Times", 10),valor)
                texto = QGraphicsTextItem(valor, self.elemGraficos[estOrigen.claveGraficos][0])  # texto, objeto sobre el que va el texto
                texto.setX(estOrigen.posX+47)
                texto.setY(estOrigen.posY)
                serifFont = QFont("Times", 10, QFont.Bold)
                texto.setFont(serifFont)
                texto.setDefaultTextColor(Qt.darkBlue)

                #Se agrega la arista al graphicsView
                graphicsView.scene().addPath(pInicial)
                graphicsView.scene().addItem(texto)
                self.dibujarFlecha(pFinal.x(),pFinal.y(),1,graphicsView)


            # Linea a la izquierda
            elif estDestino.posX - estOrigen.posX < 0 and estOrigen.posX - estDestino.posX > estDestino.posY - estOrigen.posY and estOrigen.posX - estDestino.posX > estOrigen.posY - estDestino.posY:
                pInicial = QPainterPath(QPointF(estOrigen.posX, estOrigen.posY + 25))
                c1 = QPointF(estOrigen.posX , estOrigen.posY + 55)#como es hacia abajo la posicion en y debe estar pos encima de la posY en el punto inicial y final
                c2 = QPointF(estDestino.posX+44, estDestino.posY + 55)
                pFinal = QPointF(estDestino.posX +44, estDestino.posY +25)
                pInicial.cubicTo(c1, c2, pFinal)

                # Se agrega el valor de la transicion graficamente
                #pInicial.addText(estOrigen.posX-8, estOrigen.posY + 25, QFont("Times", 10), valor)
                texto = QGraphicsTextItem(valor, self.elemGraficos[estOrigen.claveGraficos][0])  # texto, objeto sobre el que va el texto
                texto.setX(estOrigen.posX-8)
                texto.setY(estOrigen.posY + 25)
                serifFont = QFont("Times", 10, QFont.Bold)
                texto.setFont(serifFont)
                texto.setDefaultTextColor(Qt.darkBlue)

                # Se agrega la arista al graphicsView
                graphicsView.scene().addPath(pInicial)
                graphicsView.scene().addItem(texto)
                self.dibujarFlecha(pFinal.x(), pFinal.y()+3, 2,graphicsView)


            # Linea hacia abajo
            elif estDestino.posY - estOrigen.posY > 0 and estDestino.posY - estOrigen.posY > estDestino.posX - estOrigen.posX and estDestino.posY - estOrigen.posY > estOrigen.posX - estDestino.posX:
                pInicial = QPainterPath(QPointF(estOrigen.posX+44, estOrigen.posY + 22))
                c1 = QPointF(estOrigen.posX+88,estOrigen.posY+22)  # como es hacia abajo la posicion en y debe estar pos encima de la posY en el punto inicial y final
                c2 = QPointF(estDestino.posX + 88, estDestino.posY+22)
                pFinal = QPointF(estDestino.posX + 44, estDestino.posY+22)
                pInicial.cubicTo(c1, c2, pFinal)

                # Se agrega el valor de la transicion graficamente
                #pInicial.addText(estOrigen.posX+50, estOrigen.posY + 22, QFont("Times", 10), valor)
                texto = QGraphicsTextItem(valor, self.elemGraficos[estOrigen.claveGraficos][0])  # texto, objeto sobre el que va el texto
                texto.setX(estOrigen.posX+50)
                texto.setY(estOrigen.posY + 30)
                serifFont = QFont("Times", 10, QFont.Bold)
                texto.setFont(serifFont)
                texto.setDefaultTextColor(Qt.darkBlue)

                # Se agrega la arista al graphicsView
                graphicsView.scene().addPath(pInicial)
                graphicsView.scene().addItem(texto)
                self.dibujarFlecha(pFinal.x(), pFinal.y(), 3,graphicsView)


            # Linea hacia arriba
            else:
                pInicial = QPainterPath(QPointF(estOrigen.posX, estOrigen.posY +22))
                c1 = QPointF(estOrigen.posX - 44,estOrigen.posY+22 )  # como es hacia abajo la posicion en y debe estar pos encima de la posY en el punto inicial y final
                c2 = QPointF(estDestino.posX - 44, estDestino.posY + 22)
                pFinal = QPointF(estDestino.posX , estDestino.posY + 22)
                pInicial.cubicTo(c1, c2, pFinal)

                # Se agrega el valor de la transicion graficamente
                #pInicial.addText(estOrigen.posX-8, estOrigen.posY +24, QFont("Times", 10), valor)
                texto = QGraphicsTextItem(valor, self.elemGraficos[estOrigen.claveGraficos][0])  # texto, objeto sobre el que va el texto
                texto.setX(estOrigen.posX-13)
                texto.setY(estOrigen.posY +15)
                serifFont = QFont("Times", 10, QFont.Bold)
                texto.setFont(serifFont)
                texto.setDefaultTextColor(Qt.darkBlue)

                # Se agrega la arista al graphicsView
                graphicsView.scene().addPath(pInicial)
                graphicsView.scene().addItem(texto)
                self.dibujarFlecha(pFinal.x(), pFinal.y(), 4,graphicsView)


        #Limpiar Campos
        self.origen2Txt.setText("")
        self.destino2Txt.setText("")
        self.valor2Txt.setText("")



    def dibujarAutomataLogico(self,automata,graphicsView):
        self.dibujarEstLogicos(automata,graphicsView)

        #Se dibujan las transiciones de cada estado
        valorEnv=""#valor de la transicion que se le enviara al metodo de dibujarTransicion
        for estado in automata.estados.values():
            revisados = {}  # contendra las claves de las transiciones ya revisadas
            for valor in estado.transiciones:
                valorEnv=valor
                for destino in estado.transiciones[valor]:
                    if not valor in revisados:
                        revisados[valor]=[destino]
                    else:
                        revisados[valor].append(destino)
                    for clave,destinosT in estado.transiciones.items():
                        if clave in revisados:
                            if not destino in revisados[clave]:
                                if destino in destinosT:
                                    valorEnv += "," + clave
                                    revisados[clave].append(destino)
                        if not clave in revisados:
                            if destino in destinosT:
                                valorEnv+=","+clave
                                revisados[clave]=[destino]

                    self.dibujarTransicion(estado,destino,valorEnv,graphicsView)

    def dibujarFlecha(self,xFinal,yFinal,direccion,graphicsView):
        lapiz = QPen(Qt.blue)
        lapiz.setWidth(2)

        if direccion==1:#derecha
            linea1=QGraphicsLineItem(xFinal,yFinal,xFinal-10,yFinal,None) #abajo
            linea2=QGraphicsLineItem(xFinal,yFinal,xFinal+2,yFinal- 10,None) #arriba
            linea1.setPen(lapiz)
            linea2.setPen(lapiz)
            graphicsView.scene().addItem(linea1)
            graphicsView.scene().addItem(linea2)

        elif direccion==2:#izquierda
            linea1 = QGraphicsLineItem(xFinal, yFinal, xFinal, yFinal+10, None)#abajo
            linea2 = QGraphicsLineItem(xFinal, yFinal, xFinal +10, yFinal, None)#arriba
            linea1.setPen(lapiz)
            linea2.setPen(lapiz)
            graphicsView.scene().addItem(linea1)
            graphicsView.scene().addItem(linea2)

        elif direccion==3:#Abajo
            linea1 = QGraphicsLineItem(xFinal, yFinal, xFinal+10, yFinal - 10, None)#arriba
            linea2 = QGraphicsLineItem(xFinal, yFinal, xFinal+10, yFinal+ 5, None)#abajo
            linea1.setPen(lapiz)
            linea2.setPen(lapiz)
            graphicsView.scene().addItem(linea1)
            graphicsView.scene().addItem(linea2)

        elif direccion==4:#Arriba
            linea1 = QGraphicsLineItem(xFinal, yFinal, xFinal-10, yFinal - 5, None)
            linea2 = QGraphicsLineItem(xFinal, yFinal, xFinal - 5, yFinal + 10, None)
            linea1.setPen(lapiz)
            linea2.setPen(lapiz)
            graphicsView.scene().addItem(linea1)
            graphicsView.scene().addItem(linea2)

        elif direccion==5:#el mismo
            linea1 = QGraphicsLineItem(xFinal, yFinal, xFinal - 5, yFinal - 10, None)
            linea2 = QGraphicsLineItem(xFinal, yFinal, xFinal + 5, yFinal - 10, None)
            linea1.setPen(lapiz)
            linea2.setPen(lapiz)
            graphicsView.scene().addItem(linea1)
            graphicsView.scene().addItem(linea2)

        else:#flecha de estado inicial
            linea1 = QGraphicsLineItem(xFinal, yFinal, xFinal - 8, yFinal + 2, None)  # abajo
            linea2 = QGraphicsLineItem(xFinal, yFinal, xFinal , yFinal - 5, None)  # arriba
            lapiz2 = QPen(Qt.darkMagenta)
            lapiz2.setWidth(2)
            linea1.setPen(lapiz2)
            linea2.setPen(lapiz2)
            graphicsView.scene().addItem(linea1)
            graphicsView.scene().addItem(linea2)


    def mousePressEvent(self, event):

        if self.alfabeto2Txt.text() != "":#solo permite dibujar si ya se tiene especificado el alfabeto
            try:
                if len(self.automata.alfabeto) == 0:
                    self.automata.alfabeto = self.alfabeto2Txt.text().split(",")#Cada letra del alfabeto se guarda en una lista
                    self.alfabeto2Txt.setDisabled(True)

                e = QPointF(self.graphicsView_2.mapToScene(event.pos()))  # Se detecta el punto donde el usuario ha presionado el mouse
                posX = e.x()-53
                posY = e.y()-104
                self.dibujarEstados(posX,posY,self.graphicsView_2)
                print('x:'+str(posX))
                print('y:'+str(posY))


            except IOError:
                msg = QMessageBox()  # Se crea un cuadro de dialogo
                msg.setIcon(QMessageBox.Warning)  # Se especifica que es de tipo Warning
                msg.setWindowTitle("Advertencia")
                msg.setText("Ingrese datos válidos en el alfabeto \n Ejemplo: A,B,C,D")
                msg.exec_()
                self.alfabeto2Txt.setText("")
                print(IOError)

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Advertencia")
            msg.setText("Ingrese el Alfabeto por favor")
            msg.exec_()

    def aplicarTransicion(self):
        estOrigen=Estado("",0,0,"","")
        estDestino=""
        valor=""

        if self.origen2Txt.text()!= "" and self.destino2Txt.text()!= "" and self.valor2Txt.text()!= "":
            try:
                estOrigen= self.automata.estados[self.origen2Txt.text().lower()]
                estDestino= self.automata.estados[self.destino2Txt.text().lower()]

                valor=self.validarValor1()#Recordar que es una lista

                if valor!=None:
                    for simbolo in valor:
                        self.automata.estados[estOrigen.nombre].agregarTransicion(simbolo,estDestino)#se agrega la transicion de forma logica(simbolo por simbolo)
                    self.dibujarTransicion(estOrigen,estDestino,self.valor2Txt.text(),self.graphicsView_2)

            except IOError:
                print(IOError)
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Advertencia")
                msg.setText("Por favor ingrese estados válidos")
                msg.exec_()
                self.origen2Txt.setText("")
                self.destino2Txt.setText("")


        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Advertencia")
            msg.setText("Por favor ingrese todos los datos requeridos para esta acción")
            self.origen2Txt.setText("")
            self.destino2Txt.setText("")
            self.valor2Txt.setText("")
            msg.exec_()


    def validarValor1(self):

        try:
            valorText = self.valor2Txt.text().split(",")#lista de valores(pueden ser varios)

            for letra in valorText:

                if not letra in self.automata.alfabeto:
                    if letra!='E':#Transiciones vacias
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Warning)
                        msg.setWindowTitle("Advertencia")
                        msg.setText("Por favor ingrese valores del Alfabeto")
                        msg.exec_()
                        self.valor2Txt.setText("")
                        return None

                return valorText

        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Advertencia")
            msg.setText("Por favor ingrese el valor de forma correcta \n Ejemplo: B,C")
            msg.exec_()
            self.valor2Txt.setText("")

    def aplicar1(self):

        posiblesAceptadores = self.estAceptadores2Txt.text().lower().split(",")

        lapiz = QPen(Qt.darkMagenta)
        lapiz.setWidth(4)

        #Estado Inicial
        try:
            if self.automata.estadoIni=="":
                self.automata.estadoIni = self.estInicial2Txt.text().lower()
                posX= self.automata.estados[self.automata.estadoIni].posX
                posY= self.automata.estados[self.automata.estadoIni].posY

                linea=QGraphicsLineItem(posX,posY,posX-13,posY-5,None)
                linea.setPen(lapiz)
                self.graphicsView_2.scene().addItem(linea)
                self.dibujarFlecha(posX,posY,6,self.graphicsView_2)
                self.automata.estados[self.automata.estadoIni].esInicial=True
                self.estInicial2Txt.setDisabled(True)

        except:
            if self.automata.estadoIni == "":
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Advertencia")
                msg.setText("El estado inicial ya esta asignado")
                msg.exec_()
                self.estInicial2Txt.setText("")
                self.automata.estadoIni = ""
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Advertencia")
                msg.setText("Ingrese un estado válido")
                msg.exec_()
                self.estInicial2Txt.setText("")
                self.automata.estadoIni=""

        #Estados Aceptadores
        for estado in posiblesAceptadores:
            try:
                posX=self.automata.estados[estado].posX
                posY=self.automata.estados[estado].posY
                circulo=QGraphicsEllipseItem(posX-4,posY-4,53,53)
                circulo.setPen(lapiz)
                self.graphicsView_2.scene().addItem(circulo)
                self.automata.estAceptadores.append(estado)
                self.automata.estados[estado].esAceptador=True


            except:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Advertencia")
                msg.setText("El estado "+estado+" no es válido")
                msg.exec_()
                self.estAceptadores2Txt.setText("")


        self.estAceptadores2Txt.setDisabled(True)

    def limpiar2_1(self):
        #automata
        self.automata = Automata()
        self.elemGraficos.clear()

        self.graphicsView_2.scene().clear()
        self.alfabeto2Txt.setText("")
        self.estInicial2Txt.setText("")
        self.estAceptadores2Txt.setText("")
        self.origen2Txt.setText("")
        self.destino2Txt.setText("")
        self.valor2Txt.setText("")
        self.alfabeto2Txt.setDisabled(False)
        self.estInicial2Txt.setDisabled(False)
        self.estAceptadores2Txt.setDisabled(False)

        #gramatica
        self.comboBoxProducc2.clear()
        self.comboBoxTermin2.clear()
        self.combovariables2.clear()
        self.vInicialTxt.clear()
        self.checkBoxDerecha2.setChecked(False)
        self.checkBoxIzquierda2.setChecked(False)
        self.gramatica1=Gramatica()

        self.contador=0

    def automataGramatica(self):
        self.contador+=1
        #Limpia la gramatica en caso de que se llame el metodo con una ya existente(con que uno se sus atributos tenga valor, sabemos que los demas tambien)
        if self.gramatica1.valInicial!="":
            self.comboBoxProducc2.clear()
            self.comboBoxTermin2.clear()
            self.combovariables2.clear()
            self.vInicialTxt.clear()
            self.gramatica1 = Gramatica()
        if self.automata!=None:
            if self.checkBoxDerecha2.isChecked() and self.checkBoxIzquierda2.isChecked()==False:
                self.gramatica1.gramaticaDeAutomata(self.automata,'derecha', self.contador)
                #vuelve a dibujar el automata
                if self.contador<=1:
                    self.graphicsView_2.scene().clear()
                    self.graphicsView_2.scene().clear()
                    self.elemGraficos.clear()
                    self.dibujarAutomataLogico(self.automata,self.graphicsView_2)
            elif self.checkBoxIzquierda2.isChecked() and self.checkBoxDerecha2.isChecked()==False:
                self.gramatica1.gramaticaDeAutomata(self.automata, 'izquierda',self.contador)
                # vuelve a dibujar el automata
                if self.contador <= 1:
                    self.graphicsView_2.scene().clear()
                    self.graphicsView_2.scene().clear()
                    self.elemGraficos.clear()
                    self.dibujarAutomataLogico(self.automata, self.graphicsView_2)
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Advertencia")
                msg.setText("Por favor realice una acción válida")
                msg.exec_()
            self.checkBoxDerecha2.setChecked(False)
            self.checkBoxIzquierda2.setChecked(False)

            #Se agrega la gramatica graficamente
            if self.gramatica1!= None:
                #Se agregan las variables con sus producciones
                for variable in self.gramatica1.variables:
                    self.combovariables2.addItem(variable) #variable
                    #Producciones
                    producciones = ""
                    cont=0 #contara la cantidad de veces que se ejecuta el for de abajo
                    for producc in self.gramatica1.variables[variable].producciones.values():
                        cont += 1
                        for elemento in producc:
                            producciones+=elemento
                        if cont!= len(self.gramatica1.variables[variable].producciones):
                            producciones+=" | "

                    self.comboBoxProducc2.addItem(variable+" -> "+ producciones)

                #Variable incial
                self.vInicialTxt.setText(self.gramatica1.valInicial)

                #terminales
                self.comboBoxTermin2.addItems(self.gramatica1.terminales)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Advertencia")
            msg.setText("Ingrese un autómata")
            msg.exec_()

    def guardarGramatica1(self):
        self.guardarGramatica(self.gramatica1)

    #AUTOMATA A PILA
    #agregar alfabeto cadena
    def agregarAlfabetoC(self):
        try:
            alfabet= self.alfabeto4.text().split(',')
            self.automataP.alfabeto=alfabet
            self.alfabeto4.setDisabled(True)

            #Se agrega al combobox
            self.cBoxAlfabeto4_.addItems(alfabet)

        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Advertencia")
            msg.setText("Ingrese un alfabeto válido")
            msg.exec_()

    #agregar alfabeto pila
    def agregarAlfabetoPila(self):
        if len(self.automataP.alfabeto)>0:
            try:
                alfabetP= self.alfabetoPila4.text().split(',')
                self.automataP.alfabetoPila=alfabetP
                self.automataP.alfabetoPila.append('z')
                self.alfabetoPila4.setText('z,'+self.alfabetoPila4.text()) # se agrega en el campo de texto el simbolo Inicial por defecto
                self.alfabetoPila4.setDisabled(True)

                #Se agrega al combobox
                self.cBoxSimbolosPila4.addItem('z') #simbolo incicial por defecto
                self.cBoxSimbolosPila4.addItems(alfabetP)

                # Tambien se agrega el simbolo incial de la pila al combobox
                self.cBoxSimboloIniP4.addItem('z')
            except:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Advertencia")
                msg.setText("Ingrese un alfabeto para la pila válido")
                msg.exec_()

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Advertencia")
            msg.setText("Por favor ingrese primero el alfabeto de la cadena")
            msg.exec_()
            self.alfabetoPila4.setText('')

    #agregar estado
    def agregarEstadoPila(self):
        if len(self.automataP.alfabeto)>0 and len(self.automataP.alfabetoPila)>0:
            nuevoEst= self.automataP.agregarEstadoAP()

            #Se agrega al combobox estados
            self.cBoxEstados4.addItem(nuevoEst.nombre)

            if self.checkBoxInicial4.isChecked():
                if self.automataP.estadoIni=='':
                    nuevoEst.esInicial=True
                    self.automataP.estadoIni=nuevoEst.nombre

                    # Se agrega al combobox estado incial
                    self.cBoxEstInicial4.addItem(nuevoEst.nombre)

                    self.checkBoxInicial4.setChecked(False)
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setWindowTitle("Advertencia")
                    msg.setText("El autómata ya tiene un estado inicial asignado")
                    msg.exec_()
                    self.checkBoxInicial4.setChecked(False)

            if self.checkBoxAceptador4.isChecked():
                nuevoEst.esAceptador=True
                self.automataP.estAceptadores.append(nuevoEst.nombre)

                # Se agrega al combobox estados aceptadores
                self.cBoxAceptadores4.addItem(nuevoEst.nombre)

                self.checkBoxAceptador4.setChecked(False)

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Advertencia")
            msg.setText("Por favor ingrese primero los alfabetos")
            msg.exec_()
            self.checkBoxInicial4.setChecked(False)
            self.checkBoxAceptador4.setChecked(False)


    #agregar transicion
    def agregarTransicionP(self):
        correcto=True

        if self.origen4Txt.text().lower() not in self.automataP.estados:
            correcto=False
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Advertencia")
            msg.setText("El origen es incorrecto")
            msg.exec_()
            self.origen4Txt.setText('')

        if self.sEntrada4Txt.text() not in self.automataP.alfabeto and self.sEntrada4Txt.text()!='E':
            correcto = False
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Advertencia")
            msg.setText("El símbolo de entrada es incorrecto")
            msg.exec_()
            self.sEntrada4Txt.setText('')

        if self.sPila4Txt.text() not in self.automataP.alfabetoPila:
            correcto = False
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Advertencia")
            msg.setText("El símbolo de la pila es incorrecto")
            msg.exec_()
            self.sPila4Txt.setText('')

        if self.destino4Txt.text().lower() not in self.automataP.estados:
            correcto = False
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Advertencia")
            msg.setText("El destino es incorrecto")
            msg.exec_()
            self.destino4Txt.setText('')

        if self.simboloEscribirP4Txt.text() not in self.automataP.alfabetoPila and self.simboloEscribirP4Txt.text()!='E':
            correcto = False
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Advertencia")
            msg.setText("El simbolo a escribir en la pila es incorrecto")
            msg.exec_()
            self.simboloEscribirP4Txt.setText('')

        if correcto:
            #Se agrega la transicion al automataP, en el estado correspondiente
            comp1=self.sEntrada4Txt.text()+","+self.sPila4Txt.text()
            comp2=[self.automataP.estados[self.destino4Txt.text().lower()],self.simboloEscribirP4Txt.text()]

            self.automataP.estados[self.origen4Txt.text().lower()].agregarTransicion(comp1,comp2)

            #Se agrega la transicion al combobox
            self.cBoxTransiciones4_.addItem("δ( "+self.origen4Txt.text().lower()+","+self.sEntrada4Txt.text()+","+self.sPila4Txt.text()
                                            +" ) = "+ self.destino4Txt.text().lower()+","+self.simboloEscribirP4Txt.text())

            self.origen4Txt.setText('')
            self.sEntrada4Txt.setText('')
            self.sPila4Txt.setText('')
            self.destino4Txt.setText('')
            self.simboloEscribirP4Txt.setText('')


    #ARCHIVOS
    def cargarAutomata(self):
        fname = QFileDialog.getOpenFileName(self,caption="Abrir Archivo",directory='../Automatas/')#captio:nombre ventana; filter: extension que le quiero poner al archivo
        if fname[0]:#En la posicion cero esta la ruta del archivo, en la posicion 1 el tipo de archivo
            automataPref= open(fname[0],'rb')#se define la variable en la que se guardara el archivo, rb(read binary)

            try:
                self.limpiar2_1()
                self.automata= pickle.load(automataPref)#se carga el automataPref
                self.dibujarAutomataLogico(self.automata,self.graphicsView_2)


            except Exception as e:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Advertencia")
                msg.setText("Ocurrió un error, tal vez no selecciono el archivo:"+str(e))
                msg.exec_()

    def guardarAutomata(self):
        fname=QFileDialog.getSaveFileName(self,caption="Guardar Archivo",directory='../Automatas/')

        if fname[0]:
            try:
                pickle.dump(self.automata,open(fname[0],"wb"))
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Advertencia")
                msg.setText("Archivo guardado con éxito")
                msg.exec_()


            except Exception as e:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Advertencia")
                msg.setText("Error: "+e)
                msg.exec_()

    def guardarGramatica(self, gramatica):
        fname = QFileDialog.getSaveFileName(self, caption="Guardar Archivo", directory='../Gramaticas/')

        if fname[0]:
            try:
                pickle.dump(gramatica, open(fname[0], "wb"))
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Advertencia")
                msg.setText("Archivo guardado con éxito")
                msg.exec_()


            except Exception as e:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Advertencia")
                msg.setText("Error: " + e)
                msg.exec_()

