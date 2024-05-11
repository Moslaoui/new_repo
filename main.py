import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel


class Screen1(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()
        self.label = QLabel("This is Screen 1")
        layout.addWidget(self.label)
        self.button = QPushButton("Go to Screen 2")
        self.button.clicked.connect(self.go_to_screen2)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def go_to_screen2(self):
        self.parent().change_screen(2)


class Screen2(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()
        self.label = QLabel("This is Screen 2")
        layout.addWidget(self.label)
        self.button1 = QPushButton("Go to Screen 1")
        self.button1.clicked.connect(self.go_to_screen1)
        layout.addWidget(self.button1)
        self.button2 = QPushButton("Go to Screen 3")
        self.button2.clicked.connect(self.go_to_screen3)
        layout.addWidget(self.button2)
        self.setLayout(layout)

    def go_to_screen1(self):
        self.parent().change_screen(1)

    def go_to_screen3(self):
        self.parent().change_screen(3)


class Screen3(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()
        self.label = QLabel("This is Screen 3")
        layout.addWidget(self.label)
        self.button = QPushButton("Go to Screen 2")
        self.button.clicked.connect(self.go_to_screen2)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def go_to_screen2(self):
        self.parent().change_screen(2)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple PyQt5 App")
        self.current_screen = None
        self.screen1 = Screen1(self)
        self.screen2 = Screen2(self)
        self.screen3 = Screen3(self)
        self.change_screen(1)

    def change_screen(self, screen_number):
        if self.current_screen:
            self.layout().removeWidget(self.current_screen)
            self.current_screen.hide()

        if screen_number == 1:
            self.current_screen = self.screen1
        elif screen_number == 2:
            self.current_screen = self.screen2
        elif screen_number == 3:
            self.current_screen = self.screen3

        self.layout().addWidget(self.current_screen)
        self.current_screen.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setGeometry(100, 100, 400, 300)
    window.show()
    sys.exit(app.exec_())
