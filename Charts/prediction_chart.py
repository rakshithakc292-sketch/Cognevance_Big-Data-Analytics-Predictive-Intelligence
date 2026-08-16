import pandas as pd
import matplotlib.pyplot as plt

# Load prediction results
df = pd.read_csv("Model/prediction_results.csv")

# Create chart
plt.figure(figsize=(14, 6))

plt.plot(
    df.index,
    df['Actual Sales'],
    label='Actual Sales'
)

plt.plot(
    df.index,
    df['Predicted Sales'],
    label='Predicted Sales'
)

plt.title("Actual vs Predicted Sales")
plt.xlabel("Test Data Records")
plt.ylabel("Sales")

plt.legend()
plt.grid(True)
plt.tight_layout()

# Save chart
plt.savefig(
    "Charts/prediction_vs_actual.png",
    dpi=300
)

plt.show()