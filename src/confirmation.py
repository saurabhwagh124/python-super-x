import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

class ConfirmationWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Where's My Water?")
        self.setGeometry(350,150,1200,800)
        self.get_confirmation_ui()

        oImage = QtGui.QImage(os.path.join(CURRENT_DIR, "water.jpg"))
        sImage = oImage.scaled(QtCore.QSize(1200, 800))
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Window, QtGui.QBrush(sImage))
        self.setPalette(palette)

    def get_confirmation_ui(self):

        confirmation_window = QFormLayout()

        #creating labels 
        con_quantity = QLabel("Quantity of water needed: ")
        con_name =  QLabel("Name: ")
        con_phone = QLabel("Phone no.: ")
        con_address = QLabel("Address: ")
        con_date  = QLabel("Select Date: ")
        con_time = QLabel("Select Time: ")

        #creating buttons
        con_submit = QLabel("Submit")

        #creating line edits
        con_quantity_line  = QLineEdit()
        con_name_line = QLineEdit()
        con_phone_line = QLineEdit()
        con_phone_line.setMaxLength(10)
        con_address_line = QLineEdit()

        #creating boxes
        quantity_box = QHBoxLayout()
        quantity_box.setAlignment(Qt.AlignCenter)
        quantity_box.setContentsMargins(250,50,250,0)
        name_box = QHBoxLayout()
        name_box.setAlignment(Qt.AlignCenter)
        name_box.setContentsMargins(250,0,250,0)
        phone_box = QHBoxLayout()
        phone_box.setAlignment(Qt.AlignCenter)
        phone_box.setContentsMargins(250,0,250,0)
        address_box = QHBoxLayout()
        address_box.setContentsMargins(250,0,250,0)
        address_box.setAlignment(Qt.AlignCenter)
        date_box = QHBoxLayout()
        date_box.setAlignment(Qt.AlignCenter)
        date_box.setContentsMargins(250,0,250,0)
        time_box = QHBoxLayout()
        time_box.setAlignment(Qt.AlignCenter)
        time_box.setContentsMargins(250,0,250,0)

        # calendar widget
        con_calender = QCalendarWidget()
        con_calender.setGeometry(0,0,100,100)
        #adding elements into boxes
        quantity_box.addWidget(con_quantity)
        quantity_box.addWidget(con_quantity_line)


        name_box.addWidget(con_name)
        name_box.addWidget(con_name_line)
        
        phone_box.addWidget(con_phone)
        phone_box.addWidget(con_phone_line)
        
        address_box.addWidget(con_address)
        address_box.addWidget(con_address_line)
        
        date_box.addWidget(con_date)
        date_box.addWidget(con_calender)
        
        time_box.addWidget(con_time)

        #adding elements to the layout
        confirmation_window.addRow(quantity_box)
        confirmation_window.addRow(name_box)
        confirmation_window.addRow(phone_box)
        confirmation_window.addRow(address_box)
        confirmation_window.addRow(date_box)
        confirmation_window.addRow(time_box)
        
        
        self.setLayout(confirmation_window)

app = QApplication(sys.argv)
ex = ConfirmationWindow()
ex.show()
sys.exit(app.exec_())
