from GUI_downloader import PolygonDownloader
import sys
from PyQt5.QtWidgets import QApplication


# Execution of GUI
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PolygonDownloader()
    window.show()
    sys.exit(app.exec_())

