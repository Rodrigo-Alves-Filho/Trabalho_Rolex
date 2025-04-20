# ports/dataset_port.py
from abc import ABC, abstractmethod

class DatasetPort(ABC):
    """Defines how we fetch or load a dataset."""
    
    @abstractmethod
    def download_dataset(self, source_name: str) -> str:
        """
        Download a dataset from some source (e.g., Kaggle) and
        return the local path of the dataset CSV (or ZIP) file.
        """
        pass
