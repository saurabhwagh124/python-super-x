import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class SupplierRegister(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Where's my water?")
        self.setGeometry(350,150,1200,800)
        self.submit_button = QPushButton("Submit")

    def get_supplier_register_ui(self):
        supplier_register_window = QFormLayout()

        self.sup_check_u_name = QPushButton("Check Availability")

        name_label = QLabel("Name: ")
        phone_label = QLabel("Phone no: ")
        user_label = QLabel("Username:")
        area_label = QLabel("Area")
        password_label = QLabel("Password: ")
        name_label.setFont(QFont('Arial',12 )) 
        phone_label.setFont(QFont('Arial',12 )) 
        user_label.setFont(QFont('Arial',12 ))
        area_label.setFont(QFont('Arial',12)) 
        password_label.setFont(QFont('Arial',12 )) 

        self.name_line = QLineEdit()
        self.name_line.setPlaceholderText("Enter your name")
        self.name_line.setGeometry(0,0,200,60)
        self.phone_line = QLineEdit()
        self.phone_line.setMaxLength(10)
        self.phone_line.setPlaceholderText("Enter your phone no.")
        self.phone_line.setGeometry(0,0,200,60)
        self.user_line = QLineEdit()
        self.user_line.setPlaceholderText("Enter your username")
        self.user_line.setGeometry(0,0,200,60)
        self.area_line = QLineEdit()
        self.area_line.setPlaceholderText("Enter Area you operate in")
        self.area_line.setGeometry(0,0,200,60)
        self.pass_line = QLineEdit()
        self.pass_line.setPlaceholderText("Enter your password")        
        self.pass_line.setEchoMode(QLineEdit.Password)

        self.pass_line.setGeometry(0,0,200,60)

        # setting size of text box

        self.name_line.setFixedSize(400,40)
        self.phone_line.setFixedSize(400,40)
        self.user_line.setFixedSize(400,40)
        self.area_line.setFixedSize(400,40)
        self.pass_line.setFixedSize(400,40)

        #setting fontsize of text inside text box

        self.name_line.setFont(QFont('Arial', 12))
        self.phone_line.setFont(QFont('Arial', 12))
        self.user_line.setFont(QFont('Arial', 12))
        self.area_line.setFont(QFont('Arial',12))
        self.pass_line.setFont(QFont('Arial', 12))
        

        self.name_line.setStyleSheet("border :1px solid cyan;"
                                   "border-top-left-radius :15px;"
                                   " border-top-right-radius : 15px; "
                                   "border-bottom-left-radius : 15px; "
                                   "border-bottom-right-radius : 15px") 
        self.phone_line.setStyleSheet("border :1px solid cyan;"
                                   "border-top-left-radius :15px;"
                                   " border-top-right-radius : 15px; "
                                   "border-bottom-left-radius : 15px; "
                                   "border-bottom-right-radius : 15px") 
        self.user_line.setStyleSheet("border :1px solid cyan;"
                                   "border-top-left-radius :15px;"
                                   " border-top-right-radius : 15px; "
                                   "border-bottom-left-radius : 15px; "
                                   "border-bottom-right-radius : 15px") 
        self.area_line.setStyleSheet("border: 1px solid cyan;"
                                     "border-top-left-radius : 15px;"
                                     "border-top-right-radius : 15px;"
                                     "border-bottom-left-radius : 15px;"
                                     "border-bottom-right-radius : 15px;")
        self.pass_line.setStyleSheet("border :1px solid cyan;"
                                   "border-top-left-radius :15px;"
                                   " border-top-right-radius : 15px; "
                                   "border-bottom-left-radius : 15px; "
                                   "border-bottom-right-radius : 15px") 

        #creating submit button ...................

        self.sup_check_u_name.setFixedSize(140,30)
        self.sup_check_u_name.setStyleSheet("QPushButton::hover"
                    "{"
                    "background-color : lightgreen;border-radius: 10px ;border-style: outset;"
                    "}"
                    "QPushButton"
                            "{"
                            "background-color : lightyellow;border-radius: 10px ;border-style: outset;"
                            "}")
        self.sup_check_u_name.setFont(QFont('Arial',10))
        self.submit_button.setFixedSize(100,50)
        self.submit_button.setStyleSheet("QPushButton::hover"
                    "{"
                    "background-color : lightgreen;border-radius: 10px ;border-style: outset;"
                    "}"
                    "QPushButton"
                            "{"
                            "background-color : lightyellow;border-radius: 10px ;border-style: outset;"
                            "}")

        # changins size of text in button

        self.submit_button.setFont(QFont('Arial', 15))


        #creating boxes

        name_box =QHBoxLayout()
        name_box.setContentsMargins(300,250,400,0)
        phone_box=QHBoxLayout()
        phone_box.setContentsMargins(270,0,400,0)
        user_box=QHBoxLayout()
        user_box.setContentsMargins(270,0,260,0)
        area_box = QHBoxLayout()
        area_box.setContentsMargins(270,0,400,0)
        pass_box=QHBoxLayout()
        pass_box.setContentsMargins(270,0,400,0)
        submit_box = QVBoxLayout()


        #adding element in the hbox

        name_box.addWidget(name_label)
        name_box.addWidget(self.name_line)

        phone_box.addWidget(phone_label)
        phone_box.addWidget(self.phone_line)

        user_box.addWidget(user_label)
        user_box.addWidget(self.user_line)
        user_box.addWidget(self.sup_check_u_name)

        area_box.addWidget(area_label)
        area_box.addWidget(self.area_line)

        pass_box.addWidget(password_label)
        pass_box.addWidget(self.pass_line)

        submit_box.addWidget(self.submit_button)
        submit_box.setAlignment(Qt.AlignCenter)

        supplier_register_window.addRow(name_box)
        supplier_register_window.addRow(phone_box)
        supplier_register_window.addRow(user_box)
        supplier_register_window.addRow(area_box)
        supplier_register_window.addRow(pass_box)
        supplier_register_window.addRow(submit_box)
        supplier_register_window.setAlignment(Qt.AlignCenter)

        return supplier_register_window
