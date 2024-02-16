import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt,QSize
from PyQt5.QtWidgets import QWidget

# class RegisterWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Register here")
#         self.setGeometry(350,150,1200,800)
#         self.get_register_ui()

def get_register_ui(self):
    register_window=QFormLayout()

        # creating labels
    name_label=QLabel("Name: ")
    phone_label=QLabel("PhoneNo: ")
    user_label = QLabel("Username: ")
    pass_label = QLabel("Password: ")

        
        # creating LineEdits
    name_line = QLineEdit()
    name_line.setGeometry(0,0,200,60)
    phone_line = QLineEdit()
    phone_line.setGeometry(0,0,200,60)
    user_line = QLineEdit()
    user_line.setGeometry(0,0,200,60)
    pass_line = QLineEdit()
    pass_line.setGeometry(0,0,200,60)

        #creating submit button

    self.submit_button = QPushButton("Submit")
    self.submit_button.setFixedSize(100,40)

        #creating boxes
    name_box =QHBoxLayout()
    name_box.setContentsMargins(420,250,400,0)
    phone_box=QHBoxLayout()
    phone_box.setContentsMargins(400,0,400,0)
    user_box=QHBoxLayout()
    user_box.setContentsMargins(400,0,400,0)
    pass_box=QHBoxLayout()
    pass_box.setContentsMargins(400,0,400,0)
    submit_box = QVBoxLayout()


        #adding element in the hbox

    name_box.addWidget(name_label)
    name_box.addWidget(name_line)

    phone_box.addWidget(phone_label)
    phone_box.addWidget(phone_line)

    user_box.addWidget(user_label)
    user_box.addWidget(user_line)

    pass_box.addWidget(pass_label)
    pass_box.addWidget(pass_line)

    submit_box.addWidget(self.submit_button)
    submit_box.setAlignment(Qt.AlignCenter)

        #adding elements to form layout
    register_window.addRow(name_box)
    register_window.addRow(phone_box)
    register_window.addRow(user_box)
    register_window.addRow(pass_box)
    register_window.addRow(submit_box)
    register_window.setAlignment(Qt.AlignCenter)
    self.setLayout(register_window)

# app1 = QApplication(sys.argv)
# ex1 = RegisterWindow()
# ex1.show()
# sys.exit(app1.exec_())






