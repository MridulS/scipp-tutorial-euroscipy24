import tarfile
from pathlib import Path

data_p = Path('data/')

def extract_tar_gz(
    file_path,
):
    with tarfile.open(file_path, "r:gz") as tar:
        tar.extractall(path=data_p, filter="data")
        print(f"Extracted {file_path}")


data_path = Path(data_p/"nyc_taxi_data_2015_small.tar.gz")
extract_tar_gz(data_path)
