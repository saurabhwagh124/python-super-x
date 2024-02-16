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
        
        #adding textarea
        location_line = QLineEdit()
        location_line.setGeometry(0,0,200,60)

        #adding button
        submit_button = QPushButton("Submit")
        submit_button.setFixedSize(100,40)

        #creating boxes
        location_box = QHBoxLayout()
        location_box.setContentsMargins(420,250,400,0)

        #adding element in the box
        location_box.addWidget(location_label)
        location_box.addWidget(location_line)
        location_box.addWidget(submit_button)
        
        #adding layout
        Location_window.addRow(location_box)
        self.setLayout(Location_window)
        
app = QApplication(sys.argv)
obj = LocationWindow()
obj.show()
sys.exit(app.exec_())
