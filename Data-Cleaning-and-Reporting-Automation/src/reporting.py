import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


def generate_analysis(df, chart_folder, report_folder):

    os.makedirs(chart_folder, exist_ok=True)
    os.makedirs(report_folder, exist_ok=True)

    print("\n" + "=" * 60)
    print("GENERATING REPORTS AND VISUALIZATIONS")
    print("=" * 60)

    total_revenue = df["Total_Sales"].sum()
    total_orders = df["Order_ID"].nunique()
    total_quantity = df["Quantity"].sum()
    average_order_value = df["Total_Sales"].mean()

    best_product = (
        df.groupby("Product")["Total_Sales"]
        .sum()
        .sort_values(ascending=False)
        .index[0]
    )

    top_city = (
        df.groupby("City")["Total_Sales"]
        .sum()
        .sort_values(ascending=False)
        .index[0]
    )

    print("\n--- BUSINESS METRICS ---")
    print(f"Total Revenue       : ₹{total_revenue:,.2f}")
    print(f"Total Orders        : {total_orders}")
    print(f"Total Quantity Sold : {total_quantity}")
    print(f"Average Order Value : ₹{average_order_value:,.2f}")
    print(f"Best Selling Product: {best_product}")
    print(f"Top Performing City : {top_city}")

    product_sales = df.groupby("Product")["Total_Sales"].sum().sort_values(ascending=False)

    plt.figure(figsize=(10, 6))
    product_sales.plot(kind="bar")
    plt.title("Sales by Product")
    plt.xlabel("Product")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(chart_folder, "sales_by_product.png"))
    plt.close()

    city_sales = df.groupby("City")["Total_Sales"].sum().sort_values(ascending=False)

    plt.figure(figsize=(8, 5))
    city_sales.plot(kind="bar")
    plt.title("Sales by City")
    plt.xlabel("City")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(chart_folder, "sales_by_city.png"))
    plt.close()

    category_sales = df.groupby("Category")["Total_Sales"].sum().sort_values(ascending=False)

    plt.figure(figsize=(7, 5))
    category_sales.plot(kind="bar")
    plt.title("Sales by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Sales")
    plt.tight_layout()
    plt.savefig(os.path.join(chart_folder, "sales_by_category.png"))
    plt.close()

    payment_counts = df["Payment_Method"].value_counts()

    plt.figure(figsize=(7, 5))
    payment_counts.plot(kind="bar")
    plt.title("Orders by Payment Method")
    plt.xlabel("Payment Method")
    plt.ylabel("Number of Orders")
    plt.tight_layout()
    plt.savefig(os.path.join(chart_folder, "payment_methods.png"))
    plt.close()

    numerical_data = df[["Quantity", "Unit_Price", "Total_Sales"]]

    plt.figure(figsize=(7, 5))
    sns.heatmap(numerical_data.corr(), annot=True, cmap="coolwarm")
    plt.title("Sales Data Correlation")
    plt.tight_layout()
    plt.savefig(os.path.join(chart_folder, "correlation_heatmap.png"))
    plt.close()

    report_path = os.path.join(
        report_folder,
        "sales_automation_report.xlsx"
    )

    with pd.ExcelWriter(report_path, engine="openpyxl") as writer:

        df.to_excel(writer, sheet_name="Cleaned Data", index=False)

        product_sales.to_frame("Total Sales").to_excel(
            writer, sheet_name="Product Sales"
        )

        city_sales.to_frame("Total Sales").to_excel(
            writer, sheet_name="City Sales"
        )

        category_sales.to_frame("Total Sales").to_excel(
            writer, sheet_name="Category Sales"
        )

        summary = pd.DataFrame({
            "Metric": [
                "Total Revenue",
                "Total Orders",
                "Total Quantity",
                "Average Order Value",
                "Best Selling Product",
                "Top Performing City"
            ],
            "Value": [
                total_revenue,
                total_orders,
                total_quantity,
                average_order_value,
                best_product,
                top_city
            ]
        })

        summary.to_excel(writer, sheet_name="Summary", index=False)

    print("\nExcel report generated successfully!")
    print(f"Report saved to: {report_path}")
    print("\nCharts generated successfully!")