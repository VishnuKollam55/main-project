import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Load water quality dataset
data = pd.read_csv("../Dataset/water_quality.csv")

# Features and target
X = data[['pH', 'Dissolved_Oxygen', 'Turbidity']]
y = data['Water_Quality_Index']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
mse = mean_squared_error(y_test, y_pred)
print("Water Quality Prediction MSE:", mse)

# Plot
plt.plot(y_test.values, label="Actual WQI")
plt.plot(y_pred, label="Predicted WQI")
plt.xlabel("Samples")
plt.ylabel("Water Quality Index")
plt.title("Water Quality Prediction")
plt.legend()
plt.show()
