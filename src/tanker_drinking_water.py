import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QPushButton, QWidget, QLabel
from PyQt5.QtCore import Qt

class TankerDrinkingWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Where's my Water")
        self.setGeometry(350,150,1200,800)
        self.tanker_button= QPushButton("Need a Tanker ?")
        self.drinking_button = QPushButton("Need Drinking Water ?")
        
    def get_tanker_drinking_ui(self):
        tanker_drinking_layout = QVBoxLayout()

        

        self.tanker_button.setStyleSheet("QPushButton::hover"
                     "{"
                     "background-color : lightgreen;border-radius: 10px ;border-style: outset;"
                     "}"
                     "QPushButton"
                             "{"
                             "background-color : lightyellow;border-radius: 10px ;border-style: outset;"
                             "}")
        
        self.drinking_button.setStyleSheet("QPushButton::hover"
                     "{"
                     "background-color : lightgreen;border-radius: 10px ;border-style: outset;"
                     "}"
                     "QPushButton"
                             "{"
                             "background-color : lightyellow;border-radius: 10px ;border-style: outset;"
                             "}")

        self.tanker_button.setFixedSize(220,60)
        self.drinking_button.setFixedSize(220,60)

        font = self.tanker_button.font()
        font.setPointSize(12)  
        self.tanker_button.setFont(font)

        font = self.drinking_button.font()
        font.setPointSize(12)  
        self.drinking_button.setFont(font)

        or_text = QLabel("Or" , self)
        
        tanker_drinking_layout.setAlignment(Qt.AlignCenter)
        or_text.setAlignment(Qt.AlignCenter)
        or_text.setStyleSheet("font-size: 20px;")

        tanker_drinking_layout.addWidget(self.tanker_button)
        tanker_drinking_layout.addWidget(or_text)
        tanker_drinking_layout.addWidget(self.drinking_button)

        return tanker_drinking_layout
