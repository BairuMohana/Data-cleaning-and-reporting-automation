import pandas as pd
import os

def load_data(file_path):
    df = pd.read_csv(file_path)

    print("\n" + "=" * 60)
    print("DATA CLEANING & REPORTING AUTOMATION")
    print("=" * 60)

    print(f"\nRaw data loaded successfully!")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    return df


def clean_data(df):
    print("\n--- DATA CLEANING STARTED ---")

    print("\nMissing values before cleaning:")
    print(df.isnull().sum())

    duplicate_count = df.duplicated().sum()
    print(f"\nDuplicate rows found: {duplicate_count}")

    df = df.drop_duplicates()

    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    numerical_columns = ["Quantity", "Unit_Price", "Total_Sales"]

    for column in numerical_columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")
        df[column] = df[column].fillna(df[column].median())

    categorical_columns = [
        "Customer_Name",
        "Product",
        "Category",
        "City",
        "Payment_Method"
    ]

    for column in categorical_columns:
        df[column] = df[column].fillna("Unknown")

    df = df[df["Total_Sales"] >= 0]

    print("\nMissing values after cleaning:")
    print(df.isnull().sum())

    print(f"\nRows after cleaning: {df.shape[0]}")
    print(f"Columns after cleaning: {df.shape[1]}")

    print("\n--- DATA CLEANING COMPLETED ---")

    return df


def save_cleaned_data(df, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)

    print(f"\nCleaned data saved to: {output_path}")