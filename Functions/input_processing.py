from geopandas import geopandas as gpd

# read polygon
# reproject polygon
# intersect polygon
# create output list with selected tiles

path = "C:/Users/julie/Documents/Julia\Master GeoInfSpat/ITSP/ITSP-Project/data/testpolygon.shp"

shapefile = gpd.read_file(path)

print(shapefile.crs)
print(list(shapefile.bounds))


class InputProcessing:
    def __init__(self, file_path):
        self.input_file = file_path


    def read_input_file(self):
        self.shapefile = gpd.read_file(self.input_file)
        return self.shapefile

    def get_crs(self):
        self.crs = shapefile.crs
        return self.crs

    def reproject(self, crs):
        if self.crs != 4326:
            self.shapefile_4326 = shapefile.to_crs({'init': 'epsg:4326'})
        return self.shapefile_4326

    def get_bbox(self):
        if self.crs != 4326:
            self.bbox = self.shapefile_4326.bounds
        else:
            self.bbox = self.shapefile.bounds
        return self.bbox






