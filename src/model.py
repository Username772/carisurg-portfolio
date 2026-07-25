# src/model.py

"""
Model training module.

Contains functions that create and train
machine learning models used for ESI prediction.
"""


from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import (
    RandomForestClassifier,
    GradientBoostingClassifier
)


def get_models():

    """
    Create the candidate classification models.

    Returns:
        Dictionary containing model objects.
    """


    models = {

        # Baseline linear model
        "logistic_regression":
            LogisticRegression(
                max_iter=1000,
                random_state=42
            ),


        # Ensemble model that combines many decision trees
        "random_forest":
            RandomForestClassifier(
                random_state=42
            ),


        # Sequential boosting model
        "gradient_boosting":
            GradientBoostingClassifier(
                random_state=42
            )
    }


    return models



def train_models(models, X_train, y_train):

    """
    Train all supplied models.

    Parameters:
        models:
            Dictionary of model objects

        X_train:
            Training features

        y_train:
            Training labels

    Returns:
        Dictionary of trained models
    """


    trained_models = {}


    for name, model in models.items():

        print(f"Training {name}...")


        model.fit(
            X_train,
            y_train
        )


        trained_models[name] = model


    return trained_models

    """
    Create the candidate classification models.

    Returns:
        Dictionary containing model objects.
    """


    models = {

        # Baseline linear model
        "logistic_regression":
            LogisticRegression(
                max_iter=1000,
                random_state=42
            ),


        # Ensemble model that combines many decision trees
        "random_forest":
            RandomForestClassifier(
                random_state=42
            ),


        # Sequential boosting model
        "gradient_boosting":
            GradientBoostingClassifier(
                random_state=42
            )
    }


    return models



def train_models(models, X_train, y_train):

    """
    Train all supplied models.

    Parameters:
        models:
            Dictionary of model objects

        X_train:
            Training features

        y_train:
            Training labels

    Returns:
        Dictionary of trained models
    """


    trained_models = {}


    for name, model in models.items():

        print(f"Training {name}...")


        model.fit(
            X_train,
            y_train
        )


        trained_models[name] = model


    return trained_models
