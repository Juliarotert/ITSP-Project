import functions.input_processing as ip
import functions.api_interaction as ai
import functions.output_download as od

api_catalog_url = "https://dgm.stac.lgln.niedersachsen.de/"
collection = "dgm1"

input_polygon_path = "/data/test data/testpolygon_small_4647.shp"
output_folder = "C:/Users/julie/Documents/Julia/Master GeoInfSpat/ITSP/ITSP-Project/data/output test"


# Input processing
geojson_4326 = ip.ShapefileInputProcessing(input_polygon_path).button_ip()

# API Interaction
url_dict = ai.ApiInteraction(api_catalog_url, collection, geojson_4326).button_ai()

# Output download
od.OutputDownloader(url_dict, output_folder).download_dict_tif()