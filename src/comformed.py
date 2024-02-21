import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt,QSize
from PyQt5.QtWidgets import QWidget

class ComfirmedDetails(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Comfirmed Details")
        #self.setGeometry(100,150,1000,800)
        width = 1500
         
        # setting  the fixed width of window
        self.setFixedWidth(width)

        #self.setGeometry(100,150,1000,800)
        height = 800
         
        # setting  the fixed width of window
        self.setFixedHeight(height)
        self.str_quantity=" sample quantity"
        self.str_name=" sample time"
        self.str_phone=" sample phone"
        self.str_address=" sample address"
        self.str_date=" sample date"
        self.str_time= " sample time"
    
 

        self.displayInfo()
    
        
        

    def displayInfo(self):
        self.comfirmed_window=QFormLayout()

       
      
        

         # creating labels
        self.comf_quantity_label = QLabel("Quantity of water needed: ")
        self.comf_name_label =  QLabel("Name: ")
        self.comf_phone_label = QLabel("Phone no.: ")
        self.comf_address_label = QLabel("Address: ")
        self.comf_date_label  = QLabel("Select Date: ")
        self.comf_time_label = QLabel("Select Time: ")


         #creating buttons  
        self.refresh_button = QPushButton("Refresh")
        self.refresh_button.setFixedSize(100,50)
        self.refresh_button.setFont(QFont('Arial', 15))
        refresh_box = QVBoxLayout()
        refresh_box.addWidget(self.refresh_button)
        refresh_box.setAlignment(Qt.AlignRight)
        self.refresh_button.move(100, 60)
        
        self.comfirmed_window.addWidget(self.refresh_button)


        self.next_button = QPushButton("Next")
        self.next_button.setFixedSize(100,50)
        self.next_button.setFont(QFont('Arial', 15))
        next_box = QVBoxLayout()
        next_box.addWidget(self.next_button)
        next_box.setAlignment(Qt.AlignCenter)
        self.next_button.move(100, 60)
        
        self.comfirmed_window.addWidget(self.next_button)
        
        

        # creating LineEdits
        self.comf_quantity_line = QLabel(self.str_quantity)#####
        self.comf_quantity_line.setGeometry(0,0,200,60)
        self.comf_name_line = QLabel(self.str_name)
        self.comf_name_line.setGeometry(0,0,200,60)
        self.comf_phone_line = QLabel(self.str_phone)
        self.comf_phone_line.setGeometry(0,0,200,60)
        self.comf_address_line = QLabel(self.str_address)
        self.comf_address_line.setGeometry(0,0,200,60)
        self.comf_date_line = QLabel(self.str_date)
        self.comf_date_line.setGeometry(0,0,200,60)
        self.comf_time_line = QLabel(self.str_time)
        self.comf_time_line.setGeometry(0,0,200,60)
       

        
        self.comf_quantity_line.setFixedSize(500,40)
        self.comf_name_line.setFixedSize(500,40)
        self.comf_phone_line.setFixedSize(500,40)
        self.comf_address_line.setFixedSize(500,40)
        self.comf_date_line.setFixedSize(500,40)
        self.comf_time_line.setFixedSize(500,40)




        

         #changing font size 

        self.comf_quantity_label.setFont(QFont('Arial',12 )) 
        self.comf_name_label.setFont(QFont('Arial',12 ))
        self.comf_phone_label.setFont(QFont('Arial',12 ))
        self.comf_address_label.setFont(QFont('Arial',12 ))
        self.comf_date_label.setFont(QFont('Arial',12 ))
        self.comf_time_label.setFont(QFont('Arial',12 ))

             
            # creating LineEdits

        self.comf_quantity_line = QLabel(self.str_quantity)
        self.comf_quantity_line.setGeometry(0,0,500,60)
        self.comf_name_line = QLabel(self.str_name)
        self.comf_name_line.setGeometry(0,0,200,60)
        self.comf_phone_line = QLabel(self.str_phone)
        self.comf_phone_line.setGeometry(0,0,200,60)
        
        comf_address_line = QLabel(self.str_address)
        comf_address_line.setGeometry(0,0,200,60)
        comf_date_line = QLabel(self.str_date)
        comf_date_line.setGeometry(0,0,200,60)
        comf_time_line = QLabel(self.str_time)
        comf_time_line.setGeometry(0,0,200,60)


        self.comfirmed_window.addWidget(self.comf_quantity_line)
        self.comfirmed_window.addWidget(self.comf_name_line)
        self.comfirmed_window.addWidget(self.comf_phone_line)
        self.comfirmed_window.addWidget(self.comf_address_line)
        self.comfirmed_window.addWidget(self.comf_date_line)
        self.comfirmed_window.addWidget(self.comf_time_line)



         # setting size of text box

        self.comf_quantity_line.setFixedSize(500,40)
        self.comf_name_line.setFixedSize(500,40)
        self.comf_phone_line.setFixedSize(500,40)
        self.comf_address_line.setFixedSize(500,40)
        self.comf_date_line.setFixedSize(500,40)
        self.comf_time_line.setFixedSize(500,40)

        #fontsizeself.

        self.comf_quantity_line.setFont(QFont('Arial',12))
        self.comf_name_line.setFont(QFont('Arial',12))
        self.comf_phone_line.setFont(QFont('Arial',12))
        self.comf_address_line.setFont(QFont('Arial',12))
        self.comf_date_line.setFont(QFont('Arial',12))
        self.comf_time_line.setFont(QFont('Arial',12))

         #creating submit button ...................

       
            # changins size of text in button

       


         #creating boxes

        self.comf_quantity_box =QHBoxLayout()
        self.comf_quantity_box.setContentsMargins(420,0,500,0)
        self.comf_name_box=QHBoxLayout()
        self.comf_name_box.setContentsMargins(430,0,500,0)
        self.comf_phone_box=QHBoxLayout()
        self.comf_phone_box.setContentsMargins(430,0,500,0)
        self.comf_address_box=QHBoxLayout()
        self.comf_address_box.setContentsMargins(430,0,500,0)
        self.comf_date_box=QHBoxLayout()
        self.comf_date_box.setContentsMargins(430,0,500,0)
        self.comf_time_box=QHBoxLayout()
        
        self.comf_time_box.setContentsMargins(430,0,500,0)
        
        
        


         #adding element in the hbox

        self.comf_quantity_box.addWidget(self.comf_quantity_label)
        self.comf_quantity_box.addWidget(self.comf_quantity_line)

        self.comf_name_box.addWidget(self.comf_name_label)
        self.comf_name_box.addWidget(self.comf_name_line)

        self.comf_phone_box.addWidget(self.comf_phone_label)
        self.comf_phone_box.addWidget(self.comf_phone_line)

        self.comf_address_box.addWidget(self.comf_address_label)
        self.comf_address_box.addWidget(self.comf_address_line)

        self.comf_date_box.addWidget(self.comf_date_label)
        self.comf_date_box.addWidget(self.comf_date_line)

        self.comf_time_box.addWidget(self.comf_time_label)
        self.comf_time_box.addWidget(self.comf_time_line)
         #adding elements to form layout

        self.comfirmed_window.addRow(self.comf_quantity_box)
        self.comfirmed_window.addRow(self.comf_name_box)
        self.comfirmed_window.addRow(self.comf_phone_box)
        self.comfirmed_window.addRow(self.comf_address_box)
        self.comfirmed_window.addRow(self.comf_date_box)
        self.comfirmed_window.addRow(self.comf_time_box)
        self.comfirmed_window.setAlignment(Qt.AlignCenter)

        return self.comfirmed_window 

       

     
            








        