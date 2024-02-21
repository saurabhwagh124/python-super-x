import sys ,os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from confirmed import confirmedDetails
from register_page import *
from supplier_login import *
from supplier_register import SupplierRegister
from tanker_drinking_water import *
from location import *
from confirm_order import *
from supplier_order import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()        
        print("Calling constructor")
        self.setWindowTitle("Where's My Water")
        self.setGeometry(350,150,1200,800)
        # geometry(align left, align top, width, height)        

        self.obj_register = RegisterWindow()
        self.obj_supplier = SupplierWindow()
        self.obj_tanker_drinking = TankerDrinkingWindow()
        self.obj_location = LocationWindow()
        self.obj_confirmation_order = ConfirmOrderWindow()
        self.obj_confirmed_ticket = confirmedDetails()
        self.obj_sup_orders = SupplierOrders()
        self.obj_sup_register = SupplierRegister()

        self.center_widget = QWidget()
        self.setCentralWidget(self.center_widget)
        self.center_widget.setLayout(self.get_login_ui())
        self.background()

        #self.setLayout()

    def background(self):

        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_dir = os.path.abspath(os.path.join(current_dir, ".."))  # Go up one directory

        image_path = os.path.join(project_dir,"assets" , "water.jpg")
        oImage = QImage(image_path)
        sImage = oImage.scaled(1200,800)

        palette = self.palette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette) 
    
    def set_sup_orders_ui(self):
        self.sup_orders_widget = QWidget()
        self.setCentralWidget(self.sup_orders_widget)
        self.sup_orders_widget.setLayout(self.obj_sup_orders.get_supplier_orders_ui())

    def get_login_again(self):
        self.login_after_register = QWidget()
        self.setCentralWidget(self.login_after_register)
        self.login_after_register.setLayout(self.get_login_ui())   

    def set_register_ui(self):
        print("Clicked!!!!!")
        self.reg_wid = QWidget()
        self.setCentralWidget(self.reg_wid)
        self.reg_wid.setLayout(self.obj_register.get_register_ui())
        self.background()

    
    def set_supplier_ui(self):
        print("Supplier")
        self.supplier_wid = QWidget()
        self.setCentralWidget(self.supplier_wid)
        self.supplier_wid.setLayout(self.obj_supplier.get_supplier_login_ui())
        self.background()

    def set_supplier_register_ui(self):
        self.sup_register = QWidget()
        self.setCentralWidget(self.sup_register)
        self.sup_register.setLayout(self.obj_sup_register.get_supplier_register_ui())
    
    def set_tanker_drinking_ui(self):
        print("Tanker and drinking")
        self.tank_drink_widget = QWidget()
        self.setCentralWidget(self.tank_drink_widget)
        self.tank_drink_widget.setLayout(self.obj_tanker_drinking.get_tanker_drinking_ui())
        self.background()

    def set_widget_to_layout(self):
        self.main_central_widget = QWidget()
        self.setCentralWidget(self.main_central_widget)
        self.main_central_widget.setLayout(self.obj_location.LocationWindow_Ui())

    def set_order_layout_ui(self):
        self.order_widget = QWidget()
        self.setCentralWidget(self.order_widget)
        self.order_widget.setLayout(self.obj_confirmation_order.get_confirm_order_ui())

    def get_final_ticket_ui(self):
        self.final_ticket = QWidget()
        self.setCentralWidget(self.final_ticket)
        self.final_ticket.setLayout(self.obj_confirmed_ticket.display_ticket())

    def get_login_ui(self):

        login_window = QFormLayout()

        # creating labels
        username_label = QLabel("Username: ")
        username_label.setFont(QFont("Arial",12))
        
        password_label = QLabel("Password: ")
        password_label.setFont(QFont("Arial",12))

        # creating LineEdits
        username_line = QLineEdit()
        username_line.setGeometry(0,0,200,60)
        username_line.setFont(QFont("Arial",12))
        password_line = QLineEdit()
        password_line.setEchoMode(QLineEdit.Password)

        password_line.setGeometry(0,0,200,60)
        password_line.setFont(QFont("Arial",12))


        #creating buttons
        login_button = QPushButton("Login")
        login_button.setFixedSize(100,40)
        login_button.setFont(QFont("Arial",12))
        signup_button = QPushButton("Signup",self)
        signup_button.setFixedSize(100,40)
        signup_button.setFont(QFont("Arial",12))
        admin_button = QPushButton("Supplier")
        admin_button.setFixedSize(100,40)
        admin_button.setFont(QFont("Arial",12))

        #button theme

        login_button.setStyleSheet("QPushButton::hover"
                     "{"
                     "background-color : lightgreen;border-radius: 10px ;border-style: outset;"
                     "}"
                     "QPushButton"
                             "{"
                             "background-color : lightblue;border-radius: 10px ;border-style: outset;"
                             "}")
        signup_button.setStyleSheet("QPushButton::hover"
                     "{"
                     "background-color : lightgreen;border-radius: 10px ;border-style: outset;"
                     "}"
                     "QPushButton"
                             "{"
                             "background-color : lightblue;border-radius: 10px ;border-style: outset;"
                             "}")
        admin_button.setStyleSheet("QPushButton::hover"
                     "{"
                     "background-color : lightgreen;border-radius: 10px ;border-style: outset;"
                     "}"
                     "QPushButton"
                             "{"
                             "background-color : lightblue;border-radius: 10px ;border-style: outset;"
                             "}")

        #creating boxes
        username_box = QHBoxLayout()
        username_box.setContentsMargins(400,250,400,0)
        password_box = QHBoxLayout()
        password_box.setContentsMargins(400,0,400,0)
        button_box = QHBoxLayout()
        admin_box = QVBoxLayout()

        # adding elements in the hboxes
        username_box.addWidget(username_label)
        username_box.addWidget(username_line)

        password_box.addWidget(password_label)
        password_box.addWidget(password_line)

        button_box.addWidget(login_button)
        button_box.addWidget(signup_button)
        button_box.setAlignment(Qt.AlignCenter)

        admin_box.addWidget(admin_button)
        admin_box.setAlignment(Qt.AlignCenter)


        #adding elements to form layout
        login_window.addRow(username_box)
        login_window.addRow(password_box)
        login_window.addRow(button_box)
        login_window.addRow(admin_box)
        login_window.setAlignment(Qt.AlignCenter)

        # on clicked
        signup_button.clicked.connect(lambda: self.set_register_ui())
        admin_button.clicked.connect(lambda: self.set_supplier_ui())
        login_button.clicked.connect(lambda: self.set_tanker_drinking_ui())
        self.obj_register.submit_button.clicked.connect(lambda: self.get_login_again())
        
        # tanker_drinking connections
        self.obj_tanker_drinking.tanker_button.clicked.connect(lambda: self.set_widget_to_layout())
        self.obj_tanker_drinking.drinking_button.clicked.connect(lambda: self.set_widget_to_layout())

        #location and order buttons
        self.obj_location.aditya_water_button.clicked.connect(lambda: self.set_order_layout_ui())
        self.obj_location.nachiket_water_button.clicked.connect(lambda: self.set_order_layout_ui())
        self.obj_location.saurab_water_button.clicked.connect(lambda: self.set_order_layout_ui())       

        #submit onclick of confirmed details
        self.obj_confirmation_order.submit_button.clicked.connect(lambda: self.get_final_ticket_ui())
        
        #supplier login on click
        self.obj_supplier.sup_login_button.clicked.connect(lambda: self.set_sup_orders_ui())
        self.obj_supplier.sup_signup_button.clicked.connect(lambda: self.set_supplier_register_ui())

        #supplier register submit on click
        self.obj_sup_register.submit_button.clicked.connect(lambda: self.set_supplier_ui())

        return login_window
     
    
        

app = QApplication(sys.argv)
ex = MainWindow()
ex.show()
sys.exit(app.exec_())