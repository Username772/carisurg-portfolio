import pandas as pd
from sklearn.model_selection import train_test_split


def load_data(filepath):
    """
    Load the cleaned ED triage dataset.
    """
    return pd.read_csv(filepath)


def split_data(df, target="esi", test_size=0.20, random_state=42):
    """
    Split the dataset into training and testing sets.
    """

    if target not in df.columns:
        raise ValueError(f"Target column '{target}' not found in dataset.")

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
        random_state=random_state
    )

    return X_train, X_test, y_train, y_test
