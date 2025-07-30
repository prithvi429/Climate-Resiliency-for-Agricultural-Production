import pandas as pd

def evaluate_economic_impact(df):
    """Evaluate the economic impact of climate disruptions."""
    total_loss = df['loss'].sum()
    return total_loss

if __name__ == "__main__":
    economic_data = pd.read_csv('../data/processed/cleaned_economic_data.csv')
    total_loss = evaluate_economic_impact(economic_data)
    print(f"Total Economic Loss: {total_loss}")
