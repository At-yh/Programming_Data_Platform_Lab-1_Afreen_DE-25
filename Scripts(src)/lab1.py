import pandas as pd

# STEP 1: INGEST
df = pd.read_csv("data/lab1_products.csv", sep=";")  # This reads raw csv & stores in it memory as a DataFrame(df)

print(df.head())
print(df.info())