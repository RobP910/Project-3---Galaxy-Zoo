"""Module for managing datasets used for model training/testing.

Resources must be downloaded before this module can be used to get data.
Running this as a script will handle all required downloads.
"""

# requires galaxy-datasets package
# https://pypi.org/project/galaxy-datasets/

import os
import pandas as pd
from galaxy_datasets import gz2


RESOURCES_DIR = "Resources"
"""The directory to hold all downloaded resources."""


def download_resources():
    """Download required resources so galaxy datasets can be used."""
    # the whole dataset downloads regardless of train flag
    gz2(os.path.join(RESOURCES_DIR, "gz2"), False, True)


def get_gz2(train: bool = False):
    """Get the Galaxy Zoo 2 training or testing dataset.

    Args:
        train: A flag to control if the training or testing catalog should be
            returned. Defaults to False for testing data.

    Returns:
        A tuple of a catalog DataFrame holding the dataset (with "file_loc"
        column of image paths) and a list of column names to use as labels.
    """
    return gz2(os.path.join(RESOURCES_DIR, "gz2"), train, False)


def get_full_gz2():
    """Get the full Galaxy Zoo 2 dataset.

    Returns:
        A tuple of a catalog DataFrame holding the dataset (with "file_loc"
        column of image paths) and a list of column names to use as labels.
    """
    test_catalog, label_cols = get_gz2(False)
    train_catalog, _ = get_gz2(True)
    catalog = pd.concat([test_catalog, train_catalog], ignore_index=True)
    return catalog, label_cols


if __name__ == "__main__":
    download_resources()
