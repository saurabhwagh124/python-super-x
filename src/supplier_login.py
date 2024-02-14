import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt,QSize

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()        
        self.setWindowTitle("Login")
        
        self.setGeometry(350,150,1200,800)
        # geometry(align left, align top, width, height)
        
        self.get_login_ui()
        #self.setLayout()

    def get_login_ui(self):

        login_window = QFormLayout()

        # creating labels
        supplier_u_name_label = QLabel("Username: ")
        #username_label.se
        supplier_password_label = QLabel("Password: ")

        # creating LineEdits
        supplier_u_name_line = QLineEdit()
        supplier_u_name_line.setGeometry(0,0,200,60)
        supplier_password_line = QLineEdit()
        supplier_password_line.setGeometry(0,0,200,60)


        #creating buttons
        sup_login_button = QPushButton("Login")
        sup_login_button.setFixedSize(100,40)
        sup_signup_button = QPushButton("Signup")
        sup_signup_button.setFixedSize(100,40)

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

        button_box.addWidget(sup_login_button)
        button_box.addWidget(sup_signup_button)
        button_box.setAlignment(Qt.AlignCenter)        

        #adding elements to form layout
        login_window.addRow(sup_u_name_box)
        login_window.addRow(sup_password_box)
        login_window.addRow(button_box)
        login_window.setAlignment(Qt.AlignCenter)
        self.setLayout(login_window)




app = QApplication(sys.argv)
ex = MainWindow()
ex.show()
sys.exit(app.exec_())