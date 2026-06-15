import pandas as pd
import glob

# Step 1: Load all 3 CSV files and combine them
files = glob.glob("data/daily_sales_data_*.csv")
dfs = [pd.read_csv(f) for f in files]
data = pd.concat(dfs, ignore_index=True)

# Step 2: Filter for Pink Morsel only
data = data[data["product"] == "pink morsel"].copy()

# Step 3: Clean price (remove "$") and calculate sales = price x quantity
data["price"] = data["price"].str.replace("$", "", regex=False).astype(float)
data["sales"] = data["price"] * data["quantity"]

# Step 4: Keep only the required columns: sales, date, region
output = data[["sales", "date", "region"]]

# Step 5: Save to a single output CSV
output.to_csv("data/output.csv", index=False)

print(f"Done! {len(output)} rows written to data/output.csv")
print(output.head())
