import pandas as pd
import os

def load_data(file_path: str) -> pd.DataFrame:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"El archivo no existe: {file_path}")
    
    return pd.read_csv(file_path)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df_clean = df.drop_duplicates()
    
    if df_clean.isnull().values.any():
        df_clean = df_clean.dropna()

    return df_clean

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')
    df['Time'] = pd.to_datetime(df['Time'], format='%H:%M').dt.time

    return df


def save_data(df: pd.DataFrame, output_path: str) -> None:
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)


def process_data(input_file: str, output_file: str) -> None:
    df = load_data(input_file)
    df_clean = clean_data(df)
    df_transformed = transform_data(df_clean)
    save_data(df_transformed, output_file)


if __name__ == "__main__":
    input_file = 'data/raw/supermarket_sales - Sheet1.csv'
    output_file = 'data/processed/supermarket_sales_cleaned.csv'
    
    process_data(input_file, output_file)
