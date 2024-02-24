import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt,QSize
from PyQt5.QtWidgets import QWidget

from Home import get_suppliers_orders


class SupplierOrders(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Where's my water")
        self.setGeometry(350,150,1200,800)
        self.next_button = QPushButton("Next")
        self.next_button.setFixedSize(100,50)
        self.next_button.setStyleSheet("QPushButton::hover"
                     "{"
                     "background-color : lightgreen;border-radius: 10px ;border-style: outset;"
                     "}"
                     "QPushButton"
                             "{"
                             "background-color : lightyellow;border-radius: 10px ;border-style: outset;"
                             "}")
        self.next_button.setFont(QFont('Arial', 15))
        self.name = "xyz"
        self.no = "123"
        self.address = "Abc"
        self.quantity = "50"
        self.date = "01/12/2004"
        self.time = "2:30 pm"
        self.index = 0


    def get_supplier_orders_ui(self):
        self.orders_layout = QGridLayout()

        self.const_name = QLabel("Name: ")
        self.const_name.setFont(QFont('Arial',12 ))
        self.const_phone = QLabel("Phone: ")
        self.const_phone.setFont(QFont('Arial',12 ))
        self.const_address = QLabel("Address: ")
        self.const_address.setFont(QFont('Arial',12 ))
        self.const_quantity = QLabel("Quantity")
        self.const_quantity.setFont(QFont('Arial',12 ))
        self.const_date = QLabel("Date: ")
        self.const_date.setFont(QFont('Arial',12 ))
        self.const_time = QLabel("Time: ")
        self.const_time.setFont(QFont('Arial',12 ))

        order_bundles = get_suppliers_orders()
        # self.quantity = order_bundles[self.index]['quantity']
        # self.name = order_bundles[self.index]['name']
        # self.no = order_bundles[self.index]['phone']
        # self.address = order_bundles[self.index]['address']
        # self.date = order_bundles[self.index]['date']
        # self.time = order_bundles[self.index]['times']


        self.get_name = QLabel(self.name)
        self.get_no = QLabel(self.no)
        self.get_address = QLabel(self.address)
        self.get_quantity = QLabel(self.quantity)
        self.get_date = QLabel(self.date)
        self.get_time = QLabel(self.time)

        self.get_name.setFont(QFont('Arial',12 ))
        self.get_no.setFont(QFont('Arial',12 ))
        self.get_address.setFont(QFont('Arial',12 ))
        self.get_quantity.setFont(QFont('Arial',12 ))
        self.get_date.setFont(QFont('Arial',12 ))
        self.get_time.setFont(QFont('Arial',12 ))
        
        
        


        self.orders_layout.addWidget(self.const_name,0,0)
        self.orders_layout.addWidget(self.get_name,0,1)
        self.orders_layout.addWidget(self.const_phone,1,0)
        self.orders_layout.addWidget(self.get_no,1,1)
        self.orders_layout.addWidget(self.const_address,2,0)
        self.orders_layout.addWidget(self.get_address,2,1)
        self.orders_layout.addWidget(self.const_quantity,3,0)
        self.orders_layout.addWidget(self.get_quantity,3,1)
        self.orders_layout.addWidget(self.const_date,4,0)
        self.orders_layout.addWidget(self.get_date,4,1)
        self.orders_layout.addWidget(self.const_time,5,0)
        self.orders_layout.addWidget(self.get_time,5,1)
        self.orders_layout.addWidget(self.next_button)
        self.orders_layout.setAlignment(Qt.AlignCenter)

        return self.orders_layout


