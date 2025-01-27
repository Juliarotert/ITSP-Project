from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QFileDialog, QLineEdit, QPushButton,
    QMessageBox, QProgressBar, QApplication)
from PyQt5.QtGui import QIcon


import Functions.input_processing as ip
import Functions.api_interaction as ai
import Functions.output_download as od


class PolygonDownloader(QMainWindow):
    def __init__(self):
        super().__init__()
        # basic window properties
        self.setWindowIcon(QIcon('Media/PolygonDownloader_Logo.png'))
        self.setWindowTitle("DGM1 Polygondownloader")
        self.setGeometry(200, 200, 500, 200)

        # central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # polygon input
        layout.addWidget(QLabel("Polygon Input (.shp-file):"))
        self.polygon_input = QLineEdit()
        polygon_layout = QHBoxLayout()
        polygon_layout.addWidget(self.polygon_input)
        polygon_browse = QPushButton("...")
        polygon_browse.clicked.connect(self.browse_polygon_shapefile)
        polygon_layout.addWidget(polygon_browse)
        layout.addLayout(polygon_layout)

        layout.addSpacing(20)

        # raster output
        layout.addWidget(QLabel("Output Folder:"))
        self.output = QLineEdit()
        output_layout = QHBoxLayout()
        output_layout.addWidget(self.output)
        output_browse = QPushButton("...")
        output_browse.clicked.connect(self.browse_output_folder)
        output_layout.addWidget(output_browse)
        layout.addLayout(output_layout)

        layout.addSpacing(20)

        # start download button
        self.download_button = QPushButton("Start download")
        self.download_button.clicked.connect(self.start_download)
        layout.addWidget(self.download_button)

        layout.addSpacing(20)

        # progress bar
        self.progressbar = QProgressBar()
        layout.addWidget(self.progressbar)

    # function to select polygon path
    def browse_polygon_shapefile(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Polygon File", "*.shp")
        if file_name:
            self.polygon_input.setText(file_name)

    # function to select output folder
    def browse_output_folder(self):
        folder_name = QFileDialog.getExistingDirectory(self, "Select Output Folder")
        if folder_name:
            self.output.setText(folder_name)

    # function to execute all relevant Functions to download the Data
    def start_download(self):
        api_catalog_url = "https://dgm.stac.lgln.niedersachsen.de/"
        collection = "dgm1"
        input_polygon_path = self.polygon_input.text()
        output_folder = self.output.text()

        print(f" input: {input_polygon_path}, output: {output_folder}")

        # show error it there is a missing path
        if not input_polygon_path or not output_folder:
            QMessageBox.warning(self, "Error", "Please select paths")
            return

        try:
            # Input processing
            geojson_4326 = ip.ShapefileInputProcessing(input_polygon_path).button_ip()

            # API Interaction
            url_dict = ai.ApiInteraction(api_catalog_url, collection, geojson_4326).button_ai()

            # show a message about the count of returned items
            QMessageBox.information(self, "Selection", f"{len(url_dict)} Items selected")

            # create a progress bar depending on the count of items
            self.progressbar.setMaximum(len(url_dict))

            # create a downloader object and
            downloader = od.OutputDownloader(url_dict, output_folder)

            self.download_button.disconnect()
            self.download_button.clicked.connect(downloader.cancel_download)
            self.download_button.setText("Cancel download")

            # output download
            print("Starting download")

            #
            QApplication.processEvents()
            downloader.download_dict_tif(self.progressbar)
            if downloader.cancelled is True:
                QMessageBox.information(self, "Cancelled", f"Download cancelled")


        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            self.download_button.disconnect()
            self.download_button.setText("Start download")
            self.download_button.clicked.connect(self.start_download)

