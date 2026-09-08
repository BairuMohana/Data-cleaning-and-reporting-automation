import os

from data_cleaning import load_data, clean_data, save_cleaned_data
from reporting import generate_analysis


BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

RAW_DATA = os.path.join(
    BASE_DIR, "data", "raw_data.csv"
)

CLEANED_DATA = os.path.join(
    BASE_DIR, "data", "cleaned_data.csv"
)

CHART_FOLDER = os.path.join(
    BASE_DIR, "outputs", "charts"
)

REPORT_FOLDER = os.path.join(
    BASE_DIR, "outputs", "reports"
)


def main():

    print("\n")
    print("*" * 60)
    print("   DATA CLEANING & REPORTING AUTOMATION")
    print("*" * 60)

    df = load_data(RAW_DATA)

    cleaned_df = clean_data(df)

    save_cleaned_data(
        cleaned_df,
        CLEANED_DATA
    )

    generate_analysis(
        cleaned_df,
        CHART_FOLDER,
        REPORT_FOLDER
    )

    print("\n" + "=" * 60)
    print("PROJECT COMPLETED SUCCESSFULLY!")
    print("=" * 60)

    print("\nGenerated files:")
    print("1. data/cleaned_data.csv")
    print("2. outputs/charts/")
    print("3. outputs/reports/sales_automation_report.xlsx")


if __name__ == "__main__":
    main()