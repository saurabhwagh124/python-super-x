import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class SupplierOrders(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Where's my water")
        self.setGeometry(350,150,1200,800)
        self.next_button = QPushButton("Next")
        self.name = "xyz"
        self.no = "123"
        self.address = "Abc"
        self.quantity = "50"
        self.date = "01/12/2004"
        self.time = "2:30 pm"

    def get_supplier_orders_ui(self):
        self.orders_layout = QGridLayout()

        self.const_name = QLabel("Name: ")
        self.const_phone = QLabel("Phone: ")
        self.const_address = QLabel("Address: ")
        self.const_quantity = QLabel("Quantity")
        self.const_date = QLabel("Date: ")
        self.const_time = QLabel("Time: ")

        self.get_name = QLabel(self.name)
        self.get_no = QLabel(self.no)
        self.get_address = QLabel(self.address)
        self.get_quantity = QLabel(self.quantity)
        self.get_date = QLabel(self.date)
        self.get_time = QLabel(self.time)


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


