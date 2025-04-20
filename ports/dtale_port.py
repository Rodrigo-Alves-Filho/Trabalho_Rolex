# ports/dtale_port.py
from abc import ABC, abstractmethod
import pandas as pd

class DtalePort(ABC):
    """Defines how we show/edit data with Dtale."""
    
    @abstractmethod
    def open_in_dtale(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Launch dtale for interactive editing and
        return the edited dataframe.
        """
        pass
