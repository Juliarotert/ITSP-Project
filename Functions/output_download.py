import functions.api_interaction as ai
import requests

from pathlib import Path

# Class to execute download-urls and save them
class OutputDownloader:
    def __init__(self, url_dict, output_folder):
        self.dict = url_dict
        self.output_folder = output_folder


    # function to download the files as id-name
    def download_dict_tif(self):
        for id, url in self.dict.items():
            response = requests.get(url)
            file_path = f"{self.output_folder}/{id}.tif"
            with open(file_path, 'wb') as f:
                f.write(response.content)

    # function to download the files as id-name
    def download_zip(self):
        for id, url in self.dict.items():
            response = requests.get(url)
            file_path = f"{self.output_folder}/{id}.tif"
            with open(file_path, 'wb') as f:
                f.write(response.content)



# Example
# url-dict from the API-Interaction
dict = ai.url_dict

# output filder path
output_path = Path(r"C:\Users\julie\Documents\Julia\Master GeoInfSpat\ITSP\ITSP-Project\data\output test")

# download urls
od = OutputDownloader(dict, output_path)
od.download_dict_tif()
