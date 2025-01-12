from PyQt5.QtWidgets import QApplication
from gui import RasterDownloader
import sys




# Execution of GUI
if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = RasterDownloader()
    gui.show()
    sys.exit(app.exec_())