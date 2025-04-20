# adapters\kaggle_downloader_adapter.py

import os
from abc import ABC, abstractmethod
from kaggle.api.kaggle_api_extended import KaggleApi

class IKaggleRepository(ABC):
    @abstractmethod
    def authenticate(self):
        pass
    
    @abstractmethod
    def download_dataset(self, dataset_name: str, path: str):
        pass
    
    @abstractmethod
    def get_dataset_metadata(self, dataset_name: str) -> dict:
        pass

class KaggleDownloaderAdapter(IKaggleRepository):
    """
    A Kaggle adapter that uses the Python API
    (kaggle.api.kaggle_api_extended) directly.
    """

    def __init__(self):
        self.api = KaggleApi()
        # We do NOT call authenticate() here,
        # so that the user can explicitly call it later if needed.

    def authenticate(self):
        """
        Perform the Kaggle API authentication. Make sure your kaggle.json
        is placed in ~/.kaggle or %HOMEPATH%\.kaggle (Windows).
        """
        self.api.authenticate()

    def download_dataset(self, dataset_name: str, path: str):
        os.makedirs(path, exist_ok=True)
        self.api.dataset_download_files(dataset_name, path=path, unzip=True)
        print(f"Downloaded '{dataset_name}' into '{path}'.")


    def get_dataset_metadata(self, dataset_name: str) -> dict:
        """
        Returns a dict with some metadata about the dataset (title, description, etc.).
        """
        dataset_info = self.api.dataset_view(dataset_name)
        metadata = {
            "title": dataset_info["title"],
            "description": dataset_info["description"],
            "size": dataset_info["size"],
            "last_updated": dataset_info["lastUpdated"],
            "tags": dataset_info["tags"],
            "url": dataset_info["url"]
        }
        return metadata
