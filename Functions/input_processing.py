import geopandas as gpd
from pathlib import Path


# class with functions to process a shapefile from path
class ShapefileInputProcessing:
    def __init__(self, shapefile_path):
        self.shapefile_path = shapefile_path
        self.shapefile = gpd.read_file(self.shapefile_path)


    def reproject(self):
        crs = self.shapefile.crs
        if crs.to_epsg() != 4326:
            self.shapefile = self.shapefile.to_crs('EPSG:4326')
        return self.shapefile

    def get_bbox(self):
        bbox = self.shapefile.bounds
        return bbox

    def convert_to_geojson(self, output_name):
        output_path = Path.cwd() / "geojson output/" / output_name
        self.shapefile.to_file(output_path, driver='GeoJSON')
        return output_path

    def button_ip(self):
        self.reproject()
        geojson_path = self.convert_to_geojson("testpolygon_small_4326.geojson")
        return geojson_path



# Example final
geojson_path = ShapefileInputProcessing("C:/Users/julie/Documents/Julia/Master GeoInfSpat/ITSP/ITSP-Project/data/test data/testpolygon_small_4647.shp").button_ip()

print(geojson_path)

'''
# Example for tests
file_path = "C:/Users/julie/Documents/Julia/Master GeoInfSpat/ITSP/ITSP-Project/data/test data/testpolygon_small_4647.shp"

shapefile = ShapefileInputProcessing(file_path)
shapefile.reproject()
geojson = shapefile.convert_to_geojson("testpolygon_small_4326.geojson")

#geojson = shapefile.return_geojson()

print(f"saved as: {geojson}")
'''
