from kaggle.api.kaggle_api_extended import KaggleApi
import os
from dotenv import load_dotenv
from utils import FileUtils

load_dotenv()

logger = FileUtils.set_logger('extract_files')

def download_kaggle_dataset():
    """Downloads and unzips a dataset from Kaggle."""
    try:
        dataset_slug = os.getenv('DATA_SET')
        download_path = os.getenv('LOCAL_PATH')

        api = KaggleApi()
        api.authenticate()

        logger.info(f"Downloading Kaggle dataset: {dataset_slug} to path: {download_path}")
        api.dataset_download_files(dataset_slug, download_path, unzip=True)

        logger.info("Download and extraction complete.")
    except Exception as e:
        logger.info(f"Error downloading Kaggle dataset: {e}")

def main():
    download_kaggle_dataset()

if main == main:
    main()
