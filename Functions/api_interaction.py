import requests
import json
#from pathlib import Path
#import input_processing as ip


# Class to create and send request-urls and process the response
class ApiInteraction:
    def __init__(self, api_catalog_url, collection_id, geojson_path):
        self.api_catalog_url = api_catalog_url
        self.collection_id = collection_id
        self.geojson_path = geojson_path


    # function to format the geojson file fitting for the request-url
    def format_geojson_geometry(self):
        # open and read the GeoJSON-file and extract the data
        with open(self.geojson_path, 'r') as geojson_file:
            data = json.load(geojson_file)

        # only return the geometry of the geojson
        geojson_geometry = json.dumps(data["features"][0]["geometry"],  ensure_ascii=False)

        # return a geojson without Spaces
        formatted_geojson_geometry = geojson_geometry.replace(" ", "")

        return formatted_geojson_geometry


    # function to create an url which searches for all items of a collection that intersect wit a GeoJSON polygon
    def create_request_search_intersects(self, limit, formatted_geojson_geometry):
        # define request-parts
        base = self.api_catalog_url
        search = "search"
        collection = "?collections=" + str(self.collection_id)
        intersects = "&intersects=" + formatted_geojson_geometry
        limit = "&limit=" + str(limit)

        # assemble url from parts
        request_url = base + search + collection + intersects + limit

        return request_url


    # function to get a response by executing a request
    def execute_request(self, request_url):
        # initialize response dicts
        payload = {}
        headers = {}

        response = requests.request("GET", request_url, headers=headers, data=payload)

        return response


    # function to get only id and download urls from the response JSON (only for .tif-files)
    def collect_tif_download_urls(self, response):
        # initialize dict for item-ids and the associated download-url
        dict_id_with_url = {}

        # proof if request was successful and turn response to json
        if response.status_code == 200:
            response_json = response.json()

            # iterate through items and add id and download url to dict
            for item in response_json["features"]:
                item_id = item["id"]
                first_asset_object = list(item["assets"].keys())[0] # download-link is always in the first asset object
                download_url = item["assets"][first_asset_object]["href"] # get href from first asset
                dict_id_with_url[item_id] = download_url
        else:
            print(f"Error: {response.status_code}")

        return dict_id_with_url

    # function for GUI-button executing all steps
    def button_ai(self):
        formatted_geojson_geometry = self.format_geojson_geometry()
        request_url = self.create_request_search_intersects(500, formatted_geojson_geometry)
        response = self.execute_request(request_url)
        dict_id_with_url = self.collect_tif_download_urls(response)

        return dict_id_with_url


'''
# Example final
# create object from class ApiInteraction
url_dict = ApiInteraction("https://dgm.stac.lgln.niedersachsen.de/", "dgm1", ip.geojson_path).button_ai()
print(url_dict)
'''

'''
# Example for tests

# base API url DGM
api_url_dgm = "https://dgm.stac.lgln.niedersachsen.de/"

# collection name
collectiondgm1 = "dgm1"

# path to geojson
geojson = str(Path.cwd()) + "/geojson output/testpolygon_small_4326.geojson"

# create object from class ApiInteraction
dgm1_api_interaction = ApiInteraction(api_url_dgm, collectiondgm1, geojson)

# format
formatted_geojson = dgm1_api_interaction.format_geojson_geometry()

# get request url for intersection
request = dgm1_api_interaction.create_request_search_intersects(500, formatted_geojson)
print(request)

# get response by executing request
response = dgm1_api_interaction.execute_request(request)

# get download url dict from response
url_dict = dgm1_api_interaction.collect_tif_download_urls(response)

# show dict and count
count = 0
for item_id, link in url_dict.items():
    count += 1
    print(f"{item_id}: {link}")
print(f"Total count: {count}")
'''
