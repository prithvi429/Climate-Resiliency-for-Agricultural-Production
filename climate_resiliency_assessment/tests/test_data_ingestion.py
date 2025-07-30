import pytest
import pandas as pd
import os
from src.data_ingestion import ingest_climate_data, ingest_crop_data, ingest_economic_data

# Test data paths
CLIMATE_DATA_PATH = '../data/raw/climate_data.csv'
CROP_DATA_PATH = '../data/raw/crop_data.csv'
ECONOMIC_DATA_PATH = '../data/raw/economic_data.csv'

def test_ingest_climate_data_file_exists():
    """Test that climate data file exists"""
    assert os.path.exists(CLIMATE_DATA_PATH), f"File not found: {CLIMATE_DATA_PATH}"

def test_ingest_crop_data_file_exists():
    """Test that crop data file exists"""
    assert os.path.exists(CROP_DATA_PATH), f"File not found: {CROP_DATA_PATH}"

def test_ingest_economic_data_file_exists():
    """Test that economic data file exists"""
    assert os.path.exists(ECONOMIC_DATA_PATH), f"File not found: {ECONOMIC_DATA_PATH}"

def test_ingest_climate_data_returns_dataframe():
    """Test that climate data ingestion returns a DataFrame"""
    df = ingest_climate_data(CLIMATE_DATA_PATH)
    assert isinstance(df, pd.DataFrame), "Should return a pandas DataFrame"
    assert not df.empty, "DataFrame should not be empty"

def test_ingest_crop_data_returns_dataframe():
    """Test that crop data ingestion returns a DataFrame"""
    df = ingest_crop_data(CROP_DATA_PATH)
    assert isinstance(df, pd.DataFrame), "Should return a pandas DataFrame"
    assert not df.empty, "DataFrame should not be empty"

def test_ingest_economic_data_returns_dataframe():
    """Test that economic data ingestion returns a DataFrame"""
    df = ingest_economic_data(ECONOMIC_DATA_PATH)
    assert isinstance(df, pd.DataFrame), "Should return a pandas DataFrame"
    assert not df.empty, "DataFrame should not be empty"

def test_ingest_climate_data_columns():
    """Test that climate data has expected columns"""
    df = ingest_climate_data(CLIMATE_DATA_PATH)
    expected_columns = ['year', 'temperature', 'precipitation', 'extreme_events']
    assert all(col in df.columns for col in expected_columns), "Missing expected columns"

def test_ingest_crop_data_columns():
    """Test that crop data has expected columns"""
    df = ingest_crop_data(CROP_DATA_PATH)
    expected_columns = ['year', 'crop', 'yield', 'season']
    assert all(col in df.columns for col in expected_columns), "Missing expected columns"

def test_ingest_economic_data_columns():
    """Test that economic data has expected columns"""
    df = ingest_economic_data(ECONOMIC_DATA_PATH)
    expected_columns = ['year', 'loss', 'region', 'compensation']
    assert all(col in df.columns for col in expected_columns), "Missing expected columns"
