# ports/training_port.py
from abc import ABC, abstractmethod
import pandas as pd

class TrainingPort(ABC):
    """Defines how we handle model training tasks."""
    
    @abstractmethod
    def train_model(self, df: pd.DataFrame, target: str, task_type: str):
        """
        Train a model depending on the task_type (classification, regression, or clustering).
        Return the trained model or any relevant object.
        """
        pass
