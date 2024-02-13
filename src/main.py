import sys 
from PyQt5.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        
        self.setWindowTitle("Helen Of Troy")
        self.setGeometry(350,150,1200,800)
        # geometry(align left, align top, width, height)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

