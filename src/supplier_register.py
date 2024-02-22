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

        name_label = QLabel("Name: ")
        phone_label = QLabel("Phone no: ")
        user_label = QLabel("Username:")
        password_label = QLabel("Password: ")
        name_label.setFont(QFont('Arial',12 )) 
        phone_label.setFont(QFont('Arial',12 )) 
        user_label.setFont(QFont('Arial',12 )) 
        password_label.setFont(QFont('Arial',12 )) 

        name_line = QLineEdit()
        name_line.setPlaceholderText("Enter your name")
        name_line.setGeometry(0,0,200,60)
        phone_line = QLineEdit()
        phone_line.setPlaceholderText("Enter your phone no.")
        phone_line.setGeometry(0,0,200,60)
        user_line = QLineEdit()
        user_line.setPlaceholderText("Enter your username")
        user_line.setGeometry(0,0,200,60)
        pass_line = QLineEdit()
        pass_line.setPlaceholderText("Enter your password")        
        pass_line.setEchoMode(QLineEdit.Password)

        pass_line.setGeometry(0,0,200,60)

        # setting size of text box

        name_line.setFixedSize(400,40)
        phone_line.setFixedSize(400,40)
        user_line.setFixedSize(400,40)
        pass_line.setFixedSize(400,40)

        #setting fontsize of text inside text box

        name_line.setFont(QFont('Arial', 12))
        phone_line.setFont(QFont('Arial', 12))
        user_line.setFont(QFont('Arial', 12))
        pass_line.setFont(QFont('Arial', 12))
        

        name_line.setStyleSheet("border :1px solid cyan;"
                                   "border-top-left-radius :15px;"
                                   " border-top-right-radius : 15px; "
                                   "border-bottom-left-radius : 15px; "
                                   "border-bottom-right-radius : 15px") 
        phone_line.setStyleSheet("border :1px solid cyan;"
                                   "border-top-left-radius :15px;"
                                   " border-top-right-radius : 15px; "
                                   "border-bottom-left-radius : 15px; "
                                   "border-bottom-right-radius : 15px") 
        user_line.setStyleSheet("border :1px solid cyan;"
                                   "border-top-left-radius :15px;"
                                   " border-top-right-radius : 15px; "
                                   "border-bottom-left-radius : 15px; "
                                   "border-bottom-right-radius : 15px") 
        pass_line.setStyleSheet("border :1px solid cyan;"
                                   "border-top-left-radius :15px;"
                                   " border-top-right-radius : 15px; "
                                   "border-bottom-left-radius : 15px; "
                                   "border-bottom-right-radius : 15px") 

        #creating submit button ...................

        
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
        user_box.setContentsMargins(270,0,400,0)
        pass_box=QHBoxLayout()
        pass_box.setContentsMargins(270,0,400,0)
        submit_box = QVBoxLayout()


        #adding element in the hbox

        name_box.addWidget(name_label)
        name_box.addWidget(name_line)

        phone_box.addWidget(phone_label)
        phone_box.addWidget(phone_line)

        user_box.addWidget(user_label)
        user_box.addWidget(user_line)

        pass_box.addWidget(password_label)
        pass_box.addWidget(pass_line)

        submit_box.addWidget(self.submit_button)
        submit_box.setAlignment(Qt.AlignCenter)

        supplier_register_window.addRow(name_box)
        supplier_register_window.addRow(phone_box)
        supplier_register_window.addRow(user_box)
        supplier_register_window.addRow(pass_box)
        supplier_register_window.addRow(submit_box)
        supplier_register_window.setAlignment(Qt.AlignCenter)

        return supplier_register_window
