import pandas as pd

def analyze_climate_data(df):
    """Analyze climate data for trends and anomalies."""
    trends = df.describe()  # Basic statistical analysis
    return trends

def analyze_crop_performance(df):
    """Analyze crop performance data."""
    yield_summary = df.groupby('crop').agg({'yield': ['mean', 'std']})
    return yield_summary

if __name__ == "__main__":
    climate_data = pd.read_csv('../data/processed/cleaned_climate_data.csv')
    crop_data = pd.read_csv('../data/processed/cleaned_crop_data.csv')

    climate_trends = analyze_climate_data(climate_data)
    crop_performance = analyze_crop_performance(crop_data)

    print(climate_trends)
    print(crop_performance)
