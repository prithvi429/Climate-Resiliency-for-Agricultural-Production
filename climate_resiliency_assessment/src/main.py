from data_ingestion import ingest_climate_data, ingest_crop_data, ingest_economic_data
from data_transformation import clean_climate_data, clean_crop_data, clean_economic_data
from data_validation import validate_data
from data_analysis import analyze_climate_data, analyze_crop_performance
from economic_impact_analysis import evaluate_economic_impact
from technology_assessment import assess_technology_in_agriculture
from policy_analysis import analyze_government_policies

def main():
    # Ingest data
    climate_data = ingest_climate_data('climate_resiliency_assessment/data/raw/climate_data.csv')
    crop_data = ingest_crop_data('climate_resiliency_assessment/data/raw/crop_data.csv')
    economic_data = ingest_economic_data('climate_resiliency_assessment/data/raw/economic_data.csv')

    # Clean data
    cleaned_climate_data = clean_climate_data(climate_data)
    cleaned_crop_data = clean_crop_data(crop_data)
    cleaned_economic_data = clean_economic_data(economic_data)

    # Validate data
    validate_data(cleaned_climate_data)
    validate_data(cleaned_crop_data)
    validate_data(cleaned_economic_data)

    # Analyze data
    climate_trends = analyze_climate_data(cleaned_climate_data)
    crop_performance = analyze_crop_performance(cleaned_crop_data)
    total_loss = evaluate_economic_impact(cleaned_economic_data)

    # Assess technology and policies
    technology_result = assess_technology_in_agriculture()
    policy_result = analyze_government_policies()

    # Print results
    print(climate_trends)
    print(crop_performance)
    print(f"Total Economic Loss: {total_loss}")
    print(technology_result)
    print(policy_result)

if __name__ == "__main__":
    main()
