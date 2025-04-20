# ports/profiling_port.py
from abc import ABC, abstractmethod
import pandas as pd

class ProfilingPort(ABC):
    """Defines how we generate a profile (EDA) of a dataset."""
    
    @abstractmethod
    def generate_report(self, df: pd.DataFrame) -> None:
        """Generate or display a data profiling report."""
        pass
