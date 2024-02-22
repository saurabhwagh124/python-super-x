import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt,QSize
from PyQt5.QtWidgets import QWidget
import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt,QSize
from PyQt5.QtWidgets import QWidget


class Thanking(QWidget):
     def __init__(self):
        super().__init__()
        self.setWindowTitle("About Us")
        self.setGeometry(350,150,1200,800)
        self.thankyou_ui()

     def thankyou_ui(self):
        thankyou_window=QFormLayout()
        Title = QLabel("Gratitute to Shashi Sir and Core2Web Family")
        line1 = QLabel("Our team would like to express gratitude to Shashi Sir")
        line2 = QLabel("and Core2Web team to provide us with this opportunity  ")
        line3 = QLabel("to present our project on this platform. OOP concepts ")
        line4 = QLabel("taught by sir has helped us to learn Pyqt from very beginning")
        line5 =QLabel("in short period of time ")
        line6 =QLabel("Thank you...  Rahul Dada for your valuable guidence")


       

        line7=QLabel("Groupleader :- Surabh Wagh")
        line8=QLabel("Members:-")
        line9=QLabel("Adinath Khose")
        line10=QLabel("Nachiket Bokade")
        line11=QLabel("Aditya Andhale")

        Title.setFont(QFont('Arial',20 ))
        line1.setFont(QFont('Arial',13 ))
        line2.setFont(QFont('Arial',13 )) 
        line3.setFont(QFont('Arial',13 )) 
        line4.setFont(QFont('Arial',13 ))
        line5.setFont(QFont('Arial',13 ))
        line6.setFont(QFont('Arial',13 ))
        line7.setFont(QFont('Arial',13 ))
        line8.setFont(QFont('Arial',13 )) 
        line9.setFont(QFont('Arial',12 )) 
        line10.setFont(QFont('Arial',12 ))
        line11.setFont(QFont('Arial',12 ))



        Title_box = QHBoxLayout()
        Title_box.setAlignment(Qt.AlignCenter)
        Title_box.setContentsMargins(250,300,250,50)

        line1_box = QHBoxLayout()
        line1_box.setAlignment(Qt.AlignCenter)
        line1_box.setContentsMargins(250,10,250,0)

        
        line2_box = QHBoxLayout()
        line2_box.setAlignment(Qt.AlignCenter)
        line2_box.setContentsMargins(250,10,250,0)

        line3_box = QHBoxLayout()
        line3_box.setAlignment(Qt.AlignCenter)
        line3_box.setContentsMargins(250,10,250,0)

        line4_box = QHBoxLayout()
        line4_box.setAlignment(Qt.AlignCenter)
        line4_box.setContentsMargins(250,10,250,0)

        line5_box = QHBoxLayout()
        line5_box.setAlignment(Qt.AlignCenter)
        line5_box.setContentsMargins(250,10,250,0)

        line6_box = QHBoxLayout()
        line6_box.setAlignment(Qt.AlignCenter)
        line6_box.setContentsMargins(100,27,250,0)

        line7_box = QHBoxLayout()
        line7_box.setAlignment(Qt.AlignCenter)
        line7_box.setContentsMargins(25,10,250,0)

        line8_box = QHBoxLayout()
        line8_box.setAlignment(Qt.AlignCenter)
        line8_box.setContentsMargins(10,10,320,0)

        line9_box = QHBoxLayout()
        line9_box.setAlignment(Qt.AlignCenter)
        line9_box.setContentsMargins(5,5,310,0)

        line10_box = QHBoxLayout()
        line10_box.setAlignment(Qt.AlignCenter)
        line10_box.setContentsMargins(5,5,310,0)

        line11_box = QHBoxLayout()
        line11_box.setAlignment(Qt.AlignCenter)
        line11_box.setContentsMargins(5,5,310,0)

        self.label = QLabel(self)
        
        img_box = QHBoxLayout()
        img_box.setAlignment(Qt.AlignCenter)
        img_box.setContentsMargins(1,10,10,10)
        

         
        # loading image
        self.pixmap = QPixmap('sir.png')
        
 
        # adding image to label
        self.label.setPixmap(self.pixmap)
 
        # Optional, resize label to image size
        self.label.resize(self.pixmap.width(),
                          self.pixmap.height())
        self.label.setContentsMargins(10,10,10,100)
        
        img_box.addWidget(self.label)
        Title_box.addWidget(Title)
        line1_box.addWidget(line1)
        line2_box.addWidget(line2)
        line3_box.addWidget(line3)
        line4_box.addWidget(line4)
        line5_box.addWidget(line5)
        line6_box.addWidget(line6)
        line7_box.addWidget(line7)
        line8_box.addWidget(line8)
        line9_box.addWidget(line9)
        line10_box.addWidget(line10)
        line11_box.addWidget(line11)




        thankyou_window.addRow(Title_box)
        thankyou_window.addRow(line1_box)
        thankyou_window.addRow(line2_box)
        thankyou_window.addRow(line3_box)
        thankyou_window.addRow(line4_box)
        thankyou_window.addRow(line5_box)
        thankyou_window.addRow(line6_box)
        thankyou_window.addRow(line7_box)
        thankyou_window.addRow(line8_box)
        thankyou_window.addRow(line9_box)
        thankyou_window.addRow(line10_box)
        thankyou_window.addRow(line11_box)

        self.setLayout( thankyou_window)

app4 = QApplication(sys.argv)
ex = Thanking()
ex.show()
sys.exit(app4.exec_())







        
    