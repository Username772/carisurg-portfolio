# scripts/train.py

"""
Main training pipeline.

Runs:
1. Load data
2. Add clinical features
3. Split data
4. Train models
5. Evaluate models
"""


from src.data import load_data, split_data
from src.features import add_clinical_features
from src.model import get_models, train_models
from src.evaluation import evaluate_model



# Location of cleaned dataset

DATA_PATH = (
    "data/triage_cleaned_v1.csv"
)



# Load dataset

df = load_data(DATA_PATH)

print(
    "Dataset loaded:",
    df.shape
)



# Add Week 7 engineered features

df = add_clinical_features(df)

print(
    "Feature engineering completed"
)



# Split data

X_train, X_test, y_train, y_test = split_data(df)

print(
    "Train size:",
    X_train.shape
)

print(
    "Test size:",
    X_test.shape
)



# Create models

models = get_models()



# Train models

trained_models = train_models(
    models,
    X_train,
    y_train
)



# Evaluate each model

for name, model in trained_models.items():

    print("\n")
    print("="*40)
    print(name)
    print("="*40)


    results = evaluate_model(
        model,
        X_test,
        y_test
    )


    print(results)
