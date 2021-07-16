import urllib.request
from tqdm import tqdm
import os
from urllib.parse import urlparse

CACHE_LOCATION = os.path.join(os.path.expanduser('~'), 'pathways_python')


class DownloadProgressBar(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)

def download_url(url, output_path):
        with DownloadProgressBar(unit='B', unit_scale=True,
                                miniters=1, desc='downloading from pathways:') as t:
            urllib.request.urlretrieve(url, filename=output_path, reporthook=t.update_to)


class CacheManager():
    @staticmethod
    def cache_file(url: str) -> str:
        sections = urlparse(url)
        local_path = os.path.join(CACHE_LOCATION, sections.path)
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        download_url(url, local_path)
        return local_path

    @staticmethod
    def clear_cache():
        pass 