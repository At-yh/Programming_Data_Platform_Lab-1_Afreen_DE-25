# LAB 1 - Data Pipeline

import pandas as pd

#  1: Ingest Data
df = pd.read_csv("data/lab1_products.csv", sep=";")

print("Before Cleaning:")
print(df.head())
print(df.info())

# 2: Remove extra spaces
for col in df.select_dtypes(include=["object", "string"]).columns:
    df[col] = df[col].str.strip()

# 3: Fix price column
df["price"] = pd.to_numeric(df["price"], errors="coerce")

# 4: Fix date column
df["created_at"] = pd.to_datetime(df["created_at"], errors="coerce")

# 5: Remove rows with missing id
df = df.dropna(subset=["id"])

# 6: Remove negative prices
df = df[df["price"] >= 0]

# 7: Remove rows where price is missing
df = df.dropna(subset=["price"])

print("\nAfter Cleaning:")
print(df.head())
print(df.info())

# 8: Save cleaned data
df.to_csv("results/cleaned_products.csv", index=False)


# # Analytics Summary (Calculate Summary Values)

# average_price = df["price"].mean()    # calculates average 
# median_price = df["price"].median()   # middle value
# total_products = len(df)              # number of rows
# missing_price = df["price"].isna().sum()   # counts missing values

# summary_data = {
#     "average_price": [average_price],
#     "median_price": [median_price],
#     "total_products": [total_products],
#     "missing_price_count": [missing_price]
# }

# summary_df = pd.DataFrame(summary_data)

# # Export Summary file
# summary_df.to_csv("results/analytics_summary.csv", index=False)


# Create Analytics Summary 
average_price = df["price"].mean()
median_price = df["price"].median()
total_products = len(df)
missing_price_count = df["price"].isna().sum()

summary_df = pd.DataFrame({
    "average_price": [average_price],
    "median_price": [median_price],
    "total_products": [total_products],
    "missing_price_count": [missing_price_count]
})

summary_df.to_csv("results/analytics_summary.csv", index=False)


#  Top 10 most expensive products
top_10_expensive = df.sort_values(by="price", ascending=False).head(10)  # this line sort by highest price first & Take first 10 rows


# Top 10 most deviating prices
average_price = df["price"].mean()
df["price_deviation"] = abs(df["price"] - average_price)
top_10_deviation = df.sort_values(by="price_deviation", ascending=False).head(10)

# Save price analysis
price_analysis_df = pd.concat(
    [
        top_10_expensive.assign(category="Top 10 Expensive"),
        top_10_deviation.assign(category="Top 10 Deviation")
    ]
)

price_analysis_df.to_csv("results/price_analysis.csv", index=False)

print("\nPipeline completed successfully.") 