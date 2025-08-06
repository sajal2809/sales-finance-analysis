📊 Sales & Finance Analysis with Python
A lightweight Python project that performs insightful analysis and visualization of sales and finance data—ideal for showcasing analytical skills in business intelligence, financial reporting, or data analytics.

🧠 Project Overview
This project analyzes a sample sales dataset alongside financial/investor data to:
Understand monthly revenue trends
Explore sales by product lines
Visualize customer demographics
Uncover correlations between financial metrics
Generate business insights from raw datasets
It is entirely built in Python, uses pandas, seaborn, and matplotlib, and outputs high-quality plots and terminal insights for reporting or dashboard integration.

🏗️ Project Structure
Sales-Finance-Analysis/
│
├── data/
│   ├── sales_data_sample.csv       ← Raw sales transactions
│   └── Finance_data.csv            ← Customer/finance dataset
│
├── plots/
│   └── *.png                       ← Automatically generated visualizations
│
├── analysis.py                     ← Main Python script
└── README.md                       ← Documentation

🚀 How to Run
1. Clone the Repository
   git clone https://github.com/sajal2809/sales-finance-analysis.git
   cd sales-finance-analysis/Sales-Finance-Analysis
2. Install Dependencies
   Make sure you have Python 3.7+ and install required libraries:
   pip install pandas numpy matplotlib seaborn
3. Run the Script
   python analysis.py
This will:
Print key business insights in the terminal
Generate PNG plots inside the plots/ directory

📈 Features & Visualizations
✅ Sales Analysis
Monthly Revenue Trend
Line chart showing monthly sales totals
Saved as: plots/monthly_revenue.png
Product Line Contribution
Horizontal bar chart of sales by product category
Saved as: plots/sales_by_productline.png

✅ Finance/Investor Analysis
Age Distribution
Histogram with KDE overlay for age demographics
Saved as: plots/finance_age_histogram.png
Correlation Heatmap
Correlation matrix of numeric finance data
Saved as: plots/finance_corr_heatmap.png

✅ Business Insights 
Top 3 customers by sales
Best revenue year
Top-performing product line

👨‍💻 Tech Stack
| Tool         | Purpose                         |
| ------------ | ------------------------------- |
| `pandas`     | Data manipulation & grouping    |
| `matplotlib` | Core plotting                   |
| `seaborn`    | Themed, publication-style plots |
| `numpy`      | Numerical ops (optional)        |
| `os`         | Directory/file path management  |



