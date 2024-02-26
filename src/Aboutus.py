import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import *


class AboutUs(QWidget):
     def _init_(self):
        super()._init_()
        self.setWindowTitle("About Us")
        self.setGeometry(350,150,1200,800)

     def thankyou_ui(self):
        thankyou_window=QFormLayout()
        Title = QLabel("Gratitute to Shashi Sir and Core2Web Family")
        line1 = QLabel("Our team would like to express gratitude to Shashi Sir")
        line2 = QLabel("and Core2Web team to provide us with this opportunity  ")
        line3 = QLabel("to present our project on this platform. ")
        linerahul  = QLabel("Mentor:- Rahul Dada")
        line7=QLabel("Groupleader :- Saurabh Wagh")
        line8=QLabel("Members:- Adinath Khose, Nachiket Bokade, Aditya Andhale ")

        Title.setFont(QFont('Arial',20 ))
        line1.setFont(QFont('Arial',13 ))
        line2.setFont(QFont('Arial',13 )) 
        line3.setFont(QFont('Arial',13 )) 
        linerahul.setFont(QFont('Arial',13))
        line7.setFont(QFont('Arial',13 ))
        line8.setFont(QFont('Arial',13 ))
        self.back = QPushButton("Back")
        self.back.setStyleSheet("QPushButton::hover"
                     "{"
                     "background-color : lightgreen;border-radius: 10px ;border-style: outset;"
                     "}"
                     "QPushButton"
                             "{"
                             "background-color :  lightyellow;border-radius: 10px ;border-style: outset;"
                             "}")
        self.back.setFont(QFont("Arial",12))
        self.back.setFixedSize(100,40)


        img_box = QHBoxLayout()
        img_box.setAlignment(Qt.AlignCenter)
        img_box.setContentsMargins(10,10,10,10)




        Title_box = QHBoxLayout()
        Title_box.setAlignment(Qt.AlignCenter)
        Title_box.setContentsMargins(250,40,250,0)
        Title.setStyleSheet("font-weight: bold")

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
        line6_box.setContentsMargins(100,27,100,0)

        linerahul_box = QHBoxLayout()
        linerahul_box.setAlignment(Qt.AlignCenter)
        linerahul_box.setContentsMargins(45,10,250,0)

        line7_box = QHBoxLayout()
        line7_box.setAlignment(Qt.AlignCenter)
        line7_box.setContentsMargins(45,10,250,0)

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
        self.pixmap = QPixmap('src/sir.jpg')
        self.pixmap.scaled(100,100,)
        
        self.label.setPixmap(self.pixmap)
        
        self.label.setAlignment(Qt.AlignCenter)
        
      #   img_box.addWidget(self.label)
        img_box.addWidget(self.label)
        Title_box.addWidget(Title)
        line1_box.addWidget(line1)
        line2_box.addWidget(line2)
        line3_box.addWidget(line3)
        linerahul_box.addWidget(linerahul)
        line7_box.addWidget(line7)
        line8_box.addWidget(line8)
        

        background_color = QColor(135, 206, 250)  # Light Sky Blue
        palette = QPalette()
        palette.setColor(QPalette.Window, background_color)
        self.setPalette(palette)

        white_palette = QPalette()
        white_palette.setColor(QPalette.WindowText, QColor(255,255,255))

      #   for label in [ Title,line1,line2, line3, line7, line8]:
      #       label.setPalette(white_palette)


        thankyou_window.addRow(img_box)
        thankyou_window.addRow(Title_box)
        thankyou_window.addRow(line1_box)
        thankyou_window.addRow(line2_box)
        thankyou_window.addRow(line3_box)
        thankyou_window.addRow(linerahul_box)
        thankyou_window.addRow(line7_box)
        thankyou_window.addRow(line8_box)
        
        thankyou_window.addRow(self.back)


        return thankyou_window
