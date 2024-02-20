import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QPushButton, QWidget, QLabel
from PyQt5.QtCore import Qt

class TankerDrinkingWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Where's my Water")
        self.setGeometry(350,150,1200,800)
        
    def get_tanker_drinking_ui(self):
        tanker_drinking_layout = QVBoxLayout()

        tanker_button = QPushButton("Need a Tanker ?")
        drinking_button = QPushButton("Need Drinking Water ?")

        tanker_button.setStyleSheet("QPushButton::hover"
                     "{"
                     "background-color : lightgreen;border-radius: 10px ;border-style: outset;"
                     "}"
                     "QPushButton"
                             "{"
                             "background-color : lightblue;border-radius: 10px ;border-style: outset;"
                             "}")
        
        drinking_button.setStyleSheet("QPushButton::hover"
                     "{"
                     "background-color : lightgreen;border-radius: 10px ;border-style: outset;"
                     "}"
                     "QPushButton"
                             "{"
                             "background-color : lightblue;border-radius: 10px ;border-style: outset;"
                             "}")

        tanker_button.setFixedSize(220,60)
        drinking_button.setFixedSize(220,60)

        font = tanker_button.font()
        font.setPointSize(12)  
        tanker_button.setFont(font)

        font = drinking_button.font()
        font.setPointSize(12)  
        drinking_button.setFont(font)

        or_text = QLabel("Or" , self)
        
        tanker_drinking_layout.setAlignment(Qt.AlignCenter)
        or_text.setAlignment(Qt.AlignCenter)
        or_text.setStyleSheet("font-size: 20px;")

        tanker_drinking_layout.addWidget(tanker_button)
        tanker_drinking_layout.addWidget(or_text)
        tanker_drinking_layout.addWidget(drinking_button)

        return tanker_drinking_layout
