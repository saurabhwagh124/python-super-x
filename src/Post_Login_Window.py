import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QPushButton, QWidget, QLabel,QGraphicsOpacityEffect

from PyQt5.QtCore import Qt


CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Where's my Water")
        self.setGeometry(350,150,1200,800)

        oImage = QtGui.QImage(os.path.join(CURRENT_DIR, "water.jpg"))
        sImage = oImage.scaled(QtCore.QSize(1200, 800))
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Window, QtGui.QBrush(sImage))
        self.setPalette(palette)

        

        layout = QVBoxLayout()
        # layout.addWidget(QPushButton("Need a Tanker ?"))
        # layout.addWidget(QPushButton("Need Drinking Water ?"))

        button1 = QPushButton("Need a Tanker ?")
        button2 = QPushButton("Need Drinking Water ?")

        button1.setFixedSize(300, 80)
        button2.setFixedSize(300, 80)

        font = button1.font()
        font.setPointSize(16)  
        button1.setFont(font)

        

        font = button2.font()
        font.setPointSize(16)  
        button2.setFont(font)

        text = QLabel("Or" , self)
        

        layout.setAlignment(Qt.AlignCenter)
        text.setAlignment(Qt.AlignCenter)
        text.setStyleSheet("font-size: 24px;")

        layout.addWidget(button1)
        layout.addWidget(text)
        layout.addWidget(button2)

        self.setLayout(layout)
        print(self.children())

        
        opacity_effect1 = QGraphicsOpacityEffect(button1)
        opacity_effect2 = QGraphicsOpacityEffect(button2)

        opacity_effect1.setOpacity(0.7) 
        opacity_effect2.setOpacity(0.7) 

        button1.setGraphicsEffect(opacity_effect1)
        button2.setGraphicsEffect(opacity_effect2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())