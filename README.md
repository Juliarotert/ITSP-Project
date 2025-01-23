# Polygon Download Tool for LGLN OpenGeoData (DGM1)
**Final python-project for the Introduction to Software Programming course in wintersemester 24/25 at IFGI (University of Münster)**

## Short description of the project
This projects goal is to develop a tool to download DGM1 raster tiles intersecting a polygonal area using the STAC-API by LGLN (Landesamt für Geoinformation und Landesvermessung Niedersachsen). This tool should simplily the download procedure for land consolidation procedure areas at the ArL (Amt für regionale Landesentwicklung).
  
### Background and Idea
**Problem:** The raster tile download at the [OpenGeoData download application](https://ni-lgln-opengeodata.hub.arcgis.com/) is only possible for single tiles or geometries drawn by user still needing to download each selected tile manually. In land consolidation there are very individual areas which often intersect with about 50 tiles. That means first manually draw a fitting polygon and then 50 times pressing the download-button and selecting the path.

**Solution:** A tool with an input for polygon data as a shapefile, perform an intersection with the raster tiles and download all selected ones to one chosen output path.

### Concept
**Project structure**
- Classes: for input-processing, API-interaction and download
- GUI: Input-/output-dialog, start/cancel download button, progressbar
- main.py: Executes the program

<img src="Media/GUI.png" width="300">

**LGLN STAC-API**

By sending a GET-request with the query-parameters "collections" (dgm1) and "intersects" (GeoJSON-geometry) to the API, the items that intersect the polygon can be selected. To each item there is a download-url assigned which can be fetched.
- STAC-API catalog: https://dgm.stac.lgln.niedersachsen.de/
- API description: https://dgm.stac.lgln.niedersachsen.de/api.html


## How to start the project
**Requirements:**

Python 3.8 or higher (ensure that pip is installed)
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

Clone the repository and navigate to the project-folder
```bash
# 1.
cd /path/to/targetdirectory 
# 2. 
git clone https://github.com/Juliarotert/ITSP-Project.git
# 3.
cd ITSP-Project
```
Set up a virtual environment
```bash
# 4.
pip install virtualenv
# 5. 
python -m venv .venv  
# 6.
.\.venv\Scripts\activate.ps1  
```
Install the dependencies
```bash
# 7.
pip install -r requirements.txt
```
Run in terminal
```bash
python main.py
```
Run in IDE: open main.py or do a right-click on it and run it