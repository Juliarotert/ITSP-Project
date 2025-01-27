import requests
from PyQt5.QtWidgets import QApplication

#import api_interaction as ai


# Class to execute download-urls and save them
class OutputDownloader:
    def __init__(self, url_dict, output_folder):
        self.dict = url_dict
        self.output_folder = output_folder
        self.cancelled = False

    # function to set cancelled on True if it was cancelled
    def cancel_download(self):
        self.cancelled = True

    # function to download the files as id-name
    def download_dict_tif(self, progressbar=None):
        total_number = len(self.dict)
        download_number = 0

        # download and save each file from the dict
        for id, url in self.dict.items():
            # check if download was cancelled
            if self.cancelled:
                print("Download was cancelled")
                break

            # get and save url as "id.tif" to the folder
            response = requests.get(url)
            file_path = f"{self.output_folder}/{id}.tif"
            with open(file_path, 'wb') as f:
                f.write(response.content)

            # add one to the count of downloaded files for the progress
            download_number += 1
            print(f"Downloaded {download_number}/{total_number}: {id}")
            progressbar.setValue(download_number)
            QApplication.processEvents()



'''
# Example
# url-dict from the API-Interaction
dict = ai.url_dict

# output folder path
output_path = "Data/output test")

# download urls
od = OutputDownloader(dict, output_path)
od.download_dict_tif()
'''
