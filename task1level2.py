#connecting the module with layouts
from PyQt5.QtCore import Qt
#connecting the required widgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
app =  QApplication([])

my_wind = QWidget()

my_wind.setWindowTitle('My first app')

my_wind.resize(400,400)
button = QPushButton('Secret Button')
line = QVBoxLayout()
line.addWidget(button, alignment=Qt.AlignCenter)
# # adding the resulting line to the application window
my_wind.setLayout(line)

# #a function that creates and displays the second phrase
def show_fun_title():
    fun_title = QLabel('You are a miracle!')
    line.addWidget(fun_title, alignment = Qt.AlignCenter)
    my_wind.setLayout(line)

# # # # linking a button press to a function call
button.clicked.connect(show_fun_title)

my_wind.show()
app.exec_()