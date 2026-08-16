import sqlite3
import pandas as pd
from pathlib import Path

# Find the main project folder automatically
PROJECT_FOLDER = Path(__file__).resolve().parent.parent

# Database location
DATABASE_PATH = PROJECT_FOLDER / "SQL" / "ecommerce_sales.db"

print("Database location:")
print(DATABASE_PATH)

# Connect to database
connection = sqlite3.connect(DATABASE_PATH)

# Check tables in database
tables = pd.read_sql_query(
    "SELECT name FROM sqlite_master WHERE type='table';",
    connection
)

print("\nTables in database:")
print(tables)

# Stop if the required table does not exist
if "ecommerce_sales_data" not in tables["name"].values:
    print("\nERROR: ecommerce_sales_data table was not found.")
    print("Run load_data_to_sql.py again.")
    connection.close()
    exit()

print("\n========== SQL BUSINESS ANALYSIS ==========")

# 1. Total Sales
query = '''
SELECT SUM("Total Sales") AS Total_Sales
FROM ecommerce_sales_data
'''

result = pd.read_sql_query(query, connection)
print("\nTotal Sales:")
print(result)


# 2. Total Quantity
query = '''
SELECT SUM(Quantity) AS Total_Quantity
FROM ecommerce_sales_data
'''

result = pd.read_sql_query(query, connection)
print("\nTotal Quantity Sold:")
print(result)


# 3. Total Orders
query = '''
SELECT COUNT(DISTINCT "Order ID") AS Total_Orders
FROM ecommerce_sales_data
'''

result = pd.read_sql_query(query, connection)
print("\nTotal Orders:")
print(result)


# 4. Total Customers
query = '''
SELECT COUNT(DISTINCT "Customer ID") AS Total_Customers
FROM ecommerce_sales_data
'''

result = pd.read_sql_query(query, connection)
print("\nTotal Customers:")
print(result)


# 5. Sales by Category
query = '''
SELECT
    Category,
    SUM("Total Sales") AS Total_Sales
FROM ecommerce_sales_data
GROUP BY Category
ORDER BY Total_Sales DESC
'''

result = pd.read_sql_query(query, connection)
print("\nSales by Category:")
print(result)


# 6. Sales by Gender
query = '''
SELECT
    "Customer Gender",
    SUM("Total Sales") AS Total_Sales
FROM ecommerce_sales_data
GROUP BY "Customer Gender"
ORDER BY Total_Sales DESC
'''

result = pd.read_sql_query(query, connection)
print("\nSales by Gender:")
print(result)


# 7. Top 10 Products
query = '''
SELECT
    "Product Name",
    SUM("Total Sales") AS Total_Sales
FROM ecommerce_sales_data
GROUP BY "Product Name"
ORDER BY Total_Sales DESC
LIMIT 10
'''

result = pd.read_sql_query(query, connection)
print("\nTop 10 Products:")
print(result)


# 8. Average Order Value
query = '''
SELECT AVG("Total Sales") AS Average_Order_Value
FROM ecommerce_sales_data
'''

result = pd.read_sql_query(query, connection)
print("\nAverage Order Value:")
print(result)


connection.close()

print("\n========== SQL ANALYSIS COMPLETED ==========")