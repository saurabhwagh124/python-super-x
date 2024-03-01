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
        self.xlength = 0
        self.water = 'water'
        self.name = "xxx"
        self.no = "xxx"
        self.address = "xxx"
        self.quantity = "xxx"
        self.date = "xxx"
        self.time = "xxx"
        self.supplier_u_name = ''
        self.index = 0

    def get_supplier_orders_ui(self,supplier_u_name,index,in_length=0):
        self.orders_layout = QGridLayout()
        self.supplier_u_name = supplier_u_name
        self.order_bundles = get_suppliers_orders(supplier_u_name,index)
        if len(self.order_bundles)==0:
            QMessageBox.warning(self,'Warning','No orders Found')
        else: 
            self.water = self.order_bundles[in_length]['water']
            self.quantity = self.order_bundles[in_length]['quantity']
            self.name = self.order_bundles[in_length]['name']
            self.no = self.order_bundles[in_length]['phone']
            self.address = self.order_bundles[in_length]['address']
            self.date = self.order_bundles[in_length]['date']
            self.time = self.order_bundles[in_length]['time']

        self.const_water = QLabel("Water")
        self.const_water.setFont(QFont('Arial',12))
        self.const_quantity = QLabel("Quantity")
        self.const_quantity.setFont(QFont('Arial',12 ))
        self.const_name = QLabel("Name: ")
        self.const_name.setFont(QFont('Arial',12 ))
        self.const_phone = QLabel("Phone: ")
        self.const_phone.setFont(QFont('Arial',12 ))
        self.const_address = QLabel("Address: ")
        self.const_address.setFont(QFont('Arial',12 ))
        self.const_date = QLabel("Date: ")
        self.const_date.setFont(QFont('Arial',12 ))
        self.const_time = QLabel("Time: ")
        self.const_time.setFont(QFont('Arial',12 ))


        self.get_water = QLabel(self.water)
        self.get_quantity = QLabel(self.quantity)
        self.get_name = QLabel(self.name)
        self.get_no = QLabel(self.no)
        self.get_address = QLabel(self.address)
        self.get_date = QLabel(self.date)
        self.get_time = QLabel(self.time)

        self.get_water.setFont(QFont('Arial',12))
        self.get_quantity.setFont(QFont('Arial',12 ))
        self.get_name.setFont(QFont('Arial',12 ))
        self.get_no.setFont(QFont('Arial',12 ))
        self.get_address.setFont(QFont('Arial',12 ))
        self.get_date.setFont(QFont('Arial',12 ))
        self.get_time.setFont(QFont('Arial',12 ))

        self.orders_layout.addWidget(self.const_water,0,0)
        self.orders_layout.addWidget(self.get_water,0,1)
        self.orders_layout.addWidget(self.const_quantity,1,0)
        self.orders_layout.addWidget(self.get_quantity,1,1)
        self.orders_layout.addWidget(self.const_name,2,0)
        self.orders_layout.addWidget(self.get_name,2,1)
        self.orders_layout.addWidget(self.const_phone,3,0)
        self.orders_layout.addWidget(self.get_no,3,1)
        self.orders_layout.addWidget(self.const_address,4,0)
        self.orders_layout.addWidget(self.get_address,4,1)
        self.orders_layout.addWidget(self.const_date,5,0)
        self.orders_layout.addWidget(self.get_date,5,1)
        self.orders_layout.addWidget(self.const_time,6,0)
        self.orders_layout.addWidget(self.get_time,6,1)
        self.orders_layout.addWidget(QLabel(""),7,0)
        self.orders_layout.addWidget(self.next_button,8,0)
        self.orders_layout.setAlignment(Qt.AlignCenter)

        return self.orders_layout
    


    def get_new_orders_ui(self,in_length=0):
        self.orders_layout2 = QGridLayout()

        if(in_length==len(self.order_bundles)):
            QMessageBox.warning(self,'Warning','Last Order')
            return

        self.water = self.order_bundles[in_length]['water']
        self.quantity = self.order_bundles[in_length]['quantity']
        print("Printed",self.quantity)
        self.name = self.order_bundles[in_length]['name']
        print("Printed",self.name)
        self.no = self.order_bundles[in_length]['phone']
        print("Printed",self.no)
        self.address = self.order_bundles[in_length]['address']
        print("Printed",self.address)
        self.date = self.order_bundles[in_length]['date']
        print("Printed",self.date)
        self.time = self.order_bundles[in_length]['time']
        print("Printed",self.time)

        self.const_water = QLabel("Water")
        self.const_water.setFont(QFont('Arial',12))
        self.const_quantity = QLabel("Quantity")
        self.const_quantity.setFont(QFont('Arial',12 ))
        self.const_name = QLabel("Name: ")
        self.const_name.setFont(QFont('Arial',12 ))
        self.const_phone = QLabel("Phone: ")
        self.const_phone.setFont(QFont('Arial',12 ))
        self.const_address = QLabel("Address: ")
        self.const_address.setFont(QFont('Arial',12 ))
        self.const_date = QLabel("Date: ")
        self.const_date.setFont(QFont('Arial',12 ))
        self.const_time = QLabel("Time: ")
        self.const_time.setFont(QFont('Arial',12 ))


        self.get_water = QLabel(self.water)
        self.get_quantity = QLabel(self.quantity)
        self.get_name = QLabel(self.name)
        self.get_no = QLabel(self.no)
        self.get_address = QLabel(self.address)
        self.get_date = QLabel(self.date)
        self.get_time = QLabel(self.time)

        self.get_water.setFont(QFont('Arial',12))
        self.get_quantity.setFont(QFont('Arial',12 ))
        self.get_name.setFont(QFont('Arial',12 ))
        self.get_no.setFont(QFont('Arial',12 ))
        self.get_address.setFont(QFont('Arial',12 ))
        self.get_date.setFont(QFont('Arial',12 ))
        self.get_time.setFont(QFont('Arial',12 ))
        
        

        self.orders_layout2.addWidget(self.const_water,0,0)
        self.orders_layout2.addWidget(self.get_water,0,1)
        self.orders_layout2.addWidget(self.const_quantity,1,0)
        self.orders_layout2.addWidget(self.get_quantity,1,1)
        self.orders_layout2.addWidget(self.const_name,2,0)
        self.orders_layout2.addWidget(self.get_name,2,1)
        self.orders_layout2.addWidget(self.const_phone,3,0)
        self.orders_layout2.addWidget(self.get_no,3,1)
        self.orders_layout2.addWidget(self.const_address,4,0)
        self.orders_layout2.addWidget(self.get_address,4,1)
        self.orders_layout2.addWidget(self.const_date,5,0)
        self.orders_layout2.addWidget(self.get_date,5,1)
        self.orders_layout2.addWidget(self.const_time,6,0)
        self.orders_layout2.addWidget(self.get_time,6,1)
        self.orders_layout2.addWidget(QLabel(""),7,0)
        self.orders_layout2.addWidget(self.next_button,8,0)
        self.orders_layout2.setAlignment(Qt.AlignCenter)

        return self.orders_layout2
    
    def next_order(self,):
        self.xlength += 1
        print(self.xlength)
        self.next_order_layout = self.get_new_orders_ui(self.xlength)
        return self.next_order_layout



