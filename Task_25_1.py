# Первая задача к двадцать пятому занятию

import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("C L I C K E R")
        self.nazh = 0

        self.button = QPushButton("CLICK HERE!")
        self.button.setFixedSize(QSize(200, 200))
        self.button.setCheckable(True)
        self.button.clicked.connect(self.the_button_was_clicked)

        self.label = QLabel("C L I C K E R")
        font = self.label.font()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        layout = QVBoxLayout()
        widgets = [self.label, self.button]
        for w in widgets:
            layout.addWidget(w)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.tf = True

    def the_button_was_clicked(self):
        self.nazh += 1
        print(f"Clicked {self.nazh} times!")
        # self.label.setText((str(self.nazh)))
        self.button.setText(str(self.nazh))
        self.setWindowTitle(str(self.nazh))


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
