import sys
from PyQt5.QtWidgets import *
import os

# import all functions for buttons
import functions.input_processing as ip
import functions.api_interaction as ai
import functions.output_download as od
import functions.raster2xyz as xyz


class RasterDownloader(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OpenGeoData NI Rasterdownloader")
        self.setGeometry(100, 100, 600, 400)

        # Main widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # Tabs
        self.tabs = QTabWidget()
        main_layout.addWidget(self.tabs)

        # Tab 1: DGM1
        self.tab1 = QWidget()
        self.tabs.addTab(self.tab1, "DGM1")
        self.create_tab("dgm1", "https://dgm.stac.lgln.niedersachsen.de/")

        # Tab 2: DOM1
        #self.tab2 = QWidget()
        #self.tabs.addTab(self.tab2, "DOM1")

        # Tab 3: Other Raster Data
        #self.tab3 = QWidget()
        #self.tabs.addTab(self.tab3, "Other available rasterdata ...")

    def create_tab(self, collection_id, base_url):
        self.collection = collection_id
        self.url = base_url + collection_id

        layout = QVBoxLayout()
        self.tab1.setLayout(layout)

        # Polygon input part
        polygon_layout = QVBoxLayout()
        layout.addLayout(polygon_layout)

        polygon_label = QLabel("Polygon Input:")
        polygon_layout.addWidget(polygon_label)

        polygon_input_layout = QHBoxLayout()
        self.polygon_input = QLineEdit("select file path to shape-polygon")
        polygon_input_layout.addWidget(self.polygon_input)
        browse_button = QPushButton("...")
        browse_button.clicked.connect(self.browse_shape_file)
        polygon_input_layout.addWidget(browse_button)
        polygon_layout.addLayout(polygon_input_layout)


        # Raster output part
        raster_layout = QVBoxLayout()
        layout.addLayout(raster_layout)

        raster_label = QLabel("Raster Output:")
        raster_layout.addWidget(raster_label)

        raster_output_layout = QHBoxLayout()
        self.raster_output = QLineEdit("select file path to rasterdata output folder")
        raster_output_layout.addWidget(self.raster_output)
        browse_raster_button = QPushButton("...")
        browse_raster_button.clicked.connect(self.browse_folder)
        raster_output_layout.addWidget(browse_raster_button)
        raster_layout.addLayout(raster_output_layout)

        start_download_button = QPushButton("Start download")
        start_download_button.clicked.connect(self.start_download)
        raster_layout.addWidget(start_download_button)

        if self.collection in ("dgm1", "dom1"):
            # Raster 2 xyz Section
            raster2xyz_layout = QVBoxLayout()
            layout.addLayout(raster2xyz_layout)

            raster2xyz_label = QLabel("Raster to xyz:")
            raster2xyz_layout.addWidget(raster2xyz_label)

            self.raster2xyz_checkbox = QCheckBox("Select files to convert manually?")
            self.raster2xyz_checkbox.stateChanged.connect(self.toggle_raster2xyz_input)
            raster2xyz_layout.addWidget(self.raster2xyz_checkbox)

            raster2xyz_input_layout = QHBoxLayout()
            self.raster2xyz_input = QLineEdit("default: previously downloaded files")
            self.raster2xyz_input.setEnabled(False)
            raster2xyz_input_layout.addWidget(self.raster2xyz_input)
            browse_raster2xyz_button = QPushButton("...")
            browse_raster2xyz_button.clicked.connect(self.browse_tif_file)
            browse_raster2xyz_button.setEnabled(False)
            self.browse_raster2xyz_button = browse_raster2xyz_button
            raster2xyz_input_layout.addWidget(browse_raster2xyz_button)
            raster2xyz_layout.addLayout(raster2xyz_input_layout)

            self.start_raster2xyz_button = QPushButton("Start raster2xyz")
            raster2xyz_layout.addWidget(self.start_raster2xyz_button)


    # functions for buttons
    def toggle_raster2xyz_input(self, state):
        enabled = state == 2  # 2 indicates the checkbox is checked
        self.raster2xyz_input.setEnabled(enabled)
        self.browse_raster2xyz_button.setEnabled(enabled)

    def browse_shape_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select File", "*.shp")
        if file_name:
            self.polygon_input.setText(file_name)

    def browse_tif_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select File", "*.tif")
        if file_name:
            self.raster2xyz_input.setText(file_name)

    def browse_folder(self):
        folder_name = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder_name:
            self.raster_output.setText(folder_name)


    # Execution of all processing and downloading functions from ip, ai and od
    def start_download(self):
        try:
            url = self.url
            collection = self.collection
            file_path = self.polygon_input.text()

            # Input processing
            shapefile = ip.ShapefileInputProcessing(file_path)
            shapefile.reproject()
            geojson = shapefile.convert_to_geojson()

            # API Interaction
            api_info = ai.ApiInteraction(url, collection, geojson)
            # get request url for intersection (with limit)
            limit = 20
            request = api_info.request_search_intersection(limit)
            # get response by executing request
            response = api_info.execute_request()
            # get download url dict from response
            url_dict = api_info.collect_tif_download_urls()

            # Output download
            output_path = self.raster_output.text()
            output_path = os.path.normpath(output_path)

            # create downloader object
            downloader = od.OutputDownloader(url_dict, output_path)
            downloader.download_tif_files()


        except Exception as e:
            print(f"a wild error occurred: {e}")





# put into main later!!!!
if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = RasterDownloader()
    gui.show()
    sys.exit(app.exec_())