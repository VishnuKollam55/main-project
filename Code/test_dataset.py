import pandas as pd

# Load datasets
air = pd.read_csv("../Dataset/air_quality.csv")
water = pd.read_csv("../Dataset/water_quality.csv")
noise = pd.read_csv("../Dataset/noise_level.csv")

# Display first 5 rows
print("Air Quality Data:")
print(air.head())

print("\nWater Quality Data:")
print(water.head())

print("\nNoise Level Data:")
print(noise.head())
o