import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def clean_data(df):
    df = df.copy()

    # Convert date column
    df['Transaction_Date'] = pd.to_datetime(df['Transaction_Date'])

    # Create Price column
    df['Price'] = df['Revenue'] / df['Units_Sold']

    return df

def save_data(df, path):
    df.to_csv(path, index=False)

if __name__ == "__main__":
    raw_path = "data/raw/csv_file/synthetic_ecommerce_data.csv"
    processed_path = "data/processed/cleaned_ecommerce_data.csv"

    df = load_data(raw_path)
    df = clean_data(df)
    save_data(df, processed_path)
