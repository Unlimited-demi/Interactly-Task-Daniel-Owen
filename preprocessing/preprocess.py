import pandas as pd

df = pd.read_csv('../data/candidate_data.csv')
df.fillna('', inplace=True)
df.to_csv('../data/cleaned_candidate_data.csv', index=False)

print("Preprocessing complete.")
