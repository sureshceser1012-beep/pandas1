import pandas as pd


# 1. Load CSV and set date as index
df = pd.read_csv("sales_data.csv", parse_dates=["date"])
df.set_index("date", inplace=True)


# 2. Create average_price column
df["average_price"] = df["revenue"] / df["units_sold"]


# 3. Total revenue and units sold for each product
summary = df.groupby("product_id").agg(
    total_revenue=("revenue", "sum"),
    total_units=("units_sold", "sum")
)


print("Sales Data:")
print(df)

print("\nProduct Summary:")
print(summary)