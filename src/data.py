# src/data.py

import pandas as pd
from sklearn.model_selection import train_test_split


def load_data(filepath):
    """
    Load cleaned triage dataset.
    """
    return pd.read_csv(filepath)


def split_data(df, target="esi", test_size=0.20, random_state=42):
    """
    Split dataset into training and testing sets.
    """

    X = df.drop(columns=[target])
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        stratify=y,
        random_state=random_state
    )

    return X_train, X_test, y_train, y_test
