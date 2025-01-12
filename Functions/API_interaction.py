import requests
import urllib.parse

class ApiInteraction:
    def __init__(self, api_url, collection, geojson_path):
        self.api_url = api_url
        self.collection = collection
        self.geojson_path = geojson_path

    # function to create an url which searches for all items of a collection that intersect wit a GeoJSON polygon
    def request_search_intersection(self):
        # define request-parts
        base = self.api_url
        search = "search"
        collection = "?collections=" + str(self.collection)
        intersection = "&intersection=" + urllib.parse.quote(self.geojson_path) # url-encode GeoJSON
        limit = "&limit=20"

        # assemble url from parts
        self.request_url = base + search + collection + intersection + limit

        return self.request_url

    # function to get a response by executing a reqest
    def execute_request(self):
        # initialize response dicts
        payload = {}
        headers = {}

        response = requests.request("GET", self.request_url, headers=headers, data=payload)

        return response

    # function to get only id and download urls from the response JSON (only for .tif-files)
    def collect_tif_download_urls(self, response):
        # initialize dict for item-ids and the associated download-url
        id_with_link = {}

        # proof if request was successful
        if response.status_code == 200:
            response = response.json()

            for item in response["features"]:
                item_id = item["id"]
                download_url = item["assets"].get(self.collection + "-tif", {}).get("href")
                if download_url:
                    id_with_link[item_id] = download_url
        else:
            print(f"Error {self.request_url}: {response.status_code}")

        return id_with_link


# Example

# base API url DGM
api_url_dgm = "https://dgm.stac.lgln.niedersachsen.de/"
# collection name
collectiondgm1 = "dgm1"
# path to geojson
geojson = "C:/Users/julie/Documents/Julia/Master GeoInfSpat/ITSP/ITSP-Project/functions/polygon.geojson"

# create object from class ApiInteraction
dgm1_api_interaction = ApiInteraction(api_url_dgm, collectiondgm1, geojson)
# get request url for intersection
request = dgm1_api_interaction.request_search_intersection()
print(request)

# get response by executing request
response = dgm1_api_interaction.execute_request()

# get download url dict from response
url_dict = dgm1_api_interaction.collect_tif_download_urls(response)

# show dict and count
count = 0
for item_id, link in url_dict.items():
    count += 1
    print(f"{item_id}: {link}")
print(f"Total count: {count}")




