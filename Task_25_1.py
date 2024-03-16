# Первая задача к двадцать пятому занятию

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Application")
        self.count = 0
        self.button = QPushButton("Press Me!")
        # self.button.setCheckable(True)
        self.button.clicked.connect(self.the_button_was_clicked)
        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        self.count += 1
        self.button.setText(f"{self.count}")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
