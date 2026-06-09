import os


OUTPUT_DIR = "outputs"


def ensure_output_dir():

    os.makedirs(
        OUTPUT_DIR,
        exist_ok=True
    )


def get_output_path(
    filename
):

    ensure_output_dir()

    return os.path.join(
        OUTPUT_DIR,
        filename
    )