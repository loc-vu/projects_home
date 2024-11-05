import kagglehub


def download_papers():
    # Download latest version
    src_dir = kagglehub.dataset_download("Cornell-University/arxiv")

    print(f"Download location:", src_dir)

if __name__ == "__main__":
    download_papers()