import pytest
import pandas as pd
import numpy as np
from src.data_transformation import clean_climate_data, clean_crop_data, clean_economic_data

@pytest.fixture
def sample_climate_data():
    """Fixture for sample climate data with missing values"""
    return pd.DataFrame({
        'year': [2010, 2011, 2012, 2013],
        'temperature': [25.6, 26.1, np.nan, 27.3],
        'precipitation': [1200, np.nan, 1100, 1150],
        'extreme_events': [2, 3, 1, np.nan]
    })

@pytest.fixture
def sample_crop_data():
    """Fixture for sample crop data with missing values"""
    return pd.DataFrame({
        'year': [2010, 2011, 2012, 2013],
        'crop': ['wheat', 'soybean', 'cotton', np.nan],
        'yield': [3.5, np.nan, 2.8, 3.2],
        'season': ['rabi', 'kharif', 'kharif', 'rabi']
    })

@pytest.fixture
def sample_economic_data():
    """Fixture for sample economic data with missing values"""
    return pd.DataFrame({
        'year': [2010, 2011, 2012, 2013],
        'loss': [50000, 75000, np.nan, 60000],
        'region': ['MH', 'MP', 'MH', np.nan],
        'compensation': [20000, np.nan, 25000, 30000]
    })

def test_clean_climate_data_handles_missing_values(sample_climate_data):
    """Test that climate data cleaning handles missing values"""
    cleaned = clean_climate_data(sample_climate_data)
    assert not cleaned.isnull().values.any(), "Data should have no missing values after cleaning"

def test_clean_crop_data_removes_missing_rows(sample_crop_data):
    """Test that crop data cleaning removes rows with missing values"""
    cleaned = clean_crop_data(sample_crop_data)
    assert not cleaned.isnull().values.any(), "Data should have no missing values after cleaning"
    assert len(cleaned) == 2, "Should remove rows with missing values"

def test_clean_economic_data_removes_missing_rows(sample_economic_data):
    """Test that economic data cleaning removes rows with missing values"""
    cleaned = clean_economic_data(sample_economic_data)
    assert not cleaned.isnull().values.any(), "Data should have no missing values after cleaning"
    assert len(cleaned) == 1, "Should remove rows with missing values"

def test_clean_climate_data_preserves_dtypes(sample_climate_data):
    """Test that climate data cleaning preserves data types"""
    cleaned = clean_climate_data(sample_climate_data)
    assert pd.api.types.is_numeric_dtype(cleaned['temperature'])
    assert pd.api.types.is_numeric_dtype(cleaned['precipitation'])
    assert pd.api.types.is_numeric_dtype(cleaned['extreme_events'])
