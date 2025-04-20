# adapters/pycaret_adapter.py
import pandas as pd
from ports.training_port import TrainingPort

# PyCaret tasks
from pycaret.classification import setup as class_setup, compare_models as class_compare
from pycaret.regression import setup as reg_setup, compare_models as reg_compare
from pycaret.clustering import setup as clus_setup, create_model as clus_create

class PyCaretAdapter(TrainingPort):
    def train_model(self, df: pd.DataFrame, target: str, task_type: str):
        """
        Use PyCaret to train. We'll just return the best model object.
        """
        if task_type == "classification":
            class_setup(data=df, target=target, session_id=123, html=False)
            best_model = class_compare()
            print("Best Classification Model:", best_model)
            return best_model
        
        elif task_type == "regression":
            reg_setup(data=df, target=target, session_id=123, html=False)
            best_model = reg_compare()
            print("Best Regression Model:", best_model)
            return best_model
        
        elif task_type == "clustering":
            clus_setup(data=df, session_id=123, html=False)
            best_model = clus_create("kmeans")
            print("Clustering Model:", best_model)
            return best_model
        
        else:
            raise ValueError("Invalid task_type. Choose classification, regression, or clustering.")
