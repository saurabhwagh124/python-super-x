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
        self.str_quantity=" sample quantity"
        self.str_name=" sample time"
        self.str_phone=" sample phone"
        self.str_address=" sample address"
        self.str_date=" sample date"
        self.str_time= " sample time"
        self.str_supplier = "sample supplier"
    
        
        

    def display_ticket(self,x):
        self.confirmed_window=QFormLayout()
        self.name = x

        value_return = get_order_details(self.name)
        self.str_quantity = value_return['quantity']
        self.str_name = value_return['name']
        self.str_phone = value_return['phone']
        self.str_address = value_return['address']
        self.str_date = value_return['date']
        self.str_time = value_return['time']
        self.str_supplier = value_return['supplier']

        # creating labels
        self.conf_quantity_label = QLabel("Quantity of water needed: ")
        self.conf_name_label =  QLabel("                       Name: ")
        self.conf_phone_label = QLabel("                  Phone no.: ")
        self.conf_address_label = QLabel("                  Address: ")
        self.conf_date_label  = QLabel("                       Date: ")
        self.conf_time_label = QLabel("                        Time: ") 
        self.conf_supplier_label = QLabel("                 Supplier:")

        # creating LineEdits
        self.conf_quantity_line = QLabel(self.str_quantity)
        self.conf_quantity_line.setContentsMargins(100,0,500,0)
        self.conf_name_line = QLabel(self.str_name)
        self.conf_name_line.setContentsMargins(100,0,500,0)
        self.conf_phone_line = QLabel(self.str_phone)
        self.conf_phone_line.setContentsMargins(100,0,500,0)
        self.conf_address_line = QLabel(self.str_address)
        self.conf_address_line.setContentsMargins(100,0,500,0)
        self.conf_date_line = QLabel(self.str_date)
        self.conf_date_line.setContentsMargins(100,0,500,0)
        self.conf_time_line = QLabel(self.str_time)
        self.conf_time_line.setContentsMargins(100,0,500,0)
        self.conf_supplier_line =QLabel(self.str_supplier)
        self.conf_supplier_line.setContentsMargins(100,0,500,0)
       

        
         #changing font size 

        self.conf_quantity_label.setFont(QFont('Arial',12 )) 
        self.conf_name_label.setFont(QFont('Arial',12 ))
        self.conf_phone_label.setFont(QFont('Arial',12 ))
        self.conf_address_label.setFont(QFont('Arial',12 ))
        self.conf_date_label.setFont(QFont('Arial',12 ))
        self.conf_time_label.setFont(QFont('Arial',12 ))
        self.conf_supplier_label.setFont(QFont('Arial',12))


        self.conf_quantity_line = QLabel(self.str_quantity)
        self.conf_name_line = QLabel(self.str_name)
        self.conf_phone_line = QLabel(self.str_phone)
        self.conf_address_line = QLabel(self.str_address)
        self.conf_date_line = QLabel(self.str_date)
        self.conf_time_line = QLabel(self.str_time)
        self.conf_supplier_line = QLabel(self.str_supplier)


        self.confirmed_window.addWidget(self.conf_quantity_line)
        self.confirmed_window.addWidget(self.conf_name_line)
        self.confirmed_window.addWidget(self.conf_phone_line)
        self.confirmed_window.addWidget(self.conf_address_line)
        self.confirmed_window.addWidget(self.conf_date_line)
        self.confirmed_window.addWidget(self.conf_time_line)
        self.confirmed_window.addWidget(self.conf_supplier_line)



        #fontsizeself.

        self.conf_quantity_line.setFont(QFont('Arial',12))
        self.conf_name_line.setFont(QFont('Arial',12))
        self.conf_phone_line.setFont(QFont('Arial',12))
        self.conf_address_line.setFont(QFont('Arial',12))
        self.conf_date_line.setFont(QFont('Arial',12))
        self.conf_time_line.setFont(QFont('Arial',12))
        self.conf_supplier_line.setFont(QFont('Arial',12))


        #creating boxes

        self.conf_quantity_box =QHBoxLayout()
        self.conf_quantity_box.setAlignment(Qt.AlignCenter)

        self.conf_name_box=QHBoxLayout()
        self.conf_name_box.setAlignment(Qt.AlignCenter)

        self.conf_phone_box=QHBoxLayout()
        self.conf_phone_box.setAlignment(Qt.AlignCenter)

        self.conf_address_box=QHBoxLayout()
        self.conf_address_box.setAlignment(Qt.AlignCenter)

        self.conf_date_box=QHBoxLayout()
        self.conf_date_box.setAlignment(Qt.AlignCenter)

        self.conf_time_box=QHBoxLayout()
        self.conf_time_box.setAlignment(Qt.AlignCenter)

        self.conf_supplier_box = QHBoxLayout()
        self.conf_supplier_box.setAlignment(Qt.AlignCenter)
        
        
        #adding element in the hbox

        self.conf_quantity_box.addWidget(self.conf_quantity_label)
        self.conf_quantity_box.addWidget(self.conf_quantity_line)

        self.conf_name_box.addWidget(self.conf_name_label)
        self.conf_name_box.addWidget(self.conf_name_line)

        self.conf_phone_box.addWidget(self.conf_phone_label)
        self.conf_phone_box.addWidget(self.conf_phone_line)

        self.conf_address_box.addWidget(self.conf_address_label)
        self.conf_address_box.addWidget(self.conf_address_line)

        self.conf_date_box.addWidget(self.conf_date_label)
        self.conf_date_box.addWidget(self.conf_date_line)

        self.conf_time_box.addWidget(self.conf_time_label)
        self.conf_time_box.addWidget(self.conf_time_line)

        self.conf_supplier_box.addWidget(self.conf_supplier_label)
        self.conf_supplier_box.addWidget(self.conf_supplier_line)
         #adding elements to form layout

        self.confirmed_window.addRow(self.conf_quantity_box)
        self.confirmed_window.addRow(self.conf_name_box)
        self.confirmed_window.addRow(self.conf_phone_box)
        self.confirmed_window.addRow(self.conf_address_box)
        self.confirmed_window.addRow(self.conf_date_box)
        self.confirmed_window.addRow(self.conf_time_box)
        self.confirmed_window.addRow(self.conf_supplier_box)
        self.confirmed_window.setAlignment(Qt.AlignCenter)

        return self.confirmed_window 

       

     
            








        