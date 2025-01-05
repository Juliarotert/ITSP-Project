# Imports
import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


# create class window
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):
        # Buttons
        button1 = QPushButton('Start', self) # create button on self window
        #button1 = MyButton('Start', self)  # create button on self window
        button1.move(50, 200) # move button to another place

        # ToolTips
        QToolTip.setFont(QFont('Arial', 14))  # create ToolTip
        button1.setToolTip('Button <b>1</b>') # set tooltip for a Button

        # Reactions of button
        # standard: clicked (click and release over button)
        # pressed (click on button and release elsewhere)
        # released (any release going on)
        button1.clicked.connect(self.clicked) # execute button function
        #button1.pressed.connect(self.clicked)  # execute button function
        #button1.released.connect(self.clicked)  # execute button function
        #button1.clicked.connect(QtCore.QCoreApplication.instance().quit) # close window when button is clicked

        # Label
        c = QCheckBox("Check box", self)
        #c.toggle()
        c.move(50, 300)
        c.stateChanged.connect(self.clicked)

        p = QRadioButton('Check', self)
        p.setCheckable(True)
        p.move(50, 400)
        p.toggled.connect(self.clickedcheck)

        l = QLabel(self)
        l.setText("<a href=<'https://ni-lgln-opengeodata.hub.arcgis.com'>OpenGeoData</a>")
        l.setOpenExternalLinks(True)
        l.linkHovered.connect(self.clicked)
        l.move(50, 100)

        # Dropdown menu
        self.i = QComboBox(self)
        self.i.move(50, 150)
        self.i.addItem("java")
        self.i.addItem("python")
        self.i.addItem("c++")
        self.i.currentIndexChanged.connect(self.clickeditem)

        # Spinbox
        self.s = QSpinBox(self)
        self.s.move(50, 150)
        self.s.valueChanged.connect(self.clickedvalue)

        # Slider
        self.sl = QSlider(self)
        self.sl.move(300, 350)
        self.sl.valueChanged.connect(self.clickedvalue)
        self.sl.sliderMoved.connect(self.clickedvalue)
        self.sl.setMinimum(50)
        self.sl.setMaximum(100)
        self.sl.setValue(75)

        # Lineedit
        self.s = QLineEdit(self)
        self.s.move(50, 550)
        self.s.textChanged.connect(self.lineedit)

        # Window itself
        # Create function and action for menubar
        exitMe = QAction(QIcon('LGLN Logo.png'),'Exit', self)
        exitMe.setShortcut('Ctrl+Q')
        exitMe.setStatusTip('Exit')
        exitMe.triggered.connect(self.close)

        menubar = self.menuBar() # create a menubar
        start = menubar.addMenu('&Start') # Add menu to bar
        start.addAction(exitMe) # add action to start
        download = menubar.addMenu('Download')  # Add menu to bar
        download.addAction(exitMe)  # add action to download

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitMe)

        self.statusBar().showMessage('Statusbar') # create a statusbar
        self.setToolTip('click anywhere else') # create tooltip for the window background
        self.setGeometry(50, 50, 700, 1000)  # set starting point and size
        self.setWindowTitle("Title")  # set title
        self.setWindowIcon(QIcon("LGLN Logo.png"))  # set icon in the top left
        self.show()  # show the window

    # function for button click
    def clicked(self):
        sender = self.sender() # save sender of the signal (e.g. the button) as variable to edit its properties
        #sender.move(100, 100) # move the button after click
        print(sender.text() + ' ' + "Button clicked")

    def clickedcheck(self, down):
        if down:
            print("down")
        else:
            print("up")

    def clickeditem(self, i):
        print(self.i.currentText())

    def clickedvalue(self, i):
        print(self.s.value())

    def lineedit(self, text):
        print(text)

# Basics
app = QApplication(sys.argv) # sys.argv is standard to write inside

window = Window() # create new window

sys.exit(app.exec_()) # python program stops when window closes