import argparse
import sys
import logging

# Adapters
from adapters.kaggle_downloader_adapter import KaggleDownloaderAdapter
from adapters.ydata_profiling_adapter import YDataProfilingAdapter
from adapters.dtale_adapter import DtaleAdapter
from adapters.pycaret_adapter import PyCaretAdapter

# Application
from application.use_cases import MLUseCases

# Configure basic logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Hexagonal ML Pipeline CLI")
    subparsers = parser.add_subparsers(dest="command")
    
    # download
    dl_parser = subparsers.add_parser("download", help="Download dataset from Kaggle")
    dl_parser.add_argument("kaggle_name", help="Kaggle dataset name (e.g. brsahan/mouse-viral-infection-study-dataset)")
    
    # profile
    profile_parser = subparsers.add_parser("profile", help="Generate profiling report")
    profile_parser.add_argument("csv_filename", help="Which CSV file to profile (in data/)?")
    
    # edit (Dtale)
    edit_parser = subparsers.add_parser("edit", help="Open data in Dtale and (optionally) save edits")
    edit_parser.add_argument("csv_filename", help="Which CSV file to edit (in data/)?")
    
    # train
    train_parser = subparsers.add_parser("train", help="Train a model using PyCaret")
    train_parser.add_argument("csv_filename", help="CSV in data/ to use for training")
    train_parser.add_argument("target_col", help="Target column (if classification/regression)")
    train_parser.add_argument("task_type", help="classification, regression, or clustering")
    
    args = parser.parse_args()
    
    # Instantiate adapters
    kaggle_adapter = KaggleDownloaderAdapter()     
    profiler_adapter = YDataProfilingAdapter()
    dtale_adapter = DtaleAdapter()
    training_adapter = PyCaretAdapter()
    
    # Create the use-case orchestrator with the chosen adapters
    ml_use_cases = MLUseCases(
        dataset_adapter=kaggle_adapter,
        profiler_adapter=profiler_adapter,
        dtale_adapter=dtale_adapter,
        training_adapter=training_adapter
    )
    
    if args.command == "download":
        logger.info("Authenticating with Kaggle...")
        kaggle_adapter.authenticate()
        logger.info("Authentication successful. Now downloading dataset...")
        ml_use_cases.download_dataset(args.kaggle_name, "data")
        logger.info("Download step finished.")
    
    elif args.command == "profile":
        logger.info(f"Generating ydata_profiling report for {args.csv_filename}...")
        ml_use_cases.profile_data(args.csv_filename)
        logger.info("Profile report generated. Check the current folder for an HTML file.")
    
    elif args.command == "edit":
        logger.info(f"Launching Dtale to edit {args.csv_filename}...")
        ml_use_cases.edit_data(args.csv_filename)
        logger.info(f"Dtale session opened. Check your console for the local Dtale URL.")
    
    elif args.command == "train":
        logger.info(f"Training a model on {args.csv_filename} | Target: {args.target_col} | Task: {args.task_type}")
        ml_use_cases.train_model(args.csv_filename, args.target_col, args.task_type)
        logger.info("Training complete.")
    
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
