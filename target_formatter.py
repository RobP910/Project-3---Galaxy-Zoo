"""Module to format target features that can be provided/evaluated for a model."""

import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder


def _reshape_series(s: pd.Series):
    return np.array(s).reshape(-1, 1)


def get_summary_encoder(train_catalog: pd.DataFrame):
    """Get a fitted encoder of the summary as a feature for training/testing.

    Args:
        train_catalog: The catalog holding the summary column for training, to
            have the encoder fit to its data.

    Returns:
        A OneHotEncoder for summary data.
    """
    summary = train_catalog["summary"]
    return OneHotEncoder(sparse_output=False, handle_unknown="ignore").fit(
        _reshape_series(summary)
    )


def get_train_test_summary_enc(
    encoder: OneHotEncoder, train_catalog: pd.DataFrame, test_catalog: pd.DataFrame
):
    """Get encodings of summary columns from training & testing catalogs.

    Args:
        encoder: A OneHotEncoder for summary data.
        train_catalog: The catalog holding the summary column for training.
        test_catalog: The catalog holding the summary column for testing.

    Returns:
        A tuple of the encoded summary data for training and testing.
    """
    return encoder.transform(
        _reshape_series(train_catalog["summary"])
    ), encoder.transform(_reshape_series(test_catalog["summary"]))
