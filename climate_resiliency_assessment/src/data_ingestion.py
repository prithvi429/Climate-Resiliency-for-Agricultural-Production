import pandas as pd

def ingest_climate_data(file_path):
    """Ingest climate data from a CSV file."""
    return pd.read_csv(file_path)

def ingest_crop_data(file_path):
    """Ingest crop performance data from a CSV file."""
    return pd.read_csv(file_path)

def ingest_economic_data(file_path):
    """Ingest economic impact data from a CSV file."""
    return pd.read_csv(file_path)

if __name__ == "__main__":
    climate_data = ingest_climate_data('../data/raw/climate_data.csv')
    crop_data = ingest_crop_data('../data/raw/crop_data.csv')
    economic_data = ingest_economic_data('../data/raw/economic_data.csv')
