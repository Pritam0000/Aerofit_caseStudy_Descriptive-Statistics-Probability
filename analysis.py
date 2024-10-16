import pandas as pd

def get_summary_statistics(df):
    return df.describe()

def calculate_product_probabilities(df):
    return df['Product'].value_counts(normalize=True)

def calculate_gender_product_probabilities(df):
    return pd.crosstab(df['Gender'], df['Product'], normalize='index')
