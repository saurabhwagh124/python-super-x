import sys 
from PyQt5.QtWidgets import *

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
        username_label = QLabel("Username: ")
        password_label = QLabel("Password: ")

        # creating LineEdits
        username_line = QLineEdit()
        username_line.setMaxLength(20)
        password_line = QLineEdit()
        password_line.setMaxLength(20)

        #creating buttons
        login_button = QPushButton("Login")
        login_button.setFixedSize(100,40)
        signup_button = QPushButton("Signup")
        signup_button.setFixedSize(100,40)

        #creating boxes
        username_box = QHBoxLayout()
        password_box = QHBoxLayout()

        # adding elements in the hboxes
        username_box.addWidget(username_label)
        username_box.addWidget(username_line)

        password_box.addWidget(password_label)
        password_box.addWidget(password_line)

        #creating a child layout of vbox to insert hbox and push buttons in
        

        #adding elements to form layout
        login_window.addRow(username_box)
        login_window.addRow(password_box)
        login_window.addRow(login_button)
        login_window.addRow(signup_button)
        self.setLayout(login_window)


app = QApplication(sys.argv)
ex = MainWindow()
ex.show()
sys.exit(app.exec_())