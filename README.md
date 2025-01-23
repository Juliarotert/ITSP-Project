# Polygon Download Tool for LGLN OpenGeoData (DGM1)
**Final python-project for the Introduction to Software Programming course in wintersemester 24/25 at IFGI (University of Münster)**

## Short description of the project
This projects goal is to develop a tool to download DGM1 raster tiles intersecting a polygonal area using the STAC-API by LGLN.
  
### Background and Idea
**Problem:** Raster tile download at https://ni-lgln-opengeodata.hub.arcgis.com/ is only possible for single tiles or drawed geometries by user (But then you still have to download each selected tile manually). In land consolidation we have individual areas which often intersect with about 50 tiles. That means first manually draw a fitting polygon like the procedure area and then 50 times pressing the download-button and selecting the path.

**Solution:** A Tool with an Input for polygon data as a shapefile, perform an intersection with the raster tiles and download all selected ones to one chosen output path.

### Concept
**GUI:** 
- Selection of raster data Type (DGM, DOM, DOP, ...)
- Input of polygon data (or maybe choose to draw on website or other map??? or selection of other district boundaries (Verwaltungsgrenzen))
- Output path selection (or default to downloads)

**Project Structure**
- functions folder: files for classes with functions for processing
- GUI: Input, Output, Buttons
- main: Execute program
- testdata, documentation, etc.

**Functionalities**

Downloader:
- start GUI
- choose I/O
- Button "start download": reprojection, conversion, request, get download-links, execute links to path


**Using STAC-API**
- STAC-API catalog: https://dgm.stac.lgln.niedersachsen.de/
- API description: https://dgm.stac.lgln.niedersachsen.de/api.html


## How to start the project
**Requirements:**
- Python 3.8 or higher (ensure that pip is installed)
```bash
# check the version with 
python --version
# or
python3 --version

# Install pip 
python -m ensurepip
# or update pip
python -m pip install --upgrade pip
```
**Steps:**
- Clone the repository and navigate to the project-folder
```bash
# 1.
cd /path/to/targetdirectory 
# 2. 
git clone https://github.com/Juliarotert/ITSP-Project.git
# 3.
cd ITSP-Project
```
- Set up a virtual environment
```bash
# 4.
pip install virtualenv
# 5. 
python -m venv .venv  
# 6.
.\.venv\Scripts\activate.ps1  
```
- Install the dependencies
```bash
# 7.
pip install -r requirements.txt
```
- Run in terminal
```bash
python main.py
```
- Run in IDE: open main.py or do a right-click on it and run it