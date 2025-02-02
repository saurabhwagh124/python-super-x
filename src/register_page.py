import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt,QSize
from PyQt5.QtWidgets import QWidget
from Home import register_to_db

class RegisterWindow(QWidget):
     def __init__(self):
        super().__init__()
        self.setWindowTitle("Register here")
        self.setGeometry(350,150,1200,800)
        self.submit_button = QPushButton("Submit")

     def get_register_ui(self):
            register_window=QFormLayout()

            # creating labels
            name_label=QLabel("Name: ")
            phone_label=QLabel("PhoneNo: ")
            user_label = QLabel("Username: ")
            pass_label = QLabel("Password: ")

            self.check_u_name = QPushButton("Check Username")


            #changing font size 

            name_label.setFont(QFont('Arial',12 )) 
            phone_label.setFont(QFont('Arial',12 )) 
            user_label.setFont(QFont('Arial',12 )) 
            pass_label.setFont(QFont('Arial',12 )) 


               
            # creating LineEdits

            self.name_line = QLineEdit()
            # name_line.placeholderText("enter")
            self.name_line.setGeometry(0,0,200,60)
            self.phone_line = QLineEdit()
            self.phone_line.setMaxLength(10)
            self.phone_line.setValidator(QIntValidator())
            self.phone_line.setGeometry(0,0,200,60)
            self.user_line = QLineEdit()
            self.user_line.setGeometry(0,0,200,60)
            self.pass_line = QLineEdit()
            self.pass_line.setEchoMode(QLineEdit.Password)

            self.pass_line.setGeometry(0,0,200,60)

            # setting size of text box

            self.name_line.setFixedSize(400,40)
            self.phone_line.setFixedSize(400,40)
            self.user_line.setFixedSize(400,40)
            self.pass_line.setFixedSize(400,40)
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
            self.pass_line.setStyleSheet("border :1px solid cyan;"
                                   "border-top-left-radius :15px;"
                                   " border-top-right-radius : 15px; "
                                   "border-bottom-left-radius : 15px; "
                                   "border-bottom-right-radius : 15px") 




            #setting fontsize of text inside text box

            self.name_line.setFont(QFont('Arial', 12))
            self.phone_line.setFont(QFont('Arial', 12))
            self.user_line.setFont(QFont('Arial', 12))
            self.pass_line.setFont(QFont('Arial', 12))


            #creating submit button ...................

            self.check_u_name.setFixedSize(100,30)
            self.check_u_name.setStyleSheet("QPushButton::hover"
                     "{"
                     "background-color : lightgreen;border-radius: 10px ;border-style: outset;"
                     "}"
                     "QPushButton"
                             "{"
                             "background-color : lightyellow;border-radius: 10px ;border-style: outset;"
                             "}")
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
            user_box.setContentsMargins(270,0,300,0)
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
            user_box.addWidget(self.check_u_name)

            pass_box.addWidget(pass_label)
            pass_box.addWidget(self.pass_line)

            submit_box.addWidget(self.submit_button)
            submit_box.setAlignment(Qt.AlignCenter)

            #adding elements to form layout

            register_window.addRow(name_box)
            register_window.addRow(phone_box)
            register_window.addRow(user_box)
            register_window.addRow(pass_box)
            register_window.addRow(submit_box)
            register_window.setAlignment(Qt.AlignCenter)
            
            return register_window







