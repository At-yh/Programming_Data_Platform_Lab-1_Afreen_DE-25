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
df.to_csv("Reports(output)/cleaned_products.csv", index=False)