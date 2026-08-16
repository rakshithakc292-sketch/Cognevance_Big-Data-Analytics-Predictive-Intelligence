import pandas as pd
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestRegressor

# Load dataset
df = pd.read_csv("Dataset/ecommerce_sales_data.csv")

# Convert date
df['Purchase Date'] = pd.to_datetime(
    df['Purchase Date'],
    errors='coerce'
)

# Create date features
df['Month'] = df['Purchase Date'].dt.month
df['Quarter'] = df['Purchase Date'].dt.quarter
df['Day_of_Week'] = df['Purchase Date'].dt.dayofweek

# Features
features = [
    'Price',
    'Quantity',
    'Customer Age',
    'Month',
    'Quarter',
    'Day_of_Week'
]

target = 'Total Sales'

# Remove missing values
model_data = df[features + [target]].dropna()

X = model_data[features]
y = model_data[target]

# Train Random Forest
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

model.fit(X, y)

# Feature importance
importance = pd.DataFrame({
    'Feature': features,
    'Importance': model.feature_importances_
})

importance = importance.sort_values(
    'Importance',
    ascending=False
)

print("========== FEATURE IMPORTANCE ==========")
print(importance)

# Save results
importance.to_csv(
    "Model/feature_importance.csv",
    index=False
)

# Create chart
plt.figure(figsize=(10, 6))

plt.bar(
    importance['Feature'],
    importance['Importance']
)

plt.title("Feature Importance - Random Forest")
plt.xlabel("Feature")
plt.ylabel("Importance")

plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()

plt.savefig(
    "Charts/feature_importance.png",
    dpi=300
)

plt.show()