# Task7_Elevate_Labs
# 📊 Basic Sales Summary using SQLite and Python

This project demonstrates how to connect to a SQLite database using Python, run basic SQL queries to analyze sales data, and visualize the results using `matplotlib`.

## 📁 Files Included

- `basic_sales_summary.py` – Main Python script to extract and plot sales summary.
- `sales_data.db` – SQLite database file with a single table: `sales`.
- `sales_chart.png` – Auto-generated bar chart showing revenue per product (optional output).

## 🛠 Tools Used

- Python
- SQLite (via `sqlite3`)
- pandas
- matplotlib

## 🔍 What It Does

1. Connects to a SQLite database.
2. Runs an SQL query to calculate:
   - Total quantity sold per product
   - Total revenue (quantity × price) per product
3. Displays the results using:
   - `print()` for tabular summary
   - `matplotlib` for a simple bar chart

## ▶️ How to Run

1. Ensure you have Python installed.
2. Install required packages (if not already installed):

   ```bash
   pip install pandas matplotlib
Run the script:

bash
Copy
Edit
python basic_sales_summary.py
The script will:

Print a table of product-wise sales summary.

Display and save a bar chart as sales_chart.png.

🧪 Sample SQL Table Structure
sql
Copy
Edit
CREATE TABLE sales (
    id INTEGER PRIMARY KEY,
    product TEXT,
    quantity INTEGER,
    price REAL
);
📈 Example Chart Output
(Screenshot of sales_chart.png goes here if uploaded)
![Sales Chart](sales_chart.png)

📝 License
This project is open-source and available under the MIT License.
