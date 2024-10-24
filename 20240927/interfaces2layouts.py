import sys
from PyQt6.QtWidgets import QApplication, QHBoxLayout, QLabel, QLineEdit, QMainWindow, QWidget
from PyQt6.QtGui import QPalette, QColor

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)
        self.setFixedHeight(100,100)

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("App Alejandro")

        layout = QHBoxLayout()

        layout.addWidget(QLineEdit("QLineEdit 1"))
        layout.addWidget(QLineEdit('QLineEdit 2'))
        layout.addWidget(QLabel('QLabel'))
        layout.addWidget(Color('red'))
        layout.addWidget(Color('yellow'))
        layout.addWidget(Color('red'))

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()