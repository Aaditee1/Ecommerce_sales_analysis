#  E-Commerce Sales Analysis using Python & Pandas

##  Project Overview
This project focuses on **sales analysis of an e-commerce platform** using Python and Pandas.  
The objective is to understand how **revenue is influenced by pricing, discounts, product categories, and sales volume**.

The analysis is performed on a large transactional dataset to extract **business-relevant insights**, not just visualizations.

---

##  Dataset Description
The dataset contains **100,000 e-commerce transactions** with the following key attributes:

- **Transaction_ID** – Unique transaction identifier  
- **Customer_ID** – Customer identifier  
- **Product_ID** – Product identifier  
- **Transaction_Date** – Date of transaction  
- **Category** – Product category (Books, Electronics, Clothing, etc.)  
- **Units_Sold** – Number of units sold  
- **Revenue** – Total revenue generated  
- **Discount_Applied** – Discount applied on transaction  
- **Ad_CTR, Ad_CPC, Ad_Spend** – Marketing-related metrics  

###  Derived Feature
- **Price** = Revenue / Units_Sold

---

##  Data Preparation
- Verified dataset structure and data types  
- Converted date columns to datetime format  
- Created a **Price** column to analyze unit-level pricing  
- Maintained separation between **raw** and **processed** data  

---

##  Sales Analysis Performed

### 1️) Revenue by Product Category
- Compared total revenue across different product categories  
- Identified top revenue-contributing categories  

**Insight:**  
Revenue distribution varies significantly by category, indicating differences in pricing strategy and demand.

---

### 2️) Units Sold vs Revenue
- Performed correlation analysis between **Units_Sold** and **Revenue**  
- Observed a **very weak correlation** across all categories  

**Insight:**  
Higher sales volume does **not necessarily translate to higher revenue**.

---

### 3️) Discount Impact on Revenue
- Analyzed correlation between **Discount_Applied** and **Revenue**  
- Observed a **weak negative relationship**  

**Insight:**  
Discounting does not effectively increase total revenue and may slightly reduce it.

---

### 4️) Pricing Analysis by Category
- Calculated average price per unit for each product category  
- Compared pricing behavior across categories  

**Insight:**  
Revenue is primarily **price-driven**, not volume-driven.  
Categories with higher average prices contribute more to total revenue.

---

### 5️) Key Correlation Findings
- Strong positive correlation between **Price** and **Revenue**  
- Weak correlation between **Units_Sold** and **Revenue**  
- Weak negative correlation between **Discounts** and **Revenue**

---

##  Key Business Insights
- Revenue growth is driven more by **pricing strategy** than quantity sold  
- Discounts are not an effective revenue-growth mechanism  
- Product categories follow different pricing dynamics  
- Unit sales alone are not a reliable performance metric  

---

##  Tools & Technologies Used
- **Python**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **VS Code**
- **Git & GitHub**

---

##  Project Structure
Ecommerce_sales_analysis/
│
├── data/
│ ├── raw/
│ └── processed/
│
├── notebooks/
│ └── ecommerce_analysis.ipynb
│
├── src/
│ └── data_cleaning.py
│
├── visuals/
├── README.md
├── requirements.txt
└── .gitignore

---

##  Conclusion
This project demonstrates a **practical e-commerce sales analysis workflow** using Python and Pandas.  
The insights derived can help businesses optimize **pricing strategies, discount policies, and revenue generation**.

---

###  Project Status: Completed (Sales Analysis)
