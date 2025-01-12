import functions.api_interaction as ai
import requests
import time
from multiprocessing import cpu_count
from multiprocessing.pool import ThreadPool


class OutputDownloader:
    def __init__(self, url_dict, output_path):
        self.dict = url_dict
        self.output_path = output_path

    # download part based on https://towardsdatascience.com/use-python-to-download-multiple-files-or-urls-in-parallel-1759da9d6535
    # function to download urls
    def download_url(self, args):
        t0 = time.time()
        url, fn = args[0], args[1]
        try:
            r = requests.get(url)
            with open(fn, 'wb') as f:
                f.write(r.content)
            return (url, time.time() - t0)
        except Exception as e:
            print('Exception in download_url():', e)
            return (url, None)

    # function for parallel downloads
    def download_parallel(self, args):
        cpus = cpu_count()
        results = ThreadPool(cpus - 1).imap_unordered(self.download_url, args)
        for result in results:
            if result[1] is not None:
                print(f"Downloaded: {result[0]} in {result[1]:.2f} seconds")
            else:
                print(f"Failed to download: {result[0]}")

    # function to execute downloads to path
    def download_tif_files(self):
        file_names = []
        urls = []

        for id, url in self.dict.items():
            file_names.append(f"{self.output_path}/{id}.tif")
            urls.append(url)

        inputs = zip(urls, file_names)

        self.download_parallel(inputs)



# URL-Dictionary aus API-Interaction (korrigieren falls nötig)
dict = ai.url_dict

# Korrigierter Dateipfad
output_path = r"C:\Users\julie\Documents\Julia\Master GeoInfSpat\ITSP\ITSP-Project\data\Output_tests"
output_path = output_path.replace("\\", "/")

# Downloader-Objekt erstellen und Dateien herunterladen
od = OutputDownloader(dict, output_path)
od.download_tif_files()
