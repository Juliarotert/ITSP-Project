import gui

import functions.input_processing as ip
import functions.api_interaction as api
import functions.output_download as od
import functions.raster2xyz as xyz


# Execution of functions from classes

# Get data input from GUI

polygon_path = gui.getshapefile()

epsg = gui.QLineEdit