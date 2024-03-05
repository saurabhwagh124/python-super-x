import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt,QSize
from PyQt5.QtWidgets import QWidget

class LocationWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Location window")
        self.setGeometry(350,150,1200,800)
        self.saurab_water_button = QPushButton("Order")
        self.saurab_water_button.setStyleSheet("QPushButton::hover"
                     "{"
                     "background-color : lightgreen;border-radius: 10px ;border-style: outset;"
                     "}"
                     "QPushButton"
                             "{"
                             "background-color : lightyellow;border-radius: 10px ;border-style: outset;"
                             "}")
        self.saurab_water_button.setFont(QFont('Arial', 15))
        self.nachiket_water_button = QPushButton("Order")
        self.nachiket_water_button.setStyleSheet("QPushButton::hover"
                     "{"
                     "background-color : lightgreen;border-radius: 10px ;border-style: outset;"
                     "}"
                     "QPushButton"
                             "{"
                             "background-color :lightyellow;border-radius: 10px ;border-style: outset;"
                             "}")
        self.nachiket_water_button.setFont(QFont('Arial', 15))
        self.aditya_water_button = QPushButton("Order")
        self.aditya_water_button.setStyleSheet("QPushButton::hover"
                     "{"
                     "background-color : lightgreen;border-radius: 10px ;border-style: outset;"
                     "}"
                     "QPushButton"
                             "{"
                             "background-color :lightyellow;border-radius: 10px ;border-style: outset;"
                             "}")
        self.aditya_water_button.setFont(QFont('Arial', 15))
        self.submit_button = QPushButton("Submit")
        self.submit_button.setStyleSheet("QPushButton::hover"
                     "{"
                     "background-color : lightgreen;border-radius: 10px ;border-style: outset;"
                     "}"
                     "QPushButton"
                             "{"
                             "background-color :lightyellow;border-radius: 10px ;border-style: outset;"
                             "}")
        self.submit_button.setFont(QFont('Arial', 15))

    def LocationWindow_Ui(self):
        
        Location_window = QFormLayout()

        #creating labels
        location_label = QLabel("Location : ")
        water_provider1 = QLabel("1.Saurabh water suppliers")
        water_provider2 = QLabel("2.Nachiket Water provider")
        water_provider3 = QLabel("3.Aditya Waters")

        location_label.setFont(QFont('Arial',14))
        water_provider1.setFont(QFont('Arial',14))
        water_provider2.setFont(QFont('Arial',14))
        water_provider3.setFont(QFont('Arial',14))

        
        #adding textarea   ########
        self.location_line = QLineEdit()
        self.location_line.setPlaceholderText("Enter your location")
        self.location_line.setFixedSize(300,40)
        self.location_line.setGeometry(0,0,200,60)
        self.location_line.setStyleSheet("border :1px solid cyan;"
                                   "border-top-left-radius :15px;"
                                   " border-top-right-radius : 15px; "
                                   "border-bottom-left-radius : 15px; "
                                   "border-bottom-right-radius : 15px") 
        self.location_line.setFont(QFont('Arial',14))
        #adding button
        
        self.submit_button.setFixedSize(100,40)

        
        
        self.saurab_water_button.setFixedSize(100,40)
        self.nachiket_water_button.setFixedSize(100,40)
        self.aditya_water_button.setFixedSize(100,40)
        #creating boxes
        location_box = QHBoxLayout()
        location_box.setContentsMargins(300,250,300,0)
        saurabh_water_box = QHBoxLayout()
        saurabh_water_box.setContentsMargins(300,50,300,0)
        nachiket_water_box = QHBoxLayout()
        nachiket_water_box.setContentsMargins(300,25,300,0)
        aditya_water_box = QHBoxLayout()
        aditya_water_box.setContentsMargins(300,25,300,0)



        #adding element in the box
        location_box.addWidget(location_label)
        location_box.addWidget(self.location_line)
        location_box.addWidget(self.submit_button)
        
        saurabh_water_box.addWidget(water_provider1)
        saurabh_water_box.addWidget(self.saurab_water_button)

        nachiket_water_box.addWidget(water_provider2)
        nachiket_water_box.addWidget(self.nachiket_water_button)
        
        aditya_water_box.addWidget(water_provider3)
        aditya_water_box.addWidget(self.aditya_water_button)



        #adding layout
        Location_window.addRow(location_box)
        Location_window.addRow(saurabh_water_box)
        Location_window.addRow(nachiket_water_box)
        Location_window.addRow(aditya_water_box)

        return Location_window
        





        




