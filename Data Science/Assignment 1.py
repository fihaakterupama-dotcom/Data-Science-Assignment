import pandas as pd

# Load CSV dataset from the internet
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"

df = pd.read_csv(url)

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Show column names
print("\nColumn Names:")
print(df.columns.tolist())

# Display number of rows and columns
print("\nNumber of Rows:", df.shape[0])
print("Number of Columns:", df.shape[1])

# Show summary statistics
print("\nSummary Statistics:")
print(df.describe(include='all'))