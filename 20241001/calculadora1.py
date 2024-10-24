import sys
from PyQt6.QtWidgets import QApplication, QGridLayout, QLineEdit, QLabel, QWidget, QPushButton, QMainWindow

class calculadora(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calcu")
        self.setGeometry(500,500,500,500)

        self.resultado = QLineEdit()
        layout = QGridLayout()
        layout.addWidget(self.resultado,0,0,1,4)
        nombre_boton = [["1", "2", "3", "+"],
                       ["4", "5", "6", "-"],
                       ["7", "8", "9", "*"],
                       ["0", "/", "C", "."]]
        

        #añadir componentes
        for i in range (1,5):
            for j in range(4):
                print (i,j)
                boton = QPushButton(nombre_boton [i-1][j])
                boton.clicked.connect(self.press_button)
                layout.addWidget(boton,i,j)

        boton = QPushButton("=")
        boton.clicked.connect(self.press_button)
        layout.addWidget(boton,5,0,1,4)       

        self.setLayout(layout)


    
    def press_button(self):
        sender = self.sender()
        if (sender.text() == "="):
            self.resultado.setText(str(eval(self.resultado.text())))
        else:
            self.resultado.setText(self.resultado.text() + sender.text())
        if (sender.text() == "C"):
            self.resultado.setText (" ")
        else:
            self.resultado.setText(self.resultado.text())


if __name__ == "__main__":

    app = QApplication(sys.argv)
    calc = calculadora()
    calc.show()
    sys.exit(app.exec())
