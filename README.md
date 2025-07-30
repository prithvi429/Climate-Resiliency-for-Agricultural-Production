# Climate Resiliency for Agricultural Production

This project provides a modular pipeline for assessing climate resiliency in agricultural production. It includes data ingestion, transformation, validation, analysis, economic impact evaluation, technology assessment, and policy analysis.

## Project Structure

```
climate_resiliency_assessment/
├── src/
│   ├── data_ingestion.py
│   ├── data_transformation.py
│   ├── data_validation.py
│   ├── data_analysis.py
│   ├── economic_impact_analysis.py
│   ├── technology_assessment.py
│   ├── policy_analysis.py
│   └── main.py
├── tests/
│   └── test_folder_structure.py
├── data/
│   ├── raw/
│   └── processed/
```

## How to Run

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Run the main pipeline:
   ```
   python climate_resiliency_assessment/src/main.py
   ```

## Features
- Ingest and clean climate, crop, and economic data
- Validate and analyze data for trends and performance
- Evaluate economic impacts
- Assess technology and policy for climate resiliency

## Testing
Run the folder structure test:
```
python -m unittest climate_resiliency_assessment/tests/test_folder_structure.py
```

## License
See LICENSE file for details
