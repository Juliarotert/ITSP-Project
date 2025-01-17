import requests

#import functions.api_interaction as ai


# Class to execute download-urls and save them
class OutputDownloader:
    def __init__(self, url_dict, output_folder):
        self.dict = url_dict
        self.output_folder = output_folder


    # function to download the files as id-name
    def download_dict_tif(self):
        total_number = len(self.dict)
        download_number = 0
        for id, url in self.dict.items():
            response = requests.get(url)
            file_path = f"{self.output_folder}/{id}.tif"
            with open(file_path, 'wb') as f:
                f.write(response.content)
            download_number += 1
            print(f"Downloaded {download_number}/{total_number}: {id}")

    # function to download the files as id-name
    def download_zip(self):
        for id, url in self.dict.items():
            response = requests.get(url)
            file_path = f"{self.output_folder}/{id}.zip"
            with open(file_path, 'wb') as f:
                f.write(response.content)


'''
# Example
# url-dict from the API-Interaction
dict = ai.url_dict

# output folder path
output_path = "C:/Users/julie/Documents/Julia/Master GeoInfSpat/ITSP/ITSP-Project/data/output test")

# download urls
od = OutputDownloader(dict, output_path)
od.download_dict_tif()
'''