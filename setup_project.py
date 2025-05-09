import os
import urllib.request
import zipfile
import pandas as pd
import logging

# Configure Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def download_and_prepare_data(dest_folder="data"):
    os.makedirs(dest_folder, exist_ok=True)
    csv_path = os.path.join(dest_folder, "online_retail.csv")

    if os.path.exists(csv_path):
        logging.info("Dataset already exists at data/online_retail.csv")
        return

    url = "https://archive.ics.uci.edu/static/public/352/online+retail.zip"
    zip_path = os.path.join(dest_folder, "online_retail.zip")

    logging.info("Downloading dataset...")
    urllib.request.urlretrieve(url, zip_path)

    logging.info("Extracting dataset...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(dest_folder)

    # Find and convert .xls to .csv
    xls_file = next((f for f in os.listdir(dest_folder) if f.endswith(".xls")), None)
    if xls_file:
        xls_path = os.path.join(dest_folder, xls_file)
        logging.info("Converting .xls to .csv...")
        df = pd.read_excel(xls_path)
        df.to_csv(csv_path, index=False)
        os.remove(xls_path)
        logging.info(f"Dataset ready at: {csv_path}")
    else:
        logging.error("No .xls file found after extraction!")

    os.remove(zip_path)

if __name__ == "__main__":
    download_and_prepare_data()
