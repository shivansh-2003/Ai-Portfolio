import numpy as np
import pandas as pd


np.random.seed(42)

# Number of synthetic data points
n = 10000


income = np.random.normal(50000, 15000, n).astype(int) 
expenses = np.random.normal(30000, 10000, n).astype(int)
debts = np.random.normal(15000, 5000, n).astype(int)
savings = (income - expenses - debts / 10).astype(int)  


synthetic_data = pd.DataFrame({
    'income': income,
    'expenses': expenses,
    'debts': debts,
    'savings': savings
})


synthetic_data['savings'] = synthetic_data['savings'].apply(lambda x: max(x, 0))

# Save to CSV
synthetic_data.to_csv('synthetic_financial_data.csv', index=False)
print(synthetic_data.head())
