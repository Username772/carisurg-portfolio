"""
Pytest sanity checks for data loading.
"""

from src.data import load_data


def test_load_data():
    """
    Verify that the dataset loads correctly and
    contains the expected target column.
    """

    df = load_data("data/triage_cleaned_v1.csv")

    # Dataset should not be empty
    assert not df.empty

    # Expected target column
    assert "esi" in df.columns

    # Dataset should contain rows and columns
    assert df.shape[0] > 0
    assert df.shape[1] > 0
