# Imports
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget

# Basics
app = QApplication(sys.argv) # sys.argv is standard to write inside

window = QWidget() # create new window
window.setGeometry(50, 50, 500, 500) # set starting point and size
window.setWindowTitle("Title") # set title
window.setWindowIcon(QIcon("LGLN Logo.png")) # set icon in the top left

window.show() # show the window

sys.exit(app.exec_()) # python program stops when window closes