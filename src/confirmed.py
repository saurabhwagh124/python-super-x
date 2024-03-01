import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt,QSize
from PyQt5.QtWidgets import QWidget

from Home import get_order_details

class confirmedDetails(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("confirmed Details")
        self.setGeometry(350,150,1200,800)
         
        # setting  the fixed width of window
        self.str_water = "Water"
        self.str_quantity=" sample quantity"
        self.str_name=" sample time"
        self.str_phone=" sample phone"
        self.str_address=" sample address"
        self.str_date=" sample date"
        self.str_time= " sample time"
        self.str_supplier = "sample supplier"

        self.logout_button = QPushButton("LogOut")
    
        
        

    def display_ticket(self,x):
        self.confirmed_window=QGridLayout()
        self.name = x

        value_return = get_order_details(self.name)
        self.str_water = value_return['water']
        self.str_quantity = value_return['quantity']
        self.str_name = value_return['name']
        self.str_phone = value_return['phone']
        self.str_address = value_return['address']
        self.str_date = value_return['date']
        self.str_time = value_return['time']
        self.str_supplier = value_return['supplier']

        # creating labels
        self.conf_water_label = QLabel("Water: ")
        self.conf_quantity_label = QLabel("Quantity of water needed: ")
        self.conf_name_label =  QLabel("Name: ")
        self.conf_phone_label = QLabel("Phone no.: ")
        self.conf_address_label = QLabel("Address: ")
        self.conf_date_label  = QLabel("Date: ")
        self.conf_time_label = QLabel("Time: ") 
        self.conf_supplier_label = QLabel("Supplier:")

        # creating LineEdits
        self.conf_water_line = QLabel(self.str_water)
        self.conf_quantity_line = QLabel(self.str_quantity)
        self.conf_name_line = QLabel(self.str_name)
        self.conf_phone_line = QLabel(self.str_phone)
        self.conf_address_line = QLabel(self.str_address)
        self.conf_date_line = QLabel(self.str_date)
        self.conf_time_line = QLabel(self.str_time)
        self.conf_supplier_line =QLabel(self.str_supplier)
       

        
         #changing font size 
        self.conf_water_label.setFont(QFont('Arial',12))
        self.conf_quantity_label.setFont(QFont('Arial',12 )) 
        self.conf_name_label.setFont(QFont('Arial',12 ))
        self.conf_phone_label.setFont(QFont('Arial',12 ))
        self.conf_address_label.setFont(QFont('Arial',12 ))
        self.conf_date_label.setFont(QFont('Arial',12 ))
        self.conf_time_label.setFont(QFont('Arial',12 ))
        self.conf_supplier_label.setFont(QFont('Arial',12))



        self.conf_water_line = QLabel(self.str_water)
        self.conf_quantity_line = QLabel(self.str_quantity)
        self.conf_name_line = QLabel(self.str_name)
        self.conf_phone_line = QLabel(self.str_phone)
        self.conf_address_line = QLabel(self.str_address)
        self.conf_date_line = QLabel(self.str_date)
        self.conf_time_line = QLabel(self.str_time)
        self.conf_supplier_line = QLabel(self.str_supplier)


        #fontsizeself.
        self.conf_water_line.setFont(QFont('Arial',12))
        self.conf_quantity_line.setFont(QFont('Arial',12))
        self.conf_name_line.setFont(QFont('Arial',12))
        self.conf_phone_line.setFont(QFont('Arial',12))
        self.conf_address_line.setFont(QFont('Arial',12))
        self.conf_date_line.setFont(QFont('Arial',12))
        self.conf_time_line.setFont(QFont('Arial',12))
        self.conf_supplier_line.setFont(QFont('Arial',12))



        self.logout_button.setFont(QFont('Arial',12))
        
        
        blank_label = QLabel("")
        #adding elements to form layout
        
        self.confirmed_window.addWidget(self.conf_water_label,0,0)
        self.confirmed_window.addWidget(self.conf_water_line,0,1)
        self.confirmed_window.addWidget(self.conf_quantity_label,1,0)
        self.confirmed_window.addWidget(self.conf_quantity_line,1,1)
        self.confirmed_window.addWidget(self.conf_name_label,2,0)
        self.confirmed_window.addWidget(self.conf_name_line,2,1)
        self.confirmed_window.addWidget(self.conf_phone_label,3,0)
        self.confirmed_window.addWidget(self.conf_phone_line,3,1)
        self.confirmed_window.addWidget(self.conf_address_label,4,0)
        self.confirmed_window.addWidget(self.conf_address_line,4,1)
        self.confirmed_window.addWidget(self.conf_date_label,5,0)
        self.confirmed_window.addWidget(self.conf_date_line,5,1)
        self.confirmed_window.addWidget(self.conf_time_label,6,0)
        self.confirmed_window.addWidget(self.conf_time_line,6,1)
        self.confirmed_window.addWidget(self.conf_supplier_label,7,0)
        self.confirmed_window.addWidget(self.conf_supplier_line,7,1)
        self.confirmed_window.addWidget(blank_label,8,0)
        self.confirmed_window.addWidget(self.logout_button,9,0)
        self.confirmed_window.setAlignment(Qt.AlignCenter)

        return self.confirmed_window 

       

     
            








        