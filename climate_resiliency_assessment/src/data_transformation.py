import pandas as pd

def clean_climate_data(df):
    """Clean climate data by handling missing values and anomalies."""
    df.fillna(method='ffill', inplace=True)  # Forward fill for missing values
    return df

def clean_crop_data(df):
    """Clean crop data."""
    df.dropna(inplace=True)  # Drop rows with missing values
    return df

def clean_economic_data(df):
    """Clean economic data."""
    df.dropna(inplace=True)  # Drop rows with missing values
    return df

if __name__ == "__main__":
    climate_data = pd.read_csv('../data/raw/climate_data.csv')
    crop_data = pd.read_csv('../data/raw/crop_data.csv')
    economic_data = pd.read_csv('../data/raw/economic_data.csv')

    cleaned_climate_data = clean_climate_data(climate_data)
    cleaned_crop_data = clean_crop_data(crop_data)
    cleaned_economic_data = clean_economic_data(economic_data)

    cleaned_climate_data.to_csv('../data/processed/cleaned_climate_data.csv', index=False)
    cleaned_crop_data.to_csv('../data/processed/cleaned_crop_data.csv', index=False)
    cleaned_economic_data.to_csv('../data/processed/cleaned_economic_data.csv', index=False)
