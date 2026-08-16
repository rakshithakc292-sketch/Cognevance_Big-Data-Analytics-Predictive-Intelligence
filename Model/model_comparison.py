import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
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

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# -------------------------------
# Linear Regression
# -------------------------------

linear_model = LinearRegression()

linear_model.fit(
    X_train,
    y_train
)

linear_predictions = linear_model.predict(X_test)

linear_mae = mean_absolute_error(
    y_test,
    linear_predictions
)

linear_rmse = np.sqrt(
    mean_squared_error(
        y_test,
        linear_predictions
    )
)

linear_r2 = r2_score(
    y_test,
    linear_predictions
)


# -------------------------------
# Random Forest
# -------------------------------

rf_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

rf_model.fit(
    X_train,
    y_train
)

rf_predictions = rf_model.predict(X_test)

rf_mae = mean_absolute_error(
    y_test,
    rf_predictions
)

rf_rmse = np.sqrt(
    mean_squared_error(
        y_test,
        rf_predictions
    )
)

rf_r2 = r2_score(
    y_test,
    rf_predictions
)


# -------------------------------
# Model Comparison
# -------------------------------

print("========== MODEL COMPARISON ==========")

print("\nLinear Regression")
print("MAE:", linear_mae)
print("RMSE:", linear_rmse)
print("R² Score:", linear_r2)

print("\nRandom Forest")
print("MAE:", rf_mae)
print("RMSE:", rf_rmse)
print("R² Score:", rf_r2)

# --------------------------------
# Select Best Model
# --------------------------------

if rf_r2 > linear_r2:
    best_model = "Random Forest"
    best_r2 = rf_r2
else:
    best_model = "Linear Regression"
    best_r2 = linear_r2

print("\n========== BEST MODEL ==========")
print("Best Model:", best_model)
print("Best R² Score:", best_r2)

# Save model comparison results

comparison = pd.DataFrame({
    "Model": [
        "Linear Regression",
        "Random Forest"
    ],
    "MAE": [
        linear_mae,
        rf_mae
    ],
    "RMSE": [
        linear_rmse,
        rf_rmse
    ],
    "R2 Score": [
        linear_r2,
        rf_r2
    ]
})

comparison.to_csv(
    "Model/model_comparison_results.csv",
    index=False
)

print("\nModel comparison results saved successfully.")

# --------------------------------
# Generate Prediction Results
# --------------------------------

if rf_r2 > linear_r2:
    final_model = rf_model
    final_predictions = rf_predictions
else:
    final_model = linear_model
    final_predictions = linear_predictions

# Create prediction results
prediction_results = X_test.copy()

prediction_results['Actual Sales'] = y_test.values
prediction_results['Predicted Sales'] = final_predictions

# Calculate prediction error
prediction_results['Prediction Error'] = (
    prediction_results['Actual Sales']
    - prediction_results['Predicted Sales']
)

# Save prediction results
prediction_results.to_csv(
    "Model/prediction_results.csv",
    index=False
)

print("\nPrediction results saved successfully.")

print("\nFirst 10 Predictions:")
print(prediction_results.head(10))