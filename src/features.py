# src/features.py

"""
Feature engineering module.

This file contains reusable functions that create
additional clinical features before model training.
"""


def add_clinical_features(df):

    """
    Add derived clinical features.

    Parameters:
        df (DataFrame):
            Input triage dataset.

    Returns:
        DataFrame:
            Dataset with additional engineered features.
    """

    # Make a copy so the original dataset is not modified
    df = df.copy()


    # Calculate pulse pressure:
    # Pulse Pressure = Systolic BP - Diastolic BP
    # This represents the difference between the two blood pressure values.
    if (
        "triage_vital_sbp" in df.columns and
        "triage_vital_dbp" in df.columns
    ):

        df["pulse_pressure"] = (
            df["triage_vital_sbp"] -
            df["triage_vital_dbp"]
        )


    # Estimate Mean Arterial Pressure (MAP)
    # Approximation:
    # MAP = DBP + (Pulse Pressure / 3)

    if "pulse_pressure" in df.columns:

        df["map_estimate"] = (
            df["triage_vital_dbp"] +
            (df["pulse_pressure"] / 3)
        )


    return df
