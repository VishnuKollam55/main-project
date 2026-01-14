import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load noise dataset
data = pd.read_csv("../Dataset/noise_level.csv")

# Encode categorical columns
le_area = LabelEncoder()
le_level = LabelEncoder()

data['Area_Type'] = le_area.fit_transform(data['Area_Type'])
data['Noise_Level'] = le_level.fit_transform(data['Noise_Level'])

# Features and target
X = data[['Area_Type', 'Noise_dB']]
y = data['Noise_Level']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Noise Level Classification Accuracy:", accuracy)

print("\nClassification Report:")
print(classification_report(y_test, y_pred))
import matplotlib.pyplot as plt

labels = ['Low', 'Medium', 'High']
values = data['Noise_Level'].value_counts().sort_index()

plt.bar(labels[:len(values)], values)
plt.xlabel("Noise Level")
plt.ylabel("Count")
plt.title("Noise Pollution Level Distribution")
plt.show()
