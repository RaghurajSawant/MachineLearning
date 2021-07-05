#Import pandas library
import pandas as pd

# Import the dataset
data = pd.read_csv("https://raw.githubusercontent.com/RaghurajSawant/MachineLearning/master/Statistics/Measures_Of_Central_Tendency/Mode/mode.csv")
data.head(5)

# Use the mean function on the 'Overall Marks' column of the dataset
data["Overall Marks"].median()

# Capturing the quartiles of the dataset
Q1 = data["Overall Marks"].quantile(0.25)
Q2 = data["Overall Marks"].quantile(0.50)
Q3 = data["Overall Marks"].quantile(0.75)
Q4 = data["Overall Marks"].quantile(1)

print(f"Q1 : {Q1} \n Q2 : {Q2} \n Q3 : {Q3} \n Q4 : {Q4} \n")
