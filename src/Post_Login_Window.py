import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QPushButton, QWidget, QLabel
from PyQt5.QtCore import Qt

class PostLoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Where's my Water")
        self.setGeometry(350,150,1200,800)
        layout = QVBoxLayout()

        tanker_button = QPushButton("Need a Tanker ?")
        drinking_button = QPushButton("Need Drinking Water ?")

        tanker_button.setFixedSize(220,60)
        drinking_button.setFixedSize(220,60)

        font = tanker_button.font()
        font.setPointSize(12)  
        tanker_button.setFont(font)

        font = drinking_button.font()
        font.setPointSize(12)  
        drinking_button.setFont(font)

        or_text = QLabel("Or" , self)
        
        layout.setAlignment(Qt.AlignCenter)
        or_text.setAlignment(Qt.AlignCenter)
        or_text.setStyleSheet("font-size: 20px;")

        layout.addWidget(tanker_button)
        layout.addWidget(or_text)
        layout.addWidget(drinking_button)

        self.setLayout(layout)
        print(self.children())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PostLoginWindow()
    window.show()
    sys.exit(app.exec_())