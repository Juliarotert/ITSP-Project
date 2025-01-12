import geopandas as gpd


class ShapefileInputProcessing:
    def __init__(self, file_path):
        self.input_file = file_path
        self.shapefile = gpd.read_file(self.input_file)
        self.crs = self.shapefile.crs

    def reproject(self):
        if self.shapefile.crs.to_epsg() != 4326:
            self.shapefile = self.shapefile.to_crs('EPSG:4326')
        return self.shapefile

    def get_bbox(self):
        bbox = self.shapefile.bounds
        return bbox

    def convert_to_geojson(self, output_path='polygon.geojson'):
        self.shapefile.to_file(output_path, driver='GeoJSON')
        return output_path


'''
# Example
file_path = "C:/Users/julie/Documents/Julia/Master GeoInfSpat/ITSP/ITSP-Project/data/testpolygon.shp"

shapefile = ShapefileInputProcessing(file_path)
shapefile.reproject()
geojson = shapefile.convert_to_geojson()

print(f"saved as: {geojson}")
'''