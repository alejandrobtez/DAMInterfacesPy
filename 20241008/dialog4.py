
import sys

from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QPushButton, QVBoxLayout, QLabel, QDialogButtonBox

class CustomDialog(QDialog):
    def __init__(self,isColor):
        super().__init__()

        self.setWindowTitle("HELLO!")
        
        QBtn = (
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.alerta)

        layout = QVBoxLayout()
        message = QLabel("Something happened, is that OK?")
        message.setObjectName('nom_plan_label')
        if (isColor):
            message.setStyleSheet('QLabel#nom_plan_label {color: red}')
        else:   
            message.setStyleSheet('QLabel#nom_plan_label {color: blue}')
        layout.addWidget(message)
        layout.addWidget (self.buttonBox)
        self.setLayout(layout)

    def alerta (self):
        QMessageBox.warning(self, "Cancel", "Cancelado")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.setCheckable (True)
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, s):

        dlg = CustomDialog(s)
        dlg.exec()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()