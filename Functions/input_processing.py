import geopandas as gpd


# class with functions to process a shapefile from path
class ShapefileInputProcessing:
    def __init__(self, shapefile_path):
        self.shapefile_path = shapefile_path
        self.shapefile = gpd.read_file(self.shapefile_path)


    # function to reproject if the CRS is different from EPSG 4326
    def reproject(self):
        crs = self.shapefile.crs
        if crs.to_epsg() != 4326:
            self.shapefile = self.shapefile.to_crs('EPSG:4326')
        return self.shapefile


    # function to get the bbox-coordinates
    def get_bbox(self):
        bbox = self.shapefile.bounds
        return bbox


    # function to convert the shapefile to geojson
    def convert_to_geojson(self, output_name = "Data/polygon_4326.geojson"):
        self.shapefile.to_file(output_name, driver='GeoJSON')
        return output_name


    # function for GUI-button executing all steps
    def button_ip(self):
        self.reproject()
        polygon_4326 = self.convert_to_geojson()
        return polygon_4326


'''
# Example final
geojson_path = ShapefileInputProcessing("Data/testdata/testpolygon_small_4647.shp").button_ip()
print(geojson_path)
'''

'''
# Example for tests
file_path = "Data/testdata/testpolygon_small_4647.shp"

shapefile = ShapefileInputProcessing(file_path)
shapefile.reproject()
geojson = shapefile.convert_to_geojson("polygon_4326.geojson")

#geojson = shapefile.return_geojson()

print(f"saved as: {geojson}")
'''
