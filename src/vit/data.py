import requests
from pathlib import Path


def download_lenna(ouput_dir: str = "./data"):
    """Download lenna image from http://www.lenna.org/lena_std.tif

    Args:
        ouput_dir (str, optional): Output directory.
            Defaults to "./data".
    """
    url = "http://www.lenna.org/lena_std.tif"
    responce = requests.get(url)
    output_filepath = Path(ouput_dir).joinpath("lena_std.tif")
    output_filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(output_filepath, "wb") as f:
        f.write(responce.content)
