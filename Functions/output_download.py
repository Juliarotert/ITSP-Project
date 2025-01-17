import requests
from PyQt5.QtWidgets import QApplication

#import functions.api_interaction as ai


# Class to execute download-urls and save them
class OutputDownloader:
    def __init__(self, url_dict, output_folder):
        self.dict = url_dict
        self.output_folder = output_folder
        self.cancelled = False

    # function to download the files as id-name
    def download_dict_tif(self, progressbar=None):
        total_number = len(self.dict)
        download_number = 0

        # download and save each file from the dict
        for id, url in self.dict.items():
            if self.cancelled:
                print("Download was cancelled")
                break
            response = requests.get(url)
            file_path = f"{self.output_folder}/{id}.tif"
            with open(file_path, 'wb') as f:
                f.write(response.content)

            download_number += 1
            print(f"Downloaded {download_number}/{total_number}: {id}")
            progressbar.setValue(download_number)
            QApplication.processEvents()
        self.cancelled = False

    def cancel_download(self):
        self.cancelled = True


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