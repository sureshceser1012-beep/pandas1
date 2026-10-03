import pandas as pd


def load_sales_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["date"])
    return df.set_index("store_id")


def clean_sales_data(df: pd.DataFrame) -> pd.DataFrame:
    cleaned = df.dropna().copy()

    cleaned = cleaned.assign(
        total_sales=cleaned["units_sold"] * cleaned["unit_price"],
        quarter="Q" + cleaned["date"].dt.quarter.astype(str)
    )

    return cleaned


def sales_summary(df: pd.DataFrame) -> pd.DataFrame:
    summary = (
        df.groupby(["region", "quarter"])
        .agg(
            sum_units=("units_sold", "sum"),
            sum_revenue=("total_sales", "sum"),
            avg_price=("unit_price", "mean")
        )
    )

    return summary


sales_data = load_sales_data("salesdata3.csv")

cleaned_data = clean_sales_data(sales_data)

summary = sales_summary(cleaned_data)


print("Cleaned Data:")
print(cleaned_data)

print("\nSales Summary:")
print(summary)