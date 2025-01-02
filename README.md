# ITSP-Project
Final Python Project for the ITSP Course in WS 24/25

## Short description of the project
In this project it's the goal to develop a tool for automated raster data download of polygonal area.

### Idea
**Problem:** Raster tile download at https://ni-lgln-opengeodata.hub.arcgis.com/ is only possible for single tiles or drawed polygon by user (But then you still have to download each selected tile manually). In land consolidation we have individual areas which intersect often with about 50 tiles. That means first trying to manually draw a good polygon like the procedure area and then 50 times pressing the download-button and select the path.
**Solution:** A Tool with an Input for polygon data, perform an intersection with the raster tiles and download all selected ones to one chosen output path.
**Optional extension:** creating xyz-files out of elevation raster data in chosen resolution (e.g. 1, 5, 10 m)
**First Try:** "DGM1" Data, extendable on all other raster data types in https://ni-lgln-opengeodata.hub.arcgis.com/

### Concept
**GUI:** 
- Selection of raster data Type (DGM, DOM, DOP, ...)
- Input of polygon data (or maybe choose to draw on website or other map??? or selection of other district boundaries (Verwaltungsgrenzen))
- Output path selection (or default to downloads)
- further functions button: xyz, transform to 4647, ...
### Realization
- Steps in Python

### Evaluation
- functionality
- difficulties

- extension to other open data APIs possible?

## How to start the project (dependencies etc.)
- PyQT
- Geopandas
