import pandas as pd

# Load dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"

df = pd.read_csv(url)

# Create a new column
df["Average Score"] = (
    df["sepal_length"] +
    df["sepal_width"] +
    df["petal_length"] +
    df["petal_width"]
) / 4

# Apply a condition
df["Category"] = df["Average Score"].apply(
    lambda x: "High" if x >= 3.5 else "Low"
)

print(df.head())