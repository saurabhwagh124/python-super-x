import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget


class ConfirmOrderWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Where's My Water?")
        self.setGeometry(350,150,1200,800)
        self.submit_button = QPushButton("Submit")

    def get_confirm_order_ui(self):

        confirmation_window = QFormLayout()
        #creating labels 
        con_quantity = QLabel("Quantity of water needed: ")
        con_name =  QLabel("Name: ")
        con_phone = QLabel("Phone no.: ")
        con_address = QLabel("Address: ")
        con_date  = QLabel("Select Date: ")
        con_time = QLabel("Select Time: ")

        # settind font size and style
        con_quantity.setFont(QFont('Arial',12 )) 
        con_name.setFont(QFont('Arial',12 )) 
        con_phone.setFont(QFont('Arial',12 )) 
        con_address.setFont(QFont('Arial',12 )) 
        con_date.setFont(QFont('Arial',12 )) 
        con_time.setFont(QFont('Arial',12 )) 

         #creating buttons  
        
        self.submit_button.setStyleSheet("QPushButton::hover"
                     "{"
                     "background-color : lightgreen;border-radius: 10px ;border-style: outset;"
                     "}"
                     "QPushButton"
                             "{"
                             "background-color :lightyellow;border-radius: 10px ;border-style: outset;"
                             "}")
      
        self.submit_button.setFixedSize(100,50)
        self.submit_button.setFont(QFont('Arial', 15))
        submit_box = QVBoxLayout()
        submit_box.addWidget(self.submit_button)
        submit_box.setAlignment(Qt.AlignCenter)
        self.submit_button.move(60, -100)
        # self.submit_button.clicked.connect(self.passingInformation)
        confirmation_window.addWidget(self.submit_button)
        

       

        #creating line edits
        self.con_quantity_line  = QLineEdit()
        self.con_quantity_line.setPlaceholderText("Enter the quantity of water")
        self.con_quantity_line.setFont(QFont('Arial',11))

        self.con_name_line = QLineEdit()
        self.con_name_line.setPlaceholderText("Enter your name")
        self.con_name_line.setFont(QFont('Arial',11))

        self.con_phone_line = QLineEdit()
        self.con_phone_line.setPlaceholderText("Enter your phone no.")
        self.con_phone_line.setMaxLength(10)
        self.con_phone_line.setFont(QFont('Arial',11))

        self.con_address_line = QLineEdit()
        self.con_address_line.setPlaceholderText("Enter your address")
        self.con_address_line.setFont(QFont('Arial',11))


         #setting fixed sized of textbox

        self.con_quantity_line.setFixedSize(300,40)
        self.con_name_line.setFixedSize(300,40)
        self.con_phone_line.setFixedSize(300,40)
        self.con_address_line.setFixedSize(300,40)

        #curves

        self.con_quantity_line.setStyleSheet("border :1px solid cyan;"
                                   "border-top-left-radius :15px;"
                                   " border-top-right-radius : 15px; "
                                   "border-bottom-left-radius : 15px; "
                                   "border-bottom-right-radius : 15px") 
        self.con_name_line.setStyleSheet("border :1px solid cyan;"
                                   "border-top-left-radius :15px;"
                                   " border-top-right-radius : 15px; "
                                   "border-bottom-left-radius : 15px; "
                                   "border-bottom-right-radius : 15px") 
        self.con_phone_line.setStyleSheet("border :1px solid cyan;"
                                   "border-top-left-radius :15px;"
                                   " border-top-right-radius : 15px; "
                                   "border-bottom-left-radius : 15px; "
                                   "border-bottom-right-radius : 15px") 
        self.con_address_line.setStyleSheet("border :1px solid cyan;"
                                   "border-top-left-radius :15px;"
                                   " border-top-right-radius : 15px; "
                                   "border-bottom-left-radius : 15px; "
                                   "border-bottom-right-radius : 15px") 
        
        


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
        self.con_calender = QDateEdit()
        self.con_calender.setGeometry(100,100,500,100)
        set_date = QDate.currentDate()
        self.con_calender.setDate(set_date)
        self.con_calender.setFont(QFont('Arial',11))

        #time widget
        self.con_clock = QTimeEdit()
        self.con_clock.setGeometry(100,100,500,100)
        set_time = QTime.currentTime()
        self.con_clock.setTime(set_time)
        self.con_clock.setFont(QFont('Arial',11))

        #adding elements into boxes
        quantity_box.addWidget(con_quantity)
        quantity_box.addWidget(self.con_quantity_line)


        name_box.addWidget(con_name)
        name_box.addWidget(self.con_name_line)
        
        phone_box.addWidget(con_phone)
        phone_box.addWidget(self.con_phone_line)
        
        address_box.addWidget(con_address)
        address_box.addWidget(self.con_address_line)
        
        date_box.addWidget(con_date)
        date_box.addWidget(self.con_calender)
        
        time_box.addWidget(con_time)
        time_box.addWidget(self.con_clock)

        #adding elements to the layout
        confirmation_window.addRow(quantity_box)
        confirmation_window.addRow(name_box)
        confirmation_window.addRow(phone_box)
        confirmation_window.addRow(address_box)
        confirmation_window.addRow(date_box)
        confirmation_window.addRow(time_box)
        confirmation_window.addRow(submit_box)
        
        
        return confirmation_window

