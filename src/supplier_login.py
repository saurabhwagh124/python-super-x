import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class SupplierWindow(QWidget):
    def __init__(self):
        super().__init__()        
        self.setWindowTitle("Where's My Water?")
        
        self.setGeometry(350,150,1200,800)
        # geometry(align left, align top, width, height)
        self.sup_login_button = QPushButton("Login")
        self.sup_signup_button = QPushButton("Signup")
        #self.setLayout()

    def get_supplier_login_ui(self):

        supplier_login_window = QFormLayout()

        # creating labels
        supplier_u_name_label = QLabel("Username: ")
        supplier_u_name_label.setFont(QFont('Arial',12))
        #username_label.se
        supplier_password_label = QLabel("Password: ")
        supplier_password_label.setFont(QFont('Arial',12))

        # creating LineEdits
        supplier_u_name_line = QLineEdit()
        supplier_u_name_line.setPlaceholderText("Enter your name")

        supplier_u_name_line.setGeometry(0,0,200,60)
        supplier_u_name_line.setFont(QFont('Arial',12))
        supplier_password_line = QLineEdit()
        supplier_password_line.setPlaceholderText("Enter your password")

        supplier_password_line.setGeometry(0,0,200,60)
        supplier_password_line.setFont(QFont('Arial',12))

        #curves

        supplier_u_name_line.setStyleSheet("border :1px solid cyan;"
                                   "border-top-left-radius :15px;"
                                   " border-top-right-radius : 15px; "
                                   "border-bottom-left-radius : 15px; "
                                   "border-bottom-right-radius : 15px") 
        supplier_password_line.setStyleSheet("border :1px solid cyan;"
                                   "border-top-left-radius :15px;"
                                   " border-top-right-radius : 15px; "
                                   "border-bottom-left-radius : 15px; "
                                   "border-bottom-right-radius : 15px") 


        #creating buttons
        
        self.sup_login_button.setFixedSize(100,40)
        self.sup_login_button.setFont(QFont('Arial',12))
        
        self.sup_signup_button.setFixedSize(100,40)
        self.sup_signup_button.setFont(QFont('Arial',12))

        #button theme

        self.sup_login_button.setStyleSheet("QPushButton::hover"
                     "{"
                     "background-color : lightgreen;border-radius: 10px ;border-style: outset;"
                     "}"
                     "QPushButton"
                             "{"
                             "background-color :  lightyellow;border-radius: 10px ;border-style: outset;"
                             "}")
        
        
        self.sup_signup_button.setStyleSheet("QPushButton::hover"
                     "{"
                     "background-color : lightgreen;border-radius: 10px ;border-style: outset;"
                     "}"
                     "QPushButton"
                             "{"
                             "background-color :  lightyellow;border-radius: 10px ;border-style: outset;"
                             "}")

        #creating boxes
        sup_u_name_box = QHBoxLayout()
        sup_u_name_box.setContentsMargins(400,250,400,0)
        sup_password_box = QHBoxLayout()
        sup_password_box.setContentsMargins(400,0,400,0)
        button_box = QHBoxLayout()

        # adding elements in the hboxes
        sup_u_name_box.addWidget(supplier_u_name_label)
        sup_u_name_box.addWidget(supplier_u_name_line)

        sup_password_box.addWidget(supplier_password_label)
        sup_password_box.addWidget(supplier_password_line)

        button_box.addWidget(self.sup_login_button)
        button_box.addWidget(self.sup_signup_button)
        button_box.setAlignment(Qt.AlignCenter)        

        #adding elements to form layout
        supplier_login_window.addRow(sup_u_name_box)
        supplier_login_window.addRow(sup_password_box)
        supplier_login_window.addRow(button_box)
        supplier_login_window.setAlignment(Qt.AlignCenter)
        return supplier_login_window




#app = QApplication(sys.argv)
#ex = SupplierWindow()
#ex.show()
#sys.exit(app.exec_())