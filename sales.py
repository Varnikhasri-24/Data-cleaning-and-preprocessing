import pandas as pd

# 1. Load the dataset
df = pd.read_csv(r"C:\Users\UserK\Desktop\Walmart_Sales(1).csv")

# 2. Display initial information
print("Initial Data Info:\n", df.info())
print("\nMissing values:\n", df.isnull().sum())

# 3. Remove duplicate rows
df.drop_duplicates(inplace=True)

# 4. Handle missing values (example handling — adjust based on your needs)
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].fillna('Unknown')

for col in df.select_dtypes(include='number').columns:
    df[col] = df[col].fillna(0)

# 5. Standardize text columns
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].str.strip().str.title()

# 6. Convert 'Date' column to datetime (if present)
if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# 7. Rename columns to lowercase and replace spaces with underscores
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# 8. Final data check
print("\nCleaned Data Info:\n", df.info())
print("\nNull values after cleaning:\n", df.isnull().sum())

# 9. Save cleaned data
df.to_csv("walmart_sales_cleaned.csv", index=False)
print("\n✅ Cleaned Walmart dataset saved as 'walmart_sales_cleaned.csv'.")
