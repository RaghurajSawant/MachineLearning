

# Import the library
import pandas as pd

# Load the dataset
data = pd.read_csv(r"D:\Raghuraj\Courses\Analytics Vidya\Applied ML\AppliedMLHandouts\Applied ML Handouts\Module 6_ Statistics for Data Science\Descriptive\mode.csv")
data.head(5)

# Use the mode function on the 'Subject' column of the dataset
data["Subject"].mode()
