import sys
from PyQt5.QtWidgets import *

class RasterDownloaderGUI(QMainWindow):
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

        # Tab 1: Raster Downloader
        self.tab1 = QWidget()
        self.tabs.addTab(self.tab1, "DGM1")
        self.create_tab1()

        # Tab 2: DOM1
        self.tab2 = QWidget()
        self.tabs.addTab(self.tab2, "DOM1")

        # Tab 3: Other Raster Data
        self.tab3 = QWidget()
        self.tabs.addTab(self.tab3, "Other available rasterdata ...")

    def create_tab1(self):
        layout = QVBoxLayout()
        self.tab1.setLayout(layout)

        # Polygon Input Section
        polygon_layout = QVBoxLayout()
        layout.addLayout(polygon_layout)

        polygon_label = QLabel("Polygon Input:")
        polygon_layout.addWidget(polygon_label)

        polygon_input_layout = QHBoxLayout()
        self.polygon_input = QLineEdit("file/path/to/shape-polygon/in EPSG 25832")
        polygon_input_layout.addWidget(self.polygon_input)
        browse_button = QPushButton("...")
        browse_button.clicked.connect(self.browse_file)
        polygon_input_layout.addWidget(browse_button)
        polygon_layout.addLayout(polygon_input_layout)

        reproject_layout = QHBoxLayout()
        self.reproject_checkbox = QCheckBox("Reproject data - from EPSG:")
        self.reproject_checkbox.stateChanged.connect(self.toggle_reproject_input)
        reproject_layout.addWidget(self.reproject_checkbox)
        self.epsg_input = QLineEdit()
        self.epsg_input.setEnabled(False)
        reproject_layout.addWidget(self.epsg_input)
        polygon_layout.addLayout(reproject_layout)

        # Raster Output Section
        raster_layout = QVBoxLayout()
        layout.addLayout(raster_layout)

        raster_label = QLabel("Raster Output:")
        raster_layout.addWidget(raster_label)

        raster_output_layout = QHBoxLayout()
        self.raster_output = QLineEdit("file/path/to/rasterdata output folder")
        raster_output_layout.addWidget(self.raster_output)
        browse_raster_button = QPushButton("...")
        browse_raster_button.clicked.connect(self.browse_folder)
        raster_output_layout.addWidget(browse_raster_button)
        raster_layout.addLayout(raster_output_layout)

        self.start_download_button = QPushButton("Start download")
        raster_layout.addWidget(self.start_download_button)

        # Raster 2 xyz Section
        raster2xyz_layout = QVBoxLayout()
        layout.addLayout(raster2xyz_layout)

        self.raster2xyz_checkbox = QCheckBox("Select files to convert manually?")
        self.raster2xyz_checkbox.stateChanged.connect(self.toggle_raster2xyz_input)
        raster2xyz_layout.addWidget(self.raster2xyz_checkbox)

        raster2xyz_output_layout = QHBoxLayout()
        self.raster2xyz_output = QLineEdit("file/path/to/rasterdata - default: download")
        self.raster2xyz_output.setEnabled(False)
        raster2xyz_output_layout.addWidget(self.raster2xyz_output)
        browse_raster2xyz_button = QPushButton("...")
        browse_raster2xyz_button.clicked.connect(self.browse_file)
        browse_raster2xyz_button.setEnabled(False)
        self.browse_raster2xyz_button = browse_raster2xyz_button
        raster2xyz_output_layout.addWidget(browse_raster2xyz_button)
        raster2xyz_layout.addLayout(raster2xyz_output_layout)

        self.start_raster2xyz_button = QPushButton("Start raster2xyz")
        raster2xyz_layout.addWidget(self.start_raster2xyz_button)

    def toggle_reproject_input(self, state):
        self.epsg_input.setEnabled(state == 2)  # 2 indicates the checkbox is checked

    def toggle_raster2xyz_input(self, state):
        enabled = state == 2  # 2 indicates the checkbox is checked
        self.raster2xyz_output.setEnabled(enabled)
        self.browse_raster2xyz_button.setEnabled(enabled)

    def browse_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select File")
        if file_name:
            self.polygon_input.setText(file_name)

    def browse_folder(self):
        folder_name = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder_name:
            self.raster_output.setText(folder_name)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = RasterDownloaderGUI()
    gui.show()
    sys.exit(app.exec_())