#Import pandas library
import pandas as pd

# Import the dataset
data = pd.read_csv("https://raw.githubusercontent.com/RaghurajSawant/MachineLearning/master/Statistics/Measures_Of_Central_Tendency/Mode/mode.csv")
data.head(5)

# Use the mean function on the 'Overall Marks' column of the dataset
data["Overall Marks"].median()
