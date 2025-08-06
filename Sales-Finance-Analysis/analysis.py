"""
analysis.py  ·  Pure‑Python analysis for the Sales & Finance project
Run:  python analysis.py
Creates: PNG charts in plots/  ·  Prints key insights to the terminal
""" 

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ── 1.  CONFIG  ────────────────────────────────────────────────────────────
DATA_DIR  = "data"
PLOTS_DIR = "plots"
os.makedirs(PLOTS_DIR, exist_ok=True)          # auto‑create plots/ if missing
sns.set_theme(style="whitegrid")               # global plot style

# ── 2.  LOAD DATA  ─────────────────────────────────────────────────────────
sales_path   = os.path.join(DATA_DIR, "sales_data_sample.csv")
finance_path = os.path.join(DATA_DIR, "Finance_data.csv")

sales_df   = pd.read_csv(sales_path,   encoding="latin1")
finance_df = pd.read_csv(finance_path, encoding="latin1")

# ── 3.  CLEAN & FEATURE ENGINEERING  ───────────────────────────────────────
sales_df["ORDERDATE"]  = pd.to_datetime(sales_df["ORDERDATE"])
sales_df["OrderMonth"] = sales_df["ORDERDATE"].dt.to_period("M")
sales_df["YEAR_ID"]    = sales_df["YEAR_ID"].astype(str)

# ── 4.  SALES ANALYSIS + CHARTS  ───────────────────────────────────────────
def monthly_revenue_plot():
    monthly = sales_df.groupby("OrderMonth")["SALES"].sum()
    plt.figure(figsize=(10, 5))
    monthly.plot(marker="o")
    plt.title("Monthly Revenue")
    plt.xlabel("Month")
    plt.ylabel("Sales (USD)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    path = os.path.join(PLOTS_DIR, "monthly_revenue.png")
    plt.savefig(path, dpi=300);  plt.close();  return path

def product_mix_plot():
    prod_sales = sales_df.groupby("PRODUCTLINE")["SALES"].sum().sort_values()
    plt.figure(figsize=(10, 6))
    prod_sales.plot(kind="barh")
    plt.title("Sales by Product Line")
    plt.xlabel("Sales (USD)")
    plt.tight_layout()
    path = os.path.join(PLOTS_DIR, "sales_by_productline.png")
    plt.savefig(path, dpi=300);  plt.close();  return path

# ── 5.  FINANCE ANALYSIS + CHARTS  ─────────────────────────────────────────
def age_distribution_plot():
    plt.figure(figsize=(8, 5))
    sns.histplot(finance_df["age"], kde=True, bins=20)
    plt.title("Investor Age Distribution")
    plt.tight_layout()
    path = os.path.join(PLOTS_DIR, "finance_age_histogram.png")
    plt.savefig(path, dpi=300);  plt.close();  return path

def finance_corr_heatmap():
    corr = finance_df.select_dtypes("number").corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm")
    plt.title("Correlation Heat‑map – Financial Metrics")
    plt.tight_layout()
    path = os.path.join(PLOTS_DIR, "finance_corr_heatmap.png")
    plt.savefig(path, dpi=300);  plt.close();  return path

# ── 6.  INSIGHTS  ──────────────────────────────────────────────────────────
def print_insights():
    top_customers = (sales_df.groupby("CUSTOMERNAME")["SALES"]
                     .sum().sort_values(ascending=False).head(3))
    best_year  = (sales_df.groupby("YEAR_ID")["SALES"].sum().idxmax())
    best_prod  = (sales_df.groupby("PRODUCTLINE")["SALES"]
                  .sum().idxmax())

    print("\n💡  Business Insights")
    print("─────────────────────")
    print("Top‑3 customers by total sales:")
    print(top_customers.to_string(), "\n")
    print(f"Year with highest revenue : {best_year}")
    print(f"Best‑performing product   : {best_prod}\n")

# ── 7.  MAIN ───────────────────────────────────────────────────────────────
def main():
    paths = [monthly_revenue_plot(), product_mix_plot(),
             age_distribution_plot(), finance_corr_heatmap()]
    print_insights()
    print("Saved plots ➜", *paths, sep="\n  • ")

if __name__ == "__main__":
    main()



