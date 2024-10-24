import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)
        button.setCheckable(True)

    def button_clicked(self, checked):
        print("hola", checked)
        
        dlg = QDialog(self)
        dlg.setWindowTitle("Galeano feo")
        dlg.exec()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()