import pandas as pd
import os

# Create Dashboard data folder
os.makedirs("Dashboard/Data", exist_ok=True)

# Load main dataset
df = pd.read_csv("Dataset/ecommerce_sales_data.csv")

# Convert date
df['Purchase Date'] = pd.to_datetime(
    df['Purchase Date'],
    errors='coerce'
)

# Create date features
df['Year'] = df['Purchase Date'].dt.year
df['Month'] = df['Purchase Date'].dt.month
df['Quarter'] = df['Purchase Date'].dt.quarter

# Save dashboard dataset
df.to_csv(
    "Dashboard/Data/dashboard_sales_data.csv",
    index=False
)

# Model comparison
model_comparison = pd.read_csv(
    "Model/model_comparison_results.csv"
)

model_comparison.to_csv(
    "Dashboard/Data/model_comparison_results.csv",
    index=False
)

# Prediction results
prediction_results = pd.read_csv(
    "Model/prediction_results.csv"
)

prediction_results.to_csv(
    "Dashboard/Data/prediction_results.csv",
    index=False
)

# Feature importance
feature_importance = pd.read_csv(
    "Model/feature_importance.csv"
)

feature_importance.to_csv(
    "Dashboard/Data/feature_importance.csv",
    index=False
)

print("========== DASHBOARD DATA ==========")
print("Dashboard data preparation completed.")

print("\nFiles created:")
print("1. dashboard_sales_data.csv")
print("2. model_comparison_results.csv")
print("3. prediction_results.csv")
print("4. feature_importance.csv")