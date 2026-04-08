import pandas as pd

def fill_pivot_with_column_means(pivot_df):
    for column in pivot_df.columns:
        if pivot_df[column].dtype != "O":
            mean_value = pivot_df[column].mean()
            pivot_df[column] = pivot_df[column].fillna(mean_value)
    return pivot_df

def ask_export_to_excel(df):
    choice = input("Do you want to export these results to Excel? (y/n): ").strip().lower()

    if choice == "y":
        filename = input("Enter Excel filename (example: results.xlsx): ").strip()

        if not filename:
            print("No filename entered. Export cancelled.")
            return

        if not filename.endswith(".xlsx"):
            filename += ".xlsx"

        try:
            df.to_excel(filename)
            print(f"Results exported successfully to {filename}")
        except Exception as e:
            print(f"Error exporting file: {e}")

def total_sales_by_region_and_order_type(df):
    pivot = pd.pivot_table(
        df,
        values="sale_price",
        index="sales_region",
        columns="order_type",
        aggfunc="sum"
    )

    pivot = fill_pivot_with_column_means(pivot)

    print("\nTotal Sales by Region and Order Type:")
    print(pivot)

    ask_export_to_excel(pivot)

try:
    df = pd.read_csv("sales_data_test.csv")
    total_sales_by_region_and_order_type(df)
except Exception as e:
    print(f"Error loading file: {e}")