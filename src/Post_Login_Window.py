import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QPushButton, QWidget, QLabel
from PyQt5.QtCore import Qt

class PostLoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Where's my Water")
        self.setGeometry(350,150,1200,800)
        layout = QVBoxLayout()

        button1 = QPushButton("Need a Tanker ?")
        button2 = QPushButton("Need Drinking Water ?")

        button1.setFixedSize(220,60)
        button2.setFixedSize(220,60)

        font = button1.font()
        font.setPointSize(12)  
        button1.setFont(font)

        font = button2.font()
        font.setPointSize(12)  
        button2.setFont(font)

        or_text = QLabel("Or" , self)
        
        layout.setAlignment(Qt.AlignCenter)
        or_text.setAlignment(Qt.AlignCenter)
        or_text.setStyleSheet("font-size: 20px;")

        layout.addWidget(button1)
        layout.addWidget(or_text)
        layout.addWidget(button2)

        self.setLayout(layout)
        print(self.children())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PostLoginWindow()
    window.show()
    sys.exit(app.exec_())