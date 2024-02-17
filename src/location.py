import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QSize

class LocationWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Location window")
        self.setGeometry(350,150,1200,800)
        self.LocationWindow_Ui()

    def LocationWindow_Ui(self):
        
        Location_window = QFormLayout()

        #creating labels
        location_label = QLabel("Location : ")
        water_provider1 = QLabel("1.Saurabh water supplyers")
        water_provider2 = QLabel("2.Nachiket Water provider")
        water_provider3 = QLabel("3.Aditya Waters")

        
        #adding textarea
        location_line = QLineEdit()
        location_line.setGeometry(0,0,200,60)

        #adding button
        submit_button = QPushButton("Submit")
        submit_button.setFixedSize(100,40)

        saurab_water_button = QPushButton("Order")
        nachiket_water_button = QPushButton("Order")
        aditya_water_button = QPushButton("Order")
        
        saurab_water_button.setFixedSize(100,40)
        nachiket_water_button.setFixedSize(100,40)
        aditya_water_button.setFixedSize(100,40)
        #creating boxes
        location_box = QHBoxLayout()
        location_box.setContentsMargins(300,250,300,0)

        saurab_water_box = QHBoxLayout()
        saurab_water_box.setContentsMargins(300,50,300,0)
        nachiket_water_box = QHBoxLayout()
        nachiket_water_box.setContentsMargins(300,25,300,0)
        aditya_water_box = QHBoxLayout()
        aditya_water_box.setContentsMargins(300,25,300,0)


        #adding element in the box
        location_box.addWidget(location_label)
        location_box.addWidget(location_line)
        location_box.addWidget(submit_button)
        
        saurab_water_box.addWidget(water_provider1)
        saurab_water_box.addWidget(saurab_water_button)

        nachiket_water_box.addWidget(water_provider2)
        nachiket_water_box.addWidget(nachiket_water_button)
        
        aditya_water_box.addWidget(water_provider3)
        aditya_water_box.addWidget(aditya_water_button)



        #adding layout
        Location_window.addRow(location_box)

        Location_window.addRow(saurab_water_box)
        Location_window.addRow(nachiket_water_box)
        Location_window.addRow(aditya_water_box)

        self.setLayout(Location_window)
        





        #Adding fonts
        font = self.font()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.setFont(font)




app = QApplication(sys.argv)
obj = LocationWindow()
obj.show()
sys.exit(app.exec_())
