import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Connect to the SQLite database
conn = sqlite3.connect("sales_data.db")

# Step 2: Run SQL query to get total quantity and revenue by product
query = """
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
"""
df = pd.read_sql_query(query, conn)

# Step 3: Display the summary
print("Sales Summary by Product:\n")
print(df)

# Step 4: Plot a simple bar chart of revenue per product
plt.figure(figsize=(8, 6))
df.plot(kind='bar', x='product', y='revenue', legend=False, color='skyblue')
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()

# Step 5: Save the chart (optional)
plt.savefig("sales_chart.png")
plt.show()

# Close the database connection
conn.close()
