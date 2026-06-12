# Automotive Parts Order Fulfillment Analytics

<img width="1411" height="786" alt="dashboard_main" src="https://github.com/user-attachments/assets/2c1f149d-9a87-4793-baa0-5b73b027937c" />


## 📊 Project Overview
This project is a comprehensive Power BI dashboard designed to analyze and optimize the flow of automotive parts orders across multiple regional branches. It tracks the distribution of orders across various sales channels (Body Shop, Service, Aftermarket, Subdealers) and monitors the critical balance between expedited (URGENT) and standard (STOCK) orders.

## 🎯 Business Value & Problem Solved
In the automotive parts supply chain, excessive urgent orders generate unnecessary logistical costs. This dashboard provides actionable insights to:
* Track the URGENT vs. STOCK ratio against the company's 32% target.
* Automatically calculate "Missing Stock Orders" to identify inventory planning gaps.
* Categorize order origins dynamically without relying on static, hard-coded data sources.

## ⚙️ Key Technical Features
* **Optimized Data Architecture:** Built on a strict **Star Schema** with a central, dynamically generated `Dim_Order` dictionary to eliminate many-to-many relationships and improve model performance.
* **Advanced DAX:** Utilization of variables (`VAR`), context transition handling, and text search functions (`CONTAINSSTRING`, `SWITCH`) to dynamically categorize complex order strings.
* **Custom Time Intelligence:** Implementation of a lightweight, DAX-generated `Dim_Date` table, bypassing Power BI's heavy auto-date/time feature.
* **Data Synthesis (Python):** The underlying dataset was generated using a custom Python script (Pandas, Random) to simulate realistic automotive parts demand, part numbers, and branch-specific probabilities.

## 🛠️ Tech Stack
* **Power BI Desktop** (Data Visualization & UI/UX)
* **DAX** (KPI calculations, text parsing, logical routing)
* **Power Query / M Language** (Data transformation, dynamic table appending)
* **Python** (Data generation and preprocessing)

## 🗂️ Data Model Structure
The model follows best practices with unidirectional 1:* relationships:
* **Fact Tables:** `Fct_Orders`, `Fct_ShopOrders`, `Fct_BodyShopOrders`
* **Dimension Tables:** * `Dim_Order` (Central dictionary created via Power Query append)
  * `Dim_Branch` (Regional mapping)
  * `Dim_Date` (DAX calendar)

## 🚀 How to view the project
1. Download the `Automotive_Order_Analytics.pbix` file.
2. Open it using Power BI Desktop.
3. The data is imported and fully self-contained within the model.
