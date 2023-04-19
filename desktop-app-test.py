import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    layout = QHBoxLayout()
    btn = QPushButton("Click Here")
    layout.addWidget(btn)
    w.setLayout(layout)
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Desktop App')
    w.show()
    sys.exit(app.exec())
