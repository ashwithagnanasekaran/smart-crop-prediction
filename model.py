import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib  # Using joblib instead of pickle (better for large numpy arrays)
import warnings
warnings.filterwarnings('ignore')

# DATA PREPARATION
print("\n PREPARING DATA FOR MODELING...")

# Separate features and target
feature = df.drop(columns=['Crop'])
target = df['Crop']

print(f"   • Features shape: {feature.shape}")
print(f"   • Target shape: {target.shape}")
print(f"   • Features: {list(feature.columns)}")

# Train model
def train_model():
    data = load_data()
    data, le = preprocess(data)

    X = data.drop("crop", axis=1)
    y = data["crop"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluation
    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))

    # Save model
    joblib.dump(model, "model.pkl")

    return model, le

# Prediction
def predict(temp, humidity, rainfall, soil):
    model, le = train_model()

    soil_map = {
        "loamy": 0,
        "sandy": 1,
        "clay": 2
    }

    soil_value = soil_map[soil]

    input_data = [[temp, humidity, rainfall, soil_value]]
    prediction = model.predict(input_data)

    # Convert back to label
    return prediction[0]

import os

def train_model():
    data = load_data()
    data, le = preprocess(data)

    X = data.drop("crop", axis=1)
    y = data["crop"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Save model
    import joblib
    joblib.dump(model, "model.pkl")

    return model, le
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def train_model():
    data = pd.read_csv("data.csv")

    X = data.drop("label", axis=1)
    y = data["label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)

    return model
from sklearn.metrics import accuracy_score

def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)
    acc = accuracy_score(y_test, predictions)
    print("Accuracy:", acc)
    return acc
import joblib

def save_model(model):
    joblib.dump(model, "crop_model.pkl")
    print("Model saved successfully")
    
    def predict(model, input_data):
    prediction = model.predict([input_data])
    return prediction[0]
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

def build_pipeline():
    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("model", RandomForestClassifier(n_estimators=100))
    ])
    return pipeline
def train_model():
    data = pd.read_csv("data.csv")

    X = data.drop("Label", axis=1)
    y = data["Label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    pipeline = build_pipeline()
    pipeline.fit(X_train, y_train)

    return pipeline, X_test, y_test
def load_model():
    model = joblib.load("crop_model.pkl")
    print("Model loaded successfully")
    return model
def predict_crop(model, input_data):
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)
    return prediction[0]
from sklearn.model_selection import GridSearchCV

def tune_model(X_train, y_train):
    param_grid = {
        "model__n_estimators": [50, 100],
        "model__max_depth": [None, 10, 20],
    }

    pipeline = build_pipeline()

    grid = GridSearchCV(pipeline, param_grid, cv=3, n_jobs=-1)
    grid.fit(X_train, y_train)

    print("Best Parameters:", grid.best_params_)
    return grid.best_estimator_
from sklearn.model_selection import GridSearchCV

from sklearn.model_selection import cross_val_score

def cross_validate_model(model, X, y):
    scores = cross_val_score(model, X, y, cv=5)
    print("Cross-validation scores:", scores)
    print("Average score:", scores.mean())
    return scores.mean()
from sklearn.metrics import confusion_matrix

def show_confusion_matrix(model, X_test, y_test):
    preds = model.predict(X_test)
    cm = confusion_matrix(y_test, preds)
    print("Confusion Matrix:\n", cm)