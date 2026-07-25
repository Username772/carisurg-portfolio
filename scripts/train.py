# scripts/train.py

from src.data import load_data, split_data
from src.model import train_logistic_regression


df = load_data("data/triage_cleaned_v1.csv")

X_train, X_test, y_train, y_test = split_data(df)

model = train_logistic_regression(
    X_train,
    y_train
)
