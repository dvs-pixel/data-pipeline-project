# scripts/etl_pipeline.py
import os
print("Current Working Directory:", os.getcwd())
print("File Exists?", os.path.exists("data/projectdata.csv"))

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import os

# Step 1: Load data
def load_data(filepath):
    print("[INFO] Loading dataset...")
    return pd.read_csv(filepath)

# Step 2: Preprocessing
def clean_data(df):
    print("[INFO] Dropping duplicates...")
    return df.drop_duplicates()

def split_features_target(df, target_column):
    X = df.drop(columns=[target_column])
    y = df[target_column]
    return X, y

def build_preprocessor(X):
    numeric_features = X.select_dtypes(include=['int64', 'float64']).columns.tolist()
    categorical_features = X.select_dtypes(include=['object']).columns.tolist()

    numeric_transformer = Pipeline([
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler())
    ])

    categorical_transformer = Pipeline([
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('encoder', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
    ])

    return ColumnTransformer([
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

def transform_and_split(X, y, preprocessor):
    X_transformed = preprocessor.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X_transformed, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

def save_data(X_train, X_test, y_train, y_test, output_folder="processed_data"):
    os.makedirs(output_folder, exist_ok=True)  # this auto-creates the folder
    pd.DataFrame(X_train).to_csv(f"{output_folder}/X_train.csv", index=False)
    pd.DataFrame(X_test).to_csv(f"{output_folder}/X_test.csv", index=False)
    y_train.to_csv(f"{output_folder}/y_train.csv", index=False)
    y_test.to_csv(f"{output_folder}/y_test.csv", index=False)
    print(f"[INFO] Data saved to '{output_folder}' folder.")


# Main function
def run_pipeline():
    filepath = "data/projectdata.csv"  # Replace if using a different file
    target_column = "Churn"  # Replace with the actual target column name

    df = load_data(filepath)
    df = clean_data(df)
    X, y = split_features_target(df, target_column)
    preprocessor = build_preprocessor(X)
    X_train, X_test, y_train, y_test = transform_and_split(X, y, preprocessor)
    save_data(X_train, X_test, y_train, y_test)

if __name__ == "__main__":
    run_pipeline()
