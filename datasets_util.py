"""Module for managing datasets used for model training/testing.

Resources must be downloaded before this module can be used to get data.
Running this as a script will handle all required downloads.
"""

# requires galaxy-datasets package
# https://pypi.org/project/galaxy-datasets/

import os
import numpy as np
import pandas as pd
import tensorflow as tf
from galaxy_datasets import gz2
from galaxy_datasets.tensorflow.datasets import get_image_dataset


RESOURCES_DIR = "Resources"
"""The directory to hold all downloaded resources."""


def download_resources():
    """Download required resources so galaxy datasets can be used."""
    # the whole dataset downloads regardless of train flag
    gz2(os.path.join(RESOURCES_DIR, "gz2"), False, True)


def get_gz2(train: bool = False):
    """Get the Galaxy Zoo 2 training or testing data.

    Args:
        train: A flag to control if the training or testing catalog should be
            returned. Defaults to False for testing data.

    Returns:
        A tuple of a catalog DataFrame holding the data (with "file_loc"
        column of image paths) and a list of column names available for labels.
    """
    return gz2(os.path.join(RESOURCES_DIR, "gz2"), train, False)


def get_full_gz2():
    """Get the full Galaxy Zoo 2 data.

    Returns:
        A tuple of a catalog DataFrame holding the data (with "file_loc"
        column of image paths) and a list of column names available for labels.
    """
    test_catalog, label_cols = get_gz2(False)
    train_catalog, _ = get_gz2(True)
    catalog = pd.concat([test_catalog, train_catalog], ignore_index=True)
    return catalog, label_cols


def get_dataset(
    file_locs: list[str], labels: np.ndarray, requested_img_size: int | None = None
):
    """Get a tensorflow dataset made from given image file paths & labels.

    Args:
        file_locs: The file paths for images to format into the dataset.
        labels: The label data for each image to format into the dataset.
            Values are expected to be numeric.
        requested_img_size: The image square dimension to resize to if the
            original images don't match. ex: 256 for a 256px by 256px image.
            Defaults to None to not resize.
    """
    # result should automatically have normalized to 0-1 range
    dataset = get_image_dataset(
        file_locs, labels, requested_img_size=requested_img_size
    )

    # for performance:
    # - cache elements of dataset
    # - batch elements for use per epoch
    # - allow prefetching elements later than what's currently being processed
    return dataset.cache().batch(128).prefetch(tf.data.AUTOTUNE)


if __name__ == "__main__":
    download_resources()
