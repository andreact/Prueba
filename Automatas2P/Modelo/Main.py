import sys
from PyQt5.QtWidgets import QApplication
from Vista.GUI import VentanaP

if __name__ == '__main__':

    app=QApplication(sys.argv)
    ventana=VentanaP()
    ventana.show()
    sys.exit(app.exec_())