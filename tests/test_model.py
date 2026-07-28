"""
Pytest smoke test for model training.
"""

from src.data import load_data, split_data
from src.model import train_logistic_regression


def test_training_pipeline():
    """
    Verify that the training pipeline runs successfully
    on a small sample of the dataset.
    """

    # Load only a small subset of the data
    df = load_data("data/triage_cleaned_v1.csv").head(50)

    # Split the data
    X_train, X_test, y_train, y_test = split_data(df)

    # Train the model
    model = train_logistic_regression(
        X_train,
        y_train,
        max_iter=1000,
        random_state=42,
    )

    # Confirm that a model object was created
    assert model is not None
