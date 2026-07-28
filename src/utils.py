"""
Utility functions for the
AI-Assisted Emergency Department Triage project.
"""

import joblib
import pandas as pd


def save_model(model, filepath):
    """
    Save a trained machine learning model.

    Parameters
    ----------
    model : object
        Trained scikit-learn model.
    filepath : str
        Output file path.
    """
    joblib.dump(model, filepath)
    print(f"Model saved to: {filepath}")


def load_model(filepath):
    """
    Load a previously trained machine learning model.

    Parameters
    ----------
    filepath : str
        Model file path.

    Returns
    -------
    object
        Loaded model.
    """
    return joblib.load(filepath)


def print_dataset_summary(df: pd.DataFrame):
    """
    Print a brief summary of the dataset.

    Parameters
    ----------
    df : pandas.DataFrame
        Dataset to summarise.
    """
    print("\nDataset Summary")
    print("----------------")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")
    print("\nMissing values:")
    print(df.isnull().sum())
