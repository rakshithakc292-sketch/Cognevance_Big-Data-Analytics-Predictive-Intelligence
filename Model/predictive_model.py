import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

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

# Select features
features = [
    'Price',
    'Quantity',
    'Customer Age',
    'Month',
    'Quarter',
    'Day_of_Week'
]

target = 'Total Sales'

# Remove missing values required for modeling
model_data = df[features + [target]].dropna()

X = model_data[features]
y = model_data[target]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("Training records:", len(X_train))
print("Testing records:", len(X_test))

# Create Random Forest model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

# Train model
model.fit(X_train, y_train)

print("\nModel training completed!")

# Predictions
y_pred = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, y_pred)

rmse = np.sqrt(
    mean_squared_error(y_test, y_pred)
)

r2 = r2_score(y_test, y_pred)

print("\n========== MODEL EVALUATION ==========")
print("MAE:", mae)
print("RMSE:", rmse)
print("R² Score:", r2)