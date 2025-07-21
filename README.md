# 🛒 Online Retail Purchase Analysis

This project analyzes transactional data from an online retail store using Python (Pandas, Seaborn, Matplotlib). The goal is to explore customer behavior, sales patterns, and key revenue insights through data visualization and analysis.

---

## 📁 Dataset

- **Source**: [Online Retail Dataset](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/07_Visualization/Online_Retail/Online_Retail.csv)
- **Size**: ~500K rows of transactional data
- **Fields**: `InvoiceNo`, `StockCode`, `Description`, `Quantity`, `InvoiceDate`, `UnitPrice`, `CustomerID`, `Country`

---

## 🔍 Key Analysis Steps

1. **Data Loading and Cleaning**
   - Removed negative quantities
   - Handled encoding issues (`latin1`)
   - Computed derived fields (e.g. `Revenue`)

2. **Visualizations**
   - Bar chart: Top 10 countries by quantity (excluding UK)
   - Scatterplots:
     - Quantity vs UnitPrice (by CustomerID)
     - Quantity vs AvgPrice (by country and globally)
   - Revenue vs Unit Price (bucketed)

3. **Insights**
   - Most purchases come from inexpensive items
   - Quantity drops sharply as price increases
   - Revenue is concentrated in items priced $1–$3

---

## 📊 Libraries Used

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`

