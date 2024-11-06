import shutil
import argparse

import kagglehub

class KaggleClient:
    """Class for downloading data from Kaggle API"""

    def __init__(self):
        pass

    def download_data(self, dataset_handle, dest_dir=None):
        src_dir = kagglehub.dataset_download(handle=dataset_handle)
        print(f"Download location:", src_dir)

        if dest_dir:
            shutil.move(src_dir, dest_dir)
            print(f"Moving data: {src_dir} -> {dest_dir}")



if __name__ == "__main__":
        # Set up argument parsing for the save path
    parser = argparse.ArgumentParser(description="Download Arxiv metadata from Kaggle and save to specified path.")

    parser.add_argument(
        "-d",
        "--dataset",
        required=True,
        type=str,
        help="Kaggle dataset handle to download data from."
    )
    parser.add_argument(
        "-o",
        "--dest_dir",
        type=str,
        help="Path to move downloaded files to."
    )

    args = parser.parse_args()

    kaggle_client = KaggleClient()
    kaggle_client.download_data(dataset_handle=args.dataset, dest_dir=args.dest_dir)
