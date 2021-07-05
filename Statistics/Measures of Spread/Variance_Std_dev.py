#Import the library
import pandas as pd

# Import the dataset
data = pd.read_csv("https://raw.githubusercontent.com/RaghurajSawant/MachineLearning/master/Statistics/Measures%20of%20Spread/Spread%20of%20Data.csv")
data.head(5)

#Calculating the variance
var_data = data["Overall Marks"].var(ddof = 0)
print(var_data)

#Calculating the Standard Deviation
StdDev_data = data["Overall Marks"].std(ddof = 0)
print(StdDev_data)
