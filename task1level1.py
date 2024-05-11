#connecting the module with layouts
from PyQt5.QtCore import Qt
#connecting the required widgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout

#creating an application object
app = QApplication([])

# creating the main window object
my_win = QWidget()

# creating the name of the main window
my_win.setWindowTitle('My first app')

# setting the window size
my_win.resize(600, 200)

# giving the window the command to show up
my_win.show()

# creating a horizontal layout
line = QHBoxLayout()

# creating a text object
title = QLabel('Salaaam alaikom, haa application')
# # putting the text on the center of the layout
line.addWidget(title, alignment=Qt.AlignCenter)
# # adding the resulting line to the application window
my_win.setLayout(line)
app.exec_()

