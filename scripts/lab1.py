import pandas as pd

# STEP 1: INGEST
df = pd.read_csv("data/lab1_products.csv", sep=";")

print("Before Cleaning:")
print(df.head())
print(df.info())

# STEP 2: Remove extra spaces
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip()

# STEP 3: Fix price column
df["price"] = pd.to_numeric(df["price"], errors="coerce")

# STEP 4: Fix date column
df["created_at"] = pd.to_datetime(df["created_at"], errors="coerce")

# STEP 5: Remove rows with missing id
df = df.dropna(subset=["id"])

# STEP 6: Remove negative prices
df = df[df["price"] >= 0]

# STEP 7: Remove rows where price is missing
df = df.dropna(subset=["price"])

print("\nAfter Cleaning:")
print(df.head())
print(df.info())

# STEP 8: Save cleaned data
df.to_csv("results/cleaned_products.csv", index=False)


# Analytics Summary (Calculate Summary Values)

average_price = df["price"].mean()    # calculates average 
median_price = df["price"].median()   # middle value
total_products = len(df)              # number of rows
missing_price = df["price"].isna().sum()   # counts missing values

summary_data = {
    "average_price": [average_price],
    "median_price": [median_price],
    "total_products": [total_products],
    "missing_price_count": [missing_price]
}

summary_df = pd.DataFrame(summary_data)

# Export Summary file
summary_df.to_csv("results/analytics_summary.csv", index=False)