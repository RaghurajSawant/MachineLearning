
#Import the library
import pandas as pd

# Import the dataset
data = pd.read_csv("https://raw.githubusercontent.com/RaghurajSawant/MachineLearning/master/Statistics/Measures%20of%20Spread/Spread%20of%20Data.csv")
data.head(5)

# Identify the minimum data point
min_data = data["Overall Marks"].min()
print(min_data)

# Identify the minimum data point
max_data = data["Overall Marks"].max()
print(max_data)

# Calculating the range
Range = max_data - min_data
print(Range)

# Calculating the 1st and 3rd quartiles
Q1 = data["Overall Marks"].quantile(0.25)
Q3 = data["Overall Marks"].quantile(0.75)

# Calculating the inter-quartile range
IQR = Q3 - Q1
print(IQR)
