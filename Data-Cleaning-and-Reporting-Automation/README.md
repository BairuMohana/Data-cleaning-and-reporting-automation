# Data Cleaning & Reporting Automation

## Project Overview

Data Cleaning & Reporting Automation is a Python-based project that automates the process of cleaning raw sales data, performing analysis, generating visualizations, and creating an Excel report.

## Objectives

- Clean raw sales data
- Remove duplicate records
- Handle missing values
- Convert data types
- Validate data
- Analyze sales performance
- Generate charts
- Create automated Excel reports

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- OpenPyXL

## Project Structure

Data-Cleaning-and-Reporting-Automation/

├── data/
│   ├── raw_data.csv
│   └── cleaned_data.csv
│
├── outputs/
│   ├── charts/
│   └── reports/
│
├── src/
│   ├── data_cleaning.py
│   ├── reporting.py
│   └── main.py
│
├── notebooks/
├── requirements.txt
├── README.md
└── .gitignore

## Features

### Data Cleaning
- Missing value detection
- Missing value handling
- Duplicate removal
- Data type conversion
- Invalid data filtering

### Data Analysis

The project calculates:

- Total Revenue
- Total Orders
- Total Quantity Sold
- Average Order Value
- Best Selling Product
- Top Performing City

### Data Visualization

The project generates:

- Sales by Product
- Sales by City
- Sales by Category
- Payment Method Analysis
- Correlation Heatmap

### Automated Reporting

An Excel report is generated containing:

- Cleaned Data
- Product Sales
- City Sales
- Category Sales
- Summary

## How to Run

### Install dependencies

```bash
pip install -r requirements.txt