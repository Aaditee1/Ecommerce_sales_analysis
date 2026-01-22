#  E-Commerce Sales Analysis

##  Project Overview
This project focuses on analyzing e-commerce sales data using **Python and Pandas**.  
The goal is to extract meaningful business insights related to **sales performance, pricing, discounts, and product categories**.

This project demonstrates real-world **data analysis workflow**, including data loading, cleaning, exploration, and insight generation.

---

##  Dataset
- Source: Synthetic E-Commerce Dataset (CSV format)
- Records: ~100,000 transactions
- Key columns include:
  - `Transaction_ID`
  - `Category`
  - `Units_Sold`
  - `Revenue`
  - `Discount_Applied`
  - `Price` (derived)

The dataset represents multiple product categories such as **Electronics, Books, Clothing, Toys, and Home Appliances**.

---

##  Analysis Performed (Sales Analysis)
The following analyses were performed using **Pandas**:

- Revenue distribution across product categories
- Units sold vs revenue relationship
- Impact of discounts on revenue
- Price comparison across categories
- Correlation analysis between:
  - Units Sold and Revenue
  - Discount Applied and Revenue

---

##  Key Insights
- Electronics generated the highest total revenue among all categories
- Higher discounts show a **negative correlation** with revenue
- Units sold and revenue have a **weak positive correlation**
- Average product price varies significantly across categories

---

##  Tools & Technologies
- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook
- Git & GitHub

---

##  Project Structure
Ecommerce_sales_analysis/
│
├── data/
│ ├── raw/ # Raw dataset (not tracked)
│ └── processed/ # Cleaned data
│
├── notebooks/
│ └── ecommerce_analysis.ipynb
│
├── src/
│ └── data_cleaning.py
│
├── visuals/
│
├── README.md
├── requirements.txt
└── .gitignore
##  How to Run
1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   
> Note: This project is designed to be run in Jupyter Notebook.   