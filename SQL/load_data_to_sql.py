import pandas as pd
import sqlite3
from pathlib import Path

# Find the main project folder
PROJECT_FOLDER = Path(__file__).resolve().parent.parent

# Dataset location
DATASET_PATH = PROJECT_FOLDER / "Dataset" / "ecommerce_sales_data.csv"

# Database location
DATABASE_PATH = PROJECT_FOLDER / "SQL" / "ecommerce_sales.db"

print("Dataset:")
print(DATASET_PATH)

print("\nDatabase:")
print(DATABASE_PATH)

# Load dataset
df = pd.read_csv(DATASET_PATH)

print("\nDataset loaded successfully!")
print("Number of records:", len(df))

# Create SQLite database
connection = sqlite3.connect(DATABASE_PATH)

# Create SQL table
df.to_sql(
    "ecommerce_sales_data",
    connection,
    if_exists="replace",
    index=False
)

# Check table
tables = pd.read_sql_query(
    "SELECT name FROM sqlite_master WHERE type='table';",
    connection
)

print("\nTables created:")
print(tables)

connection.close()

print("\nDatabase created successfully!")