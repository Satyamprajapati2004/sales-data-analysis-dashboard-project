import pandas as pd

df = pd.read_csv("data/sales_data.csv")

print(df.head())
print(df.isnull().sum())

df.drop_duplicates(inplace=True)

# Correct revenue calculation
df['Revenue'] = df['Quantity_Sold'] * df['Unit_Price']

df.to_csv("output/cleaned_data.csv", index=False)

print("Cleaning Done Successfully!")