"""
Training script for the
AI-Assisted Emergency Department Triage project.

Usage:
    python scripts/train.py --config config.yaml
"""

import argparse
import yaml

from src.data import load_data, split_data
from src.features import add_clinical_features
from src.model import (
    train_logistic_regression,
    evaluate_model,
)
from src.utils import save_model


def main(config_path):

    # Read configuration
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)

    # Load dataset
    df = load_data(config["paths"]["data"])

    # Feature engineering
    df = add_clinical_features(df)

    # Split data
    X_train, X_test, y_train, y_test = split_data(
        df,
        target=config["training"]["target"],
    )

    # Train model
    model = train_logistic_regression(
        X_train,
        y_train,
        max_iter=config["hyperparameters"]["max_iter"],
        random_state=config["hyperparameters"]["random_state"],
    )

    # Evaluate model
    evaluate_model(model, X_test, y_test)

    # Save trained model
    save_model(model, config["paths"]["model_output"])


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--config",
        default="config.yaml",
        help="Configuration file",
    )

    args = parser.parse_args()

    main(args.config)
