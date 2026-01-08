import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Load air quality dataset
data = pd.read_csv("../Dataset/air_quality.csv")

# Features and target
X = data[['PM2_5', 'PM10', 'CO']]
y = data['AQI']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Error
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Plot result
plt.plot(y_test.values, label="Actual AQI")
plt.plot(y_pred, label="Predicted AQI")
plt.xlabel("Samples")
plt.ylabel("AQI")
plt.title("Air Pollution Prediction using Random Forest")
plt.legend()
plt.show()
object