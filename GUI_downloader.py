import sys
from PyQt5.QtWidgets import *

import functions.input_processing as ip
import functions.api_interaction as ai
import functions.output_download as od

class PolygonDownloader(QMainWindow):
    def __init__(self):
        super().__init__()
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

        # raster output
        layout.addWidget(QLabel("Raster Output Folder:"))
        self.raster_output = QLineEdit()
        raster_layout = QHBoxLayout()
        raster_layout.addWidget(self.raster_output)
        raster_browse = QPushButton("...")
        raster_browse.clicked.connect(self.browse_raster_folder)
        raster_layout.addWidget(raster_browse)
        layout.addLayout(raster_layout)

        # start download button
        self.download_button = QPushButton("Start download")
        self.download_button.clicked.connect(self.start_download)
        layout.addWidget(self.download_button)

    # function to select polygon path
    def browse_polygon_shapefile(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Polygon File", "*.shp")
        if file_name:
            self.polygon_input.setText(file_name)

    def browse_raster_folder(self):
        folder_name = QFileDialog.getExistingDirectory(self, "Select Raster Output Folder")
        if folder_name:
            self.raster_output.setText(folder_name)

    def start_download(self):
        api_catalog_url = "https://dgm.stac.lgln.niedersachsen.de/"
        collection = "dgm1"

        input_polygon_path = self.polygon_input.text()
        output_folder = self.raster_output.text()
        print(f" input: {input_polygon_path}, output: {output_folder}")

        if not input_polygon_path or not output_folder:
            QMessageBox.warning(self, "Error", "Please select paths")
            return

        try:
            # Input processing
            geojson_4326 = ip.ShapefileInputProcessing(input_polygon_path).button_ip()

            # API Interaction
            url_dict = ai.ApiInteraction(api_catalog_url, collection, geojson_4326).button_ai()

            # Output download
            od.OutputDownloader(url_dict, output_folder).download_dict_tif()

        except Exception as e:
            print(f"An error occurred: {e}")

        QMessageBox.information(self, "Success", "Download finished")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PolygonDownloader()
    window.show()
    sys.exit(app.exec_())
