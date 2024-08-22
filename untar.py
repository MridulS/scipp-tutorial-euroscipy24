import tarfile
from pathlib import Path


def extract_tar_gz(
    file_path,
):
    with tarfile.open(file_path, "r:gz") as tar:
        tar.extractall(path=Path("."), filter="data")
        print(f"Extracted {file_path}")


data_path = Path("nyc_taxi_data_2015_small.tar.gz")
extract_tar_gz(data_path)
