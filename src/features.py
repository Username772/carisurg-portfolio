"""
Feature engineering functions for the
AI-Assisted Emergency Department Triage project.
"""

import pandas as pd


def add_clinical_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create additional clinical features from the raw triage variables.

    Parameters
    ----------
    df : pandas.DataFrame
        Input triage dataset.

    Returns
    -------
    pandas.DataFrame
        Dataset with engineered features added.
    """

    data = df.copy()

    # Pulse Pressure
    if {"triage_vital_sbp", "triage_vital_dbp"}.issubset(data.columns):
        data["pulse_pressure"] = (
            data["triage_vital_sbp"] - data["triage_vital_dbp"]
        )

    # Shock Index
    if {"triage_vital_hr", "triage_vital_sbp"}.issubset(data.columns):
        data["shock_index"] = (
            data["triage_vital_hr"] /
            data["triage_vital_sbp"].replace(0, pd.NA)
        )

    # Estimated Mean Arterial Pressure (MAP)
    if {"triage_vital_sbp", "triage_vital_dbp"}.issubset(data.columns):
        data["map_estimate"] = (
            data["triage_vital_dbp"] +
            (data["pulse_pressure"] / 3)
        )

    # Oxygen Saturation / Respiratory Rate Ratio
    if {"triage_vital_o2", "triage_vital_rr"}.issubset(data.columns):
        data["o2_rr_ratio"] = (
            data["triage_vital_o2"] /
            data["triage_vital_rr"].replace(0, pd.NA)
        )

    # Tachypnoea Indicator
    if "triage_vital_rr" in data.columns:
        data["tachypnoea"] = (
            data["triage_vital_rr"] > 20
        ).astype(int)

    # Hypoxia Indicator
    if "triage_vital_o2" in data.columns:
        data["hypoxia"] = (
            data["triage_vital_o2"] < 94
        ).astype(int)

    # Fever Indicator
    if "triage_vital_temp" in data.columns:
        data["fever"] = (
            data["triage_vital_temp"] >= 38.0
        ).astype(int)

    return data
