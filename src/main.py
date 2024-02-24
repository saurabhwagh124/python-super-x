import sys ,os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Home import check_login_details, upload_order_details, upload_supplier_details
from confirmed import confirmedDetails
from register_page import *
from supplier_login import *
from supplier_register import SupplierRegister
from tanker_drinking_water import *
from location import *
from confirm_order import *
from supplier_order import *
from about_us import *
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()        
        print("Calling constructor")
        self.setWindowTitle("Where's My Water")
        self.setGeometry(350,150,1200,800)
        # geometry(align left, align top, width, height)        

        self.obj_register = RegisterWindow()
        self.obj_about = AboutUS()
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
        register_to_db(self.obj_register.user_line.text(),self.obj_register.name_line.text(),self.obj_register.pass_line.text(),self.obj_register.phone_line.text())
        self.login_after_register.setLayout(self.get_login_ui())


    def set_register_ui(self):
        print("Clicked!!!!!")
        self.reg_wid = QWidget()
        self.setCentralWidget(self.reg_wid)
        self.reg_wid.setLayout(self.obj_register.get_register_ui())
        self.background()
    
    def set_about_us_ui(self):
        self.about_widget = QWidget()
        self.setCentralWidget(self.about_widget)
        self.about_widget.setLayout(self.obj_about.thankyou_ui())

    def set_supplier_ui(self):
        print("Supplier")
        self.supplier_wid = QWidget()
        self.setCentralWidget(self.supplier_wid)
        self.supplier_wid.setLayout(self.obj_supplier.get_supplier_login_ui())
        self.background()
    
    def set_supplier_ui_again(self):
        self.obj_supplier = SupplierWindow()
        self.supplier_wid2 = QWidget()
        upload_supplier_details(self.obj_sup_register.name_line.text(),self.obj_sup_register.user_line.text(),self.obj_sup_register.phone_line.text(),self.obj_sup_register.pass_line.text())
        self.setCentralWidget(self.supplier_wid2)
        self.supplier_wid2.setLayout(self.obj_supplier.get_supplier_login_ui())
        self.obj_supplier.sup_login_button.clicked.connect(lambda: self.set_sup_orders_ui())
        self.background()

    def set_supplier_register_ui(self):
        self.sup_register = QWidget()
        self.setCentralWidget(self.sup_register)
        self.sup_register.setLayout(self.obj_sup_register.get_supplier_register_ui())
    
    def set_tanker_drinking_ui(self):
        print("Tanker and drinking")
        if (check_login_details(self.username_line.text(), self.password_line.text())): 
            self.tank_drink_widget = QWidget()
            print("Login sucessfull")
            self.setCentralWidget(self.tank_drink_widget)
            self.tank_drink_widget.setLayout(self.obj_tanker_drinking.get_tanker_drinking_ui())
            self.background()
        else:
            print("Login unsucessful")
            return

    def set_widget_to_layout(self):
        self.main_central_widget = QWidget()
        self.setCentralWidget(self.main_central_widget)
        self.main_central_widget.setLayout(self.obj_location.LocationWindow_Ui())

    def set_order_layout_ui(self,supplier_name):
        self.order_widget = QWidget()
        self.supplier_name = supplier_name
        self.setCentralWidget(self.order_widget)
        self.order_widget.setLayout(self.obj_confirmation_order.get_confirm_order_ui(self.supplier_name))

    def get_final_ticket_ui(self):
        upload_order_details(self.obj_confirmation_order.con_quantity_line.text(),self.obj_confirmation_order.con_name_line.text(),self.obj_confirmation_order.con_phone_line.text(),self.obj_confirmation_order.con_address_line.text(),self.obj_confirmation_order.con_calender.text(),self.obj_confirmation_order.con_clock.text(),self.obj_confirmation_order.con_supplier.text())
        self.final_ticket = QWidget()
        self.setCentralWidget(self.final_ticket)
        self.final_ticket.setLayout(self.obj_confirmed_ticket.display_ticket(self.obj_confirmation_order.con_name_line.text()))

    def get_login_ui(self):

        login_window = QFormLayout()

        # creating labels
        username_label = QLabel("Username: ")
        username_label.setFont(QFont("Arial",13,20))
        
        password_label = QLabel("Password: ")
        password_label.setFont(QFont("Arial",13,20))

        blank_label1 = QLabel("")
        blank_label1.setFixedHeight(20)

        blank_label2 = QLabel("")
        blank_label2.setFixedHeight(20)

        blank_label3 = QLabel("")
        blank_label3.setFixedHeight(20)

        # creating LineEdits
        self.username_line = QLineEdit()
        self.username_line.setPlaceholderText("Enter your username")
        self.username_line.setGeometry(0,0,200,60)
        self.username_line.setFont(QFont("Arial",12))
        self.username_line.setStyleSheet("border :1px solid cyan;"
                                   "border-top-left-radius :15px;"
                                   " border-top-right-radius : 15px; "
                                   "border-bottom-left-radius : 15px; "
                                   "border-bottom-right-radius : 15px") 
        self.password_line = QLineEdit()
        self.password_line.setPlaceholderText("Enter your password")

        self.password_line.setEchoMode(QLineEdit.Password)
       
        self.password_line.setGeometry(0,0,200,60)
        self.password_line.setFont(QFont("Arial",12))
        self.password_line.setStyleSheet("border :2px solid cyan;"
                                   "border-top-left-radius :15px;"
                                   " border-top-right-radius : 15px; "
                                   "border-bottom-left-radius : 15px; "
                                   "border-bottom-right-radius : 15px") 


        #creating buttons
        about_us_button = QPushButton("About us")
        about_us_button.setFixedSize(100,40)
        about_us_button.setFont(QFont("Arial",12))
        about_us_button.setContentsMargins(550,0,550,0)
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
                             "background-color :  lightyellow;border-radius: 10px ;border-style: outset;"
                             "}")
        signup_button.setStyleSheet("QPushButton::hover"
                     "{"
                     "background-color : lightgreen;border-radius: 10px ;border-style: outset;"
                     "}"
                     "QPushButton"
                             "{"
                             "background-color :lightyellow;border-radius: 10px ;border-style: outset;"
                             "}")
        admin_button.setStyleSheet("QPushButton::hover"
                     "{"
                     "background-color : lightgreen;border-radius: 10px ;border-style: outset;"
                     "}"
                     "QPushButton"
                             "{"
                             "background-color : lightyellow;border-radius: 10px ;border-style: outset;"
                             "}")
        about_us_button.setStyleSheet("QPushButton::hover"
                     "{"
                     "background-color : lightgreen;border-radius: 10px ;border-style: outset;"
                     "}"
                     "QPushButton"
                             "{"
                             "background-color : lightyellow;border-radius: 10px ;border-style: outset;"
                             "}")

        #creating boxes
        username_box = QHBoxLayout()
        username_box.setContentsMargins(400,250,400,0)
        password_box = QHBoxLayout()
        password_box.setContentsMargins(400,0,400,0)
        button_box = QHBoxLayout()
        admin_box = QVBoxLayout()
        about_us_box = QHBoxLayout()

        # adding elements in the hboxes
        username_box.addWidget(username_label)
        username_box.addWidget(self.username_line)

        password_box.addWidget(password_label)
        password_box.addWidget(self.password_line)

        button_box.addWidget(login_button)
        button_box.addWidget(signup_button)
        button_box.setAlignment(Qt.AlignCenter)

        admin_box.addWidget(admin_button)
        admin_box.setAlignment(Qt.AlignCenter)

        about_us_box.addWidget(about_us_button)
        about_us_box.setAlignment(Qt.AlignCenter)

        #adding elements to form layout
        login_window.addRow(username_box)
        login_window.addRow(password_box)
        login_window.addRow(blank_label1)
        login_window.addRow(button_box)
        login_window.addRow(blank_label2)
        login_window.addRow(admin_box)
        login_window.addRow(blank_label3)
        login_window.addRow(about_us_box)
        login_window.setAlignment(Qt.AlignCenter)

        # on clicked
        signup_button.clicked.connect(lambda: self.set_register_ui())
        admin_button.clicked.connect(lambda: self.set_supplier_ui())
        about_us_button.clicked.connect(lambda: self.set_about_us_ui())
        login_button.clicked.connect(lambda: self.set_tanker_drinking_ui())
        self.obj_register.submit_button.clicked.connect(lambda: self.get_login_again())
        
        # tanker_drinking connections
        self.obj_tanker_drinking.tanker_button.clicked.connect(lambda: self.set_widget_to_layout())
        self.obj_tanker_drinking.drinking_button.clicked.connect(lambda: self.set_widget_to_layout())

        #location and order buttons
        self.obj_location.aditya_water_button.clicked.connect(lambda: self.set_order_layout_ui("Aditya water"))
        self.obj_location.nachiket_water_button.clicked.connect(lambda: self.set_order_layout_ui("Nachiket Water provider"))
        self.obj_location.saurab_water_button.clicked.connect(lambda: self.set_order_layout_ui("Saurabh Water Suppliers"))       

        #submit onclick of confirmed details
        self.obj_confirmation_order.submit_button.clicked.connect(lambda: self.get_final_ticket_ui())
        
        #supplier login on clicks
        self.obj_supplier.sup_login_button.clicked.connect(lambda: self.set_sup_orders_ui())
        #self.obj_supplier_login.sup_login_button.clicked.connect(lambda: self.set_sup_orders_ui())
        self.obj_supplier.sup_signup_button.clicked.connect(lambda: self.set_supplier_register_ui())

        #supplier register submit on click
        self.obj_sup_register.submit_button.clicked.connect(lambda: self.set_supplier_ui_again())

        self.obj_about.back_button.clicked.connect(lambda: self.get_login_ui())

        return login_window
     
    
        

app = QApplication(sys.argv)
ex = MainWindow()
ex.show()
sys.exit(app.exec_())