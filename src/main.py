import sys ,os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Home import check_login_details, check_sup_username_availability, check_supplier_login, check_username_availability, upload_order_details, upload_supplier_details
from confirmed import confirmedDetails
from register_page import *
from supplier_login import *
from supplier_register import SupplierRegister
from location import *
from confirm_order import *
from supplier_order import *
from Aboutus import *
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()        
        print("Calling constructor")
        self.setWindowTitle("Where is my water?")
        self.setGeometry(350,150,1200,800)
        # geometry(align left, align top, width, height)        

        self.obj_register = RegisterWindow()
        self.obj_about = AboutUs()
        self.obj_supplier = SupplierWindow()
        self.obj_location = LocationWindow()
        self.obj_confirmation_order = ConfirmOrderWindow()
        self.obj_confirmed_ticket = confirmedDetails()
        self.obj_sup_orders = SupplierOrders()
        self.obj_sup_register = SupplierRegister()

        self.center_widget = QWidget()
        self.setCentralWidget(self.center_widget)
        self.center_widget.setLayout(self.get_login_ui())
        self.background("water.jpg")

        #self.setLayout()

    def background(self,image_name):    
        # self.image_name= "water.jpg"
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.project_dir = os.path.abspath(os.path.join(self.current_dir, ".."))  # Go up one directory

        self.image_path = os.path.join(self.project_dir,"assets" , image_name)
        oImage = QImage(self.image_path)
        sImage = oImage.scaled(1200,800)

        palette = self.palette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)   

    def set_register_ui(self):
        print("Clicked!!!!!")
        self.reg_wid = QWidget()
        self.setCentralWidget(self.reg_wid)
        self.reg_wid.setLayout(self.obj_register.get_register_ui())
        self.obj_register.check_u_name.clicked.connect(lambda:  self.username_availability() )
        self.obj_register.submit_button.clicked.connect(lambda: self.get_login_again())
        self.background("water_bottle1.jpg")
    
    def username_availability(self):
        u_name_av = check_username_availability(self.obj_register.user_line.text())
        if(u_name_av):
           return QMessageBox.warning(self,'warning','This username is taken')
        else:
           return QMessageBox.information(self,'Info','Username Available')
        

    def get_login_again(self):
        self.login_after_register = QWidget()
        self.setCentralWidget(self.login_after_register)
        register_to_db(self.obj_register.user_line.text(),self.obj_register.name_line.text(),self.obj_register.pass_line.text(),self.obj_register.phone_line.text())
        self.login_after_register.setLayout(self.get_login_ui())
        self.background("water.jpg")

    def set_about_us_ui(self):
        self.about_widget = QWidget()
        self.setCentralWidget(self.about_widget)
        self.about_widget.setLayout(self.obj_about.thankyou_ui())
        self.obj_about.back.clicked.connect(lambda: self.set_login_after_about())
        self.background("thanks.jpg")
    
    def set_login_after_about(self):
        self.back_about_widget = QWidget()
        self.setCentralWidget(self.back_about_widget)
        self.back_about_widget.setLayout(self.get_login_ui())
        self.background("water.jpg")

    def set_location_ui(self):
        print("Tanker and drinking")
        check = check_login_details(self.username_line.text(), self.password_line.text())
        if (check): 
            self.location_widget = QWidget()
            self.setCentralWidget(self.location_widget)
            self.location_widget.setLayout(self.obj_location.LocationWindow_Ui())
            self.obj_location.aditya_water_button.clicked.connect(lambda: self.set_order_layout_ui("Aditya water"))
            self.obj_location.nachiket_water_button.clicked.connect(lambda: self.set_order_layout_ui("Nachiket Water provider"))
            self.obj_location.saurab_water_button.clicked.connect(lambda: self.set_order_layout_ui("Saurabh Water Suppliers")) 
            self.background("water_truck.jpg")
        else:
            QMessageBox.warning(self,'Warning','Login Unsuccessful')
            return
        
    def set_order_layout_ui(self,supplier_name):
        self.order_widget = QWidget()
        self.supplier_name = supplier_name
        self.setCentralWidget(self.order_widget)
        self.order_widget.setLayout(self.obj_confirmation_order.get_confirm_order_ui(self.supplier_name))
        self.obj_confirmation_order.submit_button.clicked.connect(lambda: self.get_final_ticket_ui())
        self.background("fog.jpg")


    def get_final_ticket_ui(self):
        upload_order_details(self.obj_confirmation_order.con_water_combo.currentText(),self.obj_confirmation_order.con_quantity_line.text(),self.obj_confirmation_order.con_name_line.text(),self.obj_confirmation_order.con_phone_line.text(),self.obj_confirmation_order.con_address_line.text(),self.obj_confirmation_order.con_calender.text(),self.obj_confirmation_order.con_clock.text(),self.obj_confirmation_order.con_supplier.text())
        self.final_ticket = QWidget()
        self.setCentralWidget(self.final_ticket)
        self.final_ticket.setLayout(self.obj_confirmed_ticket.display_ticket(self.obj_confirmation_order.con_name_line.text()))
        self.obj_confirmed_ticket.logout_button.clicked.connect(lambda: self.after_logout_ui() )
        self.background("water3.jpg")

    def after_logout_ui(self):
        self.logout_widget = QWidget()
        self.setCentralWidget(self.logout_widget)
        self.logout_widget.setLayout(self.get_login_ui())
        self.background("water.jpg")
    
    
    def set_supplier_ui(self):
        print("Supplier")
        self.supplier_wid = QWidget()
        self.setCentralWidget(self.supplier_wid)
        self.supplier_wid.setLayout(self.obj_supplier.get_supplier_login_ui())
        self.obj_supplier.sup_login_button.clicked.connect(lambda: self.set_sup_orders_ui(self.obj_supplier.supplier_u_name_line.text(),self.obj_supplier.supplier_password_line.text()))
        self.obj_supplier.sup_signup_button.clicked.connect(lambda: self.set_supplier_register_ui())
        self.background("water_del.jpg")

    def set_supplier_register_ui(self):
        self.sup_register = QWidget()
        self.setCentralWidget(self.sup_register)
        self.sup_register.setLayout(self.obj_sup_register.get_supplier_register_ui())
        self.obj_sup_register.sup_check_u_name.clicked.connect(lambda: self.sup_username_availability())
        self.obj_sup_register.submit_button.clicked.connect(lambda: self.set_supplier_ui_again())
        self.background("water_truck.jpg")

    def sup_username_availability(self):
        u_name_av = check_sup_username_availability(self.obj_sup_register.user_line.text())
        if(u_name_av):
           return QMessageBox.warning(self,'warning','This username is taken')
        else:
           return QMessageBox.information(self,'Info','Username Available')

    def set_supplier_ui_again(self):
        self.obj_supplier = SupplierWindow()
        self.supplier_wid2 = QWidget()
        upload_supplier_details(self.obj_sup_register.name_line.text(),self.obj_sup_register.user_line.text(),self.obj_sup_register.phone_line.text(),self.obj_sup_register.area_line.text(),self.obj_sup_register.pass_line.text())
        self.setCentralWidget(self.supplier_wid2)
        self.supplier_wid2.setLayout(self.obj_supplier.get_supplier_login_ui())
        self.obj_supplier.sup_login_button.clicked.connect(lambda: self.set_sup_orders_ui(self.obj_supplier.supplier_u_name_line.text(),self.obj_supplier.supplier_password_line.text()))
        #self.background("water_del.jpg")
    
    def set_sup_orders_ui(self,supplier_u_name,supplier_password):
        check_admin = check_supplier_login(supplier_u_name,supplier_password)
        if(check_admin):
            self.sup_orders_widget = QWidget()
            self.setCentralWidget(self.sup_orders_widget)
            index = 0
            self.sup_orders_widget.setLayout(self.obj_sup_orders.get_supplier_orders_ui(supplier_u_name, index))
            self.obj_sup_orders.next_button.clicked.connect(lambda: self.set_sup_next_order_ui())
        else:
            QMessageBox.warning(self,'warning','Invalid username/password')
            return
        self.background("orders.jpg")
        

    def set_sup_next_order_ui(self):
        self.set_new_orders = QWidget()
        self.setCentralWidget(self.set_new_orders)
        self.set_new_orders.setLayout(self.obj_sup_orders.next_order())
        self.background("orders.jpg")



    def get_login_ui(self):

        login_window = QFormLayout()

        # creating labels
        username_label = QLabel("Username: ")
        username_label.setFont(QFont("Arial",13,20))
        username_label.setStyleSheet("background-color : white")
        
        password_label = QLabel("Password: ")
        password_label.setFont(QFont("Arial",13,20))
        password_label.setStyleSheet("background-color : white")

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
        login_button.clicked.connect(lambda: self.set_location_ui())      


        return login_window
     
    
        

app = QApplication(sys.argv)
ex = MainWindow()
ex.show()
sys.exit(app.exec_())